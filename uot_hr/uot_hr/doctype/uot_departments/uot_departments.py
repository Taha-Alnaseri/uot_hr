# Copyright (c) 2026, Eng. Taha Al-Naseri and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class UOTDepartments(Document):
	pass

import frappe
from frappe.model.document import Document

class UOTDepartments(Document):
    def on_update(self):
        # 1. Find all employees that belong to this specific department
        employees_in_dept = frappe.get_all(
            "UOT Employees",
            filters={"employee_department_or_division": self.name},
            pluck="name"
        )

        # 2. If we found employees, update their manager field to match the new department manager
        if employees_in_dept:
            for employee in employees_in_dept:
                # Replace 'department_manager_user' with the EXACT field name in your UOT Employees DocType
                # Replace 'department_manager' with the EXACT field name in your UOT Departments DocType
                frappe.db.set_value(
                    "UOT Employees", 
                    employee, 
                    "department_manager_user", # <--- CHANGE THIS IF NEEDED
                    self.manager_user    # <--- CHANGE THIS IF NEEDED
                )