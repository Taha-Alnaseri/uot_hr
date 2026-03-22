import frappe


def get_permission_query_conditions(user=None):
    if not user:
        user = frappe.session.user

    if "System Manager" in frappe.get_roles(user):
        return ""

    roles = frappe.get_roles(user)

    if "UOT Dean" in roles:
        return ""

    if "UOT HR Manager" in roles:
        return ""

    if "UOT Administrative Associate" in roles:
        return ""

    if "UOT Department manager" in roles:
        manager_employee = frappe.db.get_value(
            "UOT Employees",
            {"employee_user": user},
            "name"
        )
        if not manager_employee:
            return "1=0"

        managed_departments = frappe.get_all(
            "UOT Departments",
            filters={"department_manager": manager_employee},
            pluck="name"
        )
        if not managed_departments:
            return "1=0"

        # FIXED: use parameterized query
        placeholders = ", ".join(["%s"] * len(managed_departments))
        employees_in_dept = frappe.db.sql(f"""
            SELECT name FROM `tabUOT Employees`
            WHERE employee_department_or_division IN ({placeholders})
        """, managed_departments, as_list=True)

        if not employees_in_dept:
            return "1=0"

        # FIXED: use frappe.db.escape
        emp_list = ", ".join(
            frappe.db.escape(e[0]) for e in employees_in_dept
        )
        return f"`tabUOT Leave Request`.employee IN ({emp_list})"

    employee = frappe.db.get_value(
        "UOT Employees",
        {"employee_user": user},
        "name"
    )
    if not employee:
        return "1=0"

    # FIXED: use frappe.db.escape
    return f"`tabUOT Leave Request`.employee = {frappe.db.escape(employee)}"


def get_employee_permission_query_conditions(user=None):
    if not user:
        user = frappe.session.user

    if "System Manager" in frappe.get_roles(user):
        return ""

    roles = frappe.get_roles(user)

    if any(r in roles for r in ["UOT Dean", "UOT HR Manager", "UOT Administrative Associate"]):
        return ""

    if "UOT Department manager" in roles:
        manager_employee = frappe.db.sql("""
            SELECT name FROM `tabUOT Employees`
            WHERE employee_user = %s
            LIMIT 1
        """, user, as_list=True)

        if not manager_employee:
            return "1=0"

        managed_departments = frappe.get_all(
            "UOT Departments",
            filters={"department_manager": manager_employee[0][0]},
            pluck="name"
        )
        if not managed_departments:
            return "1=0"

        # FIXED: use frappe.db.escape
        dept_list = ", ".join(
            frappe.db.escape(d) for d in managed_departments
        )
        return f"`tabUOT Employees`.employee_department_or_division IN ({dept_list})"

    result = frappe.db.sql("""
        SELECT name FROM `tabUOT Employees`
        WHERE employee_user = %s
        LIMIT 1
    """, user, as_list=True)

    if not result:
        return "1=0"

    # FIXED: use frappe.db.escape
    return f"`tabUOT Employees`.name = {frappe.db.escape(result[0][0])}"


def get_user_permission_query_conditions(user=None):
    if not user:
        user = frappe.session.user

    if "System Manager" in frappe.get_roles(user):
        return ""

    roles = frappe.get_roles(user)

    if any(r in roles for r in ["UOT Dean", "UOT HR Manager", "UOT Administrative Associate"]):
        return ""

    # FIXED: use frappe.db.escape
    return f"`tabUser`.`name` = {frappe.db.escape(user)}"