import frappe

def get_permission_query_conditions(user=None):
    if not user:
        user = frappe.session.user

    # 1. System Admins and High-Level Roles see everything
    roles = frappe.get_roles(user)
    unrestricted_roles = ["System Manager", "UOT Dean", "UOT HR Manager", "UOT Administrative Associate"]
    
    if any(role in roles for role in unrestricted_roles):
        return ""

    # 2. Identify the logged-in user's Employee ID
    emp_name = frappe.db.get_value(
        "UOT Employees",
        {"employee_user": user},
        "name"
    )
    
    if not emp_name:
        return "1=0" # If they aren't linked to an employee profile, they see nothing

    # 3. Start a Set with their OWN ID (This guarantees they always see their own records)
    allowed_employees = set([emp_name])

    # 4. If they are a Department Manager, find their staff and add them to the Set
    if "UOT Department manager" in roles:
        
        # Find all departments where this employee is set as the manager
        managed_departments = frappe.get_all(
            "UOT Departments",
            filters={"department_manager": emp_name},
            pluck="name"
        )

        if managed_departments:
            # Find all employees working in those managed departments
            employees_in_dept = frappe.get_all(
                "UOT Employees",
                filters={"employee_department_or_division": ("in", managed_departments)},
                pluck="name"
            )
            
            if employees_in_dept:
                # Add all staff IDs to the allowed list
                allowed_employees.update(employees_in_dept)

    # 5. Build the final SQL IN clause securely
    emp_list = ", ".join(frappe.db.escape(emp) for emp in allowed_employees)
    return f"`tabUOT Leave Request`.employee IN ({emp_list})"


def get_employee_permission_query_conditions(user=None):
    if not user:
        user = frappe.session.user

    roles = frappe.get_roles(user)
    
    # 1. System Admins and High-Level Roles see everything
    if any(r in roles for r in ["System Manager", "UOT Dean", "UOT HR Manager", "UOT Administrative Associate"]):
        return ""

    # 2. Get the logged-in user's personal Employee ID
    emp_name = frappe.db.get_value(
        "UOT Employees",
        {"employee_user": user},
        "name"
    )
    
    if not emp_name:
        return "1=0"

    # 3. Department Manager Logic
    if "UOT Department manager" in roles:
        managed_departments = frappe.get_all(
            "UOT Departments",
            filters={"department_manager": emp_name},
            pluck="name"
        )
        
        if managed_departments:
            dept_list = ", ".join(frappe.db.escape(d) for d in managed_departments)
            # THE FIX: Use an OR condition so their own record is always visible
            return f"(`tabUOT Employees`.employee_department_or_division IN ({dept_list}) OR `tabUOT Employees`.name = {frappe.db.escape(emp_name)})"

    # 4. Standard Employee fallback (or Manager with no assigned departments yet)
    return f"`tabUOT Employees`.name = {frappe.db.escape(emp_name)}"

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