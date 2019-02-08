odoo.define('hr_attendance_department.kiosk_confirm', function (require) {
    "use strict";

    var KioskConfirm = require('hr_attendance.kiosk_confirm');
    var AbstractAction = require('web.AbstractAction');

    KioskConfirm.include({
        events: _.extend({}, KioskConfirm.prototype.events, {
            "click .o_hr_attendance_sign_in_out_icon": function () {
                var self = this;
                this.$('.o_hr_attendance_sign_in_out_icon').attr("disabled", "disabled");
                this._rpc({
                    model: 'hr.employee',
                    method: 'attendance_manual',
                    args: [[this.employee_id], this.next_action],
                    context: {department_id: this.department_id}
                }).then(function(result) {
                    if (result.action) {
                        self.do_action(result.action);
                    } else if (result.warning) {
                        self.do_warn(result.warning);
                        self.$('.o_hr_attendance_sign_in_out_icon').removeAttr("disabled");
                    }
                });
                },
        }),
    });

    AbstractAction.include({
        init: function (parent, action) {
            this._super.apply(this, arguments);
            this.department_id = action.department_id;
            this.department_name = action.department_name;
            },
    });

});