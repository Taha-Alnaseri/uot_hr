# Copyright (c) 2026, Eng. Taha Al-Naseri and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class UOTLeaveRequest(Document):
	pass
import frappe
from frappe.model.document import Document

class UOTLeaveRequest(Document):
    pass  # your existing code stays here


def has_permission(doc, ptype="read", user=None):
    if not user:
        user = frappe.session.user

    if "System Manager" in frappe.get_roles(user):
        return True

    roles = frappe.get_roles(user)

    # ── UOT Dean, HR Manager, Admin Associate: full access ───────────────
    if any(r in roles for r in ["UOT Dean", "UOT HR Manager", "UOT Administrative Associate"]):
        return True

    # ── UOT Department manager ───────────────────────────────────────────
    if "UOT Department manager" in roles:
        manager_employee = frappe.db.get_value(
            "UOT Employees",
            {"employee_user": user},
            "name"
        )
        if not manager_employee:
            return False

        managed_departments = frappe.get_all(
            "UOT Departments",
            filters={"department_manager": manager_employee},
            pluck="name"
        )

        emp_dept = frappe.db.get_value(
            "UOT Employees",
            doc.employee,
            "employee_department_or_division"
        )
        return emp_dept in managed_departments

    # ── UOT Employee ─────────────────────────────────────────────────────
    if "UOT Employee" in roles:
        # Allow create (doc is new, employee field may be empty yet)
        if ptype == "create":
            return True

        employee = frappe.db.get_value(
            "UOT Employees",
            {"employee_user": user},
            "name"
        )
        return doc.employee == employee

    return False