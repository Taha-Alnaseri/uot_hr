// Copyright (c) 2026, Eng. Taha Al-Naseri and contributors
// For license information, please see license.txt

// frappe.ui.form.on("UOT Departments", {
// 	refresh(frm) {

// 	},
// });


frappe.ui.form.on('UOT Departments', {
    dep_prefix: function(frm) {
        if (frm.doc.dep_prefix && frm.doc.dep_prefix.length > 3) {
            frappe.msgprint({
                title: 'خطأ',
                message: 'حقل المختصر للقسم يجب ان يكون ثلاث احرف او اقل',
                indicator: 'red'
            });
            setTimeout(() => {
                $('.msgprint-dialog .modal-body').css({
                    'direction': 'rtl',
                    'text-align': 'right'
                });
            }, 100);
            // Clear the extra characters
            frm.set_value('dep_prefix', 
                frm.doc.dep_prefix.substring(0, 3));
        }
    }
});