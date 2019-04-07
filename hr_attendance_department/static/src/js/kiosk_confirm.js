odoo.define('hr_attendance_department.kiosk_confirm', function (require) {
    "use strict";

    var KioskConfirm = require('hr_attendance.kiosk_confirm');
    var AbstractAction = require('web.AbstractAction');

    KioskConfirm.include({
        events: _.extend({}, KioskConfirm.prototype.events, {
            "click .o_hr_attendance_sign_in_out_icon": function () {
                var self = this;
                this.$('.o_hr_attendance_sign_in_out_icon').attr("disabled", "disabled");
                var e = document.getElementById("reasons");
                if (e) {
                    var reasons = e.options[e.selectedIndex].value;
                }

                this._rpc({
                    model: 'hr.employee',
                    method: 'attendance_manual',
                    args: [[this.employee_id], this.next_action],
                    context: {department_restaurant_id: this.department_restaurant_id, clock_reason_id: reasons}
                }).then(function(result) {
                    if (result.action) {
                        self.do_action(result.action);
                    } else if (result.warning) {
                        self.do_warn(result.warning);
                        self.$('.o_hr_attendance_sign_in_out_icon').removeAttr("disabled");
                    }
                });
                },

            'click .o_hr_attendance_pin_pad_button_ok': function() {
                var self = this;
                this.$('.o_hr_attendance_pin_pad_button_ok').attr("disabled", "disabled");
                var e = document.getElementById("reasons");
                if (e) {
                    var reasons = e.options[e.selectedIndex].value;
                }
                this._rpc({
                    model: 'hr.employee',
                    method: 'attendance_manual',
                    args: [[this.employee_id], this.next_action, this.$('.o_hr_attendance_PINbox').val()],
                    context: {department_restaurant_id: this.department_restaurant_id, clock_reason_id: reasons}
                }).then(function(result) {
                    if (result.action) {
                        self.do_action(result.action);
                    } else if (result.warning) {
                        self.do_warn(result.warning);
                        self.$('.o_hr_attendance_PINbox').val('');
                        setTimeout( function() { self.$('.o_hr_attendance_pin_pad_button_ok').removeAttr("disabled"); }, 500);
                    }
                });
            }
        }),
    });

    AbstractAction.include({
        init: function (parent, action) {
            this._super.apply(this, arguments);
            this.department_restaurant_id = action.department_restaurant_id;
            this.department_name = action.department_name;
            },
    });

});