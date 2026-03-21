import frappe

@frappe.whitelist()
def get_current_employee():
    """Get the Employee record for the currently logged in user"""
    user = frappe.session.user

    result = frappe.db.sql("""
        SELECT name, employee_department_or_division
        FROM `tabUOT Employees`
        WHERE employee_user = %s
        LIMIT 1
    """, user, as_dict=True)

    return result[0] if result else {}


def sync_custom_permissions():
    """
    After every migrate, sync custom permissions from DocType JSON
    into the Role Permission Manager so both systems are always in sync.
    """
    doctypes = [
        "UOT Leave Request",
        "UOT Employees",
        "UOT Departments",
        "UOT Leave Type",
        "UOT Employee Type"
    ]

    for doctype in doctypes:
        # Step 1: Clear existing custom permissions
        frappe.db.delete("Custom DocPerm", {"parent": doctype})

        # Step 2: Read standard permissions from DocType JSON
        standard_perms = frappe.get_all(
            "DocPerm",
            filters={"parent": doctype},
            fields=[
                "role", "read", "write", "create",
                "delete", "submit", "cancel", "amend",
                "select", "permlevel"
            ]
        )

        # Step 3: Write them into Custom DocPerm
        for perm in standard_perms:
            custom_perm = frappe.get_doc({
                "doctype": "Custom DocPerm",
                "parent": doctype,
                "parenttype": "DocType",
                "parentfield": "permissions",
                "role": perm.role,
                "read": perm.read,
                "write": perm.write,
                "create": perm.create,
                "delete": perm.delete,
                "submit": perm.submit,
                "cancel": perm.cancel,
                "amend": perm.amend,
                "select": perm.select,
                "permlevel": perm.permlevel
            })
            custom_perm.insert(ignore_permissions=True)

        print("Synced permissions for: " + doctype)

    frappe.db.commit()
    print("Permission sync complete!")