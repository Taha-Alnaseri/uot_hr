import frappe

@frappe.whitelist()
def get_current_employee():
    """Get the Employee record for the currently logged in user - no permission check needed"""
    user = frappe.session.user

    result = frappe.db.sql("""
        SELECT name, employee_department_or_division
        FROM `tabUOT Employees`
        WHERE employee_user = %s
        LIMIT 1
    """, user, as_dict=True)

    return result[0] if result else {}
