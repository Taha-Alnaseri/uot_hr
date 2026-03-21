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

        dept_list = ", ".join(f"'{d}'" for d in managed_departments)
        employees_in_dept = frappe.db.sql(f"""
            SELECT name FROM `tabUOT Employees`
            WHERE employee_department_or_division IN ({dept_list})
        """, as_list=True)

        if not employees_in_dept:
            return "1=0"

        emp_list = ", ".join(f"'{e[0]}'" for e in employees_in_dept)
        return f"`tabUOT Leave Request`.employee IN ({emp_list})"

    employee = frappe.db.get_value(
        "UOT Employees",
        {"employee_user": user},
        "name"
    )
    if not employee:
        return "1=0"

    return f"`tabUOT Leave Request`.employee = '{employee}'"


def get_employee_permission_query_conditions(user=None):
    if not user:
        user = frappe.session.user

    if "System Manager" in frappe.get_roles(user):
        return ""

    roles = frappe.get_roles(user)

    # Full access roles
    if any(r in roles for r in ["UOT Dean", "UOT HR Manager", "UOT Administrative Associate"]):
        return ""

    # Department Manager: see only their department's employees
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

        dept_list = ", ".join(f"'{d}'" for d in managed_departments)
        return f"`tabUOT Employees`.employee_department_or_division IN ({dept_list})"

    # Regular Employee: can only see their own record
    result = frappe.db.sql("""
        SELECT name FROM `tabUOT Employees`
        WHERE employee_user = %s
        LIMIT 1
    """, user, as_list=True)

    if not result:
        return "1=0"

    return f"`tabUOT Employees`.name = '{result[0][0]}'"


def get_user_permission_query_conditions(user=None):
    if not user:
        user = frappe.session.user

    if "System Manager" in frappe.get_roles(user):
        return ""

    roles = frappe.get_roles(user)

    # Full access roles
    if any(r in roles for r in ["UOT Dean", "UOT HR Manager", "UOT Administrative Associate"]):
        return ""

    # Everyone else can only see their own user record
    return f"`tabUser`.`name` = '{user}'"