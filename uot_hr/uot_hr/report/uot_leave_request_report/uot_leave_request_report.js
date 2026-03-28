// Copyright (c) 2026, Eng. Taha Al-Naseri and contributors
// For license information, please see license.txt

frappe.query_reports["uot leave request report"] = {
	"filters": 
			[
				{
					"fieldname": "data_lprk",
					"label": "الاسم الكامل",
					"fieldtype": "Data",
					"default": ""
				},
				{
					"fieldname": "from_day",
					"label": "من تاريخ",
					"fieldtype": "Date",
					"default": ""
				},
				{
					"fieldname": "to_day",
					"label": "إلى تاريخ",
					"fieldtype": "Date",
					"default": ""
				},
				{
					"fieldname": "workflow_state",
					"label": "حالة الطلب",
					"fieldtype": "Select",
					"options": "\nPending\napproved by the line manager\nApproved by the Administrative Associate\nApproved\nRejected",
					"default": ""
				},
				{
					"fieldname": "leave_type",
					"label": "نوع الإجازة",
					"fieldtype": "Link",
					"options": "UOT Leave Type",
					"default": ""
				}
			]
};


