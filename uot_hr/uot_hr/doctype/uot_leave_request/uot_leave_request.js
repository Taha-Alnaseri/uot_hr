// Copyright (c) 2026, Eng. Taha Al-Naseri and contributors
// For license information, please see license.txt

// frappe.ui.form.on("UOT Leave Request", {
// 	refresh(frm) {

// 	},
// });
// Let's see if the file is even loading!
console.log("1. JS File is on the server!");

frappe.ui.form.on("UOT Leave Request", {
    
    // THIS IS THE NEW TEST!
    refresh: function(frm) {
        console.log("2. SUCCESS! The DocType name matches and the form is awake!");
    },
    
    from_day: function(frm) {
        console.log("3. Start date changed!");
        frm.trigger('to_day');
    },

    to_day: function(frm) {
        console.log("4. End date changed! Checking math...");
        
        if (frm.doc.from_day && frm.doc.to_day) {
            if (frm.doc.from_day > frm.doc.to_day) {
                frappe.msgprint("Error: Your Start Date cannot be after your End Date!");
                frm.set_value('to_day', ''); 
                frm.set_value('days_count_of_leave', 0);
            } 
            else {
                let diff = frappe.datetime.get_day_diff(frm.doc.to_day, frm.doc.from_day) + 1;
                frm.set_value('days_count_of_leave', diff);
            }
        }
    }
});


frappe.ui.form.on('UOT Leave Request', {
    onload: function(frm) {
        if (frm.is_new()) {
            frappe.call({
                method: 'uot_hr.uot_hr.api.get_current_employee',
                callback: function(r) {
                    if (r.message && r.message.name) {
                        frm.set_value('employee', r.message.name);
                        // Refresh form so all dependent fields appear
                        frm.refresh_fields();
                    }
                }
            });
        }
    }
});
