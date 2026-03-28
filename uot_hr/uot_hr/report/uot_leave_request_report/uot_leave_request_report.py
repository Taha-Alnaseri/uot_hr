# Copyright (c) 2026, Eng. Taha Al-Naseri and contributors
# For license information, please see license.txt

# import frappe


def execute(filters=None):
	columns, data = [], []
	return columns, data

import frappe
from frappe import _  # Import the translation function
from frappe.desk.reportview import get_match_cond  # <--- CORRECT IMPORT FOR PERMISSIONS

def execute(filters=None):
    if not filters:
        filters = {}
        
    columns = get_columns()
    data = get_data(filters)
    
    return columns, data

def get_columns():
    # Wrap all labels in _() to make them translatable
    return [
        {"label": _("الاسم الكامل"), "fieldname": "data_lprk", "fieldtype": "Data", "width": 200},
        {"label": _("عدد أيام الإجازة"), "fieldname": "days_count_of_leave", "fieldtype": "Int", "width": 150},
        {"label": _("من تاريخ"), "fieldname": "from_day", "fieldtype": "Date", "width": 120},
        {"label": _("إلى تاريخ"), "fieldname": "to_day", "fieldtype": "Date", "width": 120},
        {"label": _("نوع الإجازة"), "fieldname": "leave_type", "fieldtype": "Data", "width": 150},
        {"label": _("حالة الطلب"), "fieldname": "workflow_state", "fieldtype": "Data", "width": 150}
    ]

def get_data(filters):
    conditions = get_conditions(filters)
    
    # --- 1. THE PERMISSION FIX ---
    match_conditions = get_match_cond("UOT Leave Request")
    
    # If the user has permission restrictions, append them cleanly
    if match_conditions:
        # Clean up empty spaces
        match_conditions = match_conditions.strip()
        
        # Prevent the "AND and" SQL syntax error
        if match_conditions.lower().startswith("and"):
            conditions += f" {match_conditions}"  # Frappe already included 'and'
        else:
            conditions += f" AND {match_conditions}" # We need to add 'AND'
    
    # Run the SQL Query 
    raw_data = frappe.db.sql(f"""
        SELECT
            `tabUOT Leave Request`.data_lprk,
            `tabUOT Leave Request`.days_count_of_leave,
            `tabUOT Leave Request`.from_day,
            `tabUOT Leave Request`.to_day,
            lt.leave_type AS leave_type, 
            `tabUOT Leave Request`.workflow_state
        FROM `tabUOT Leave Request`
        LEFT JOIN `tabUOT Leave Type` lt ON `tabUOT Leave Request`.leave_type = lt.name
        WHERE `tabUOT Leave Request`.docstatus < 2
        {conditions}
        ORDER BY `tabUOT Leave Request`.data_lprk ASC
    """, filters, as_dict=True)

    # --- 2. THE DATA TRANSLATION FIX ---
    # Loop through the results and translate the actual table data
    for row in raw_data:
        if row.get("workflow_state"):
            row["workflow_state"] = _(row["workflow_state"])
            
        if row.get("leave_type"):
            row["leave_type"] = _(row["leave_type"])

    return raw_data


def get_conditions(filters):
    conditions = []

    if filters.get("data_lprk"):
        conditions.append("`tabUOT Leave Request`.data_lprk LIKE %(data_lprk)s")
        filters["data_lprk"] = f"%{filters['data_lprk']}%"

    if filters.get("from_day"):
        conditions.append("`tabUOT Leave Request`.from_day >= %(from_day)s")

    if filters.get("to_day"):
        conditions.append("`tabUOT Leave Request`.to_day <= %(to_day)s")

    if filters.get("workflow_state"):
        conditions.append("`tabUOT Leave Request`.workflow_state = %(workflow_state)s")

    if filters.get("leave_type"):
        conditions.append("`tabUOT Leave Request`.leave_type = %(leave_type)s")

    return " AND " + " AND ".join(conditions) if conditions else ""