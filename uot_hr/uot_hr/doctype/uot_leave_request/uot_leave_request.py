# Copyright (c) 2026, Eng. Taha Al-Naseri and contributors
# For license information, please see license.txt

# import frappe

import frappe
from frappe.model.document import Document

class UOTLeaveRequest(Document):
    def validate(self):
        if self.attachment_for_leave_request:
            if not self.attachment_for_leave_request.lower().endswith('.pdf'):
                frappe.throw(
                    '<div style="direction:rtl; text-align:right;">'
                    'يجب أن يكون المرفق بصيغة PDF فقط'
                    '</div>',
                    title='<div style="direction:rtl; text-align:right;">خطأ في المرفق</div>'
                )

# ── PERMISSION HOOK MUST BE OUTSIDE THE CLASS ────────────────────────────
# Added **kwargs to prevent TypeError from hooks.py
def has_permission(doc, ptype="read", user=None, **kwargs):
    if not user:
        user = frappe.session.user

    roles = frappe.get_roles(user)

    # 1. High-Level Roles: Full Access
    # Included your exact spelling from hooks.py ('associte') just to be safe!
    unrestricted_roles = [
        "System Manager", "UOT Dean", "UOT HR Manager", 
        "UOT Administrative Associate", "UOT Administrative associte"
    ]
    if any(r in roles for r in unrestricted_roles):
        return True

    # 2. Get Logged-in User's Employee ID
    logged_in_employee = frappe.db.get_value(
        "UOT Employees",
        {"employee_user": user},
        "name"
    )

    # CRITICAL: If the user is not linked to an Employee Profile, deny access
    if not logged_in_employee:
        return False

    # 3. Handle Empty or String Documents safely
    if not doc or isinstance(doc, str):
        return True if ptype == "create" else None

    # Safely check is_new (prevents AttributeError on dictionaries)
    if hasattr(doc, "is_new") and doc.is_new():
        return True
    if ptype == "create":
        return True

    # 4. UNIVERSAL RULE: Everyone can manage their OWN records
    if getattr(doc, "employee", None) == logged_in_employee:
        return True

    # 5. UOT Department Manager Logic
    if "UOT Department Manager" in roles or "UOT Department manager" in roles:
        managed_departments = frappe.get_all(
            "UOT Departments",
            filters={"department_manager": logged_in_employee},
            pluck="name"
        )

        if getattr(doc, "employee", None) and managed_departments:
            emp_dept = frappe.db.get_value(
                "UOT Employees",
                doc.employee,
                "employee_department_or_division"
            )
            if emp_dept in managed_departments:
                return True

    # 6. Fallback
    return False