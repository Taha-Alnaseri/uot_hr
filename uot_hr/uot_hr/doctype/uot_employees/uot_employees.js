// Copyright (c) 2026, Eng. Taha Al-Naseri and contributors
// For license information, please see license.txt

// frappe.ui.form.on("UOT Employees", {
// 	refresh(frm) {

// 	},
// });

// 1. Define the logic once in a helper function
function update_full_name(frm) {
    // Check if ALL five fields are filled out
    if (
        frm.doc.first_name && 
        frm.doc.father_name && 
        frm.doc.grandfather_name && 
        frm.doc.great_grandfather_name && 
        frm.doc.family_name
    ) {
        // Combine them
        let combined_name = 
            frm.doc.first_name + " " + 
            frm.doc.father_name + " " + 
            frm.doc.grandfather_name + " " + 
            frm.doc.great_grandfather_name + " " + 
            frm.doc.family_name;
            
        frm.set_value("employee_full_name", combined_name);
    } else {
        // If even one field is missing, clear the full name
        frm.set_value("employee_full_name", "");
    }
}

// 2. Trigger that function whenever any of these fields change
frappe.ui.form.on("UOT Employees", {
    first_name: update_full_name,
    father_name: update_full_name,
    grandfather_name: update_full_name,
    great_grandfather_name: update_full_name,
    family_name: update_full_name
});