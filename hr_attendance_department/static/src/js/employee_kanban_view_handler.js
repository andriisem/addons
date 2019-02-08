odoo.define('hr_attendance_department.department_kanban_view_handler', function(require) {
    "use strict";

    var KanbanRecord = require('web.KanbanRecord');

    KanbanRecord.include({
        _openRecord: function () {
            var self = this;
            if (this.modelName === 'hr.employee' && this.$el.parents('.o_hr_employee_attendance_kanban').length) {
                $.when(self._child_department_employee()).done(function() {
                    self._rpc({
                        model: 'ir.model.data',
                        method: 'xmlid_to_res_id',
                        kwargs: {xmlid: 'hr_attendance_department.hr_department_view_kanban'},
                    }).then(function (view_id) {
                        self.do_action({
                            type: 'ir.actions.act_window',
                            name: 'Department',
                            res_model: "hr.department",
                            views: [[view_id, 'kanban']],
                            domain: [['id', 'in', self.recordData.childs]],
                            target: 'current',
                            context: {
                                type: 'ir.actions.client',
                                name: 'Confirm',
                                tag: 'hr_attendance_kiosk_confirm',
                                employee_id: self.record.id.raw_value,
                                employee_name: self.record.name.raw_value,
                                employee_state: self.record.attendance_state.raw_value,
                            },
                        });
                    });
                });
            } else {
                this._super.apply(this, arguments);
            }
        },

        _child_department_employee: function () {
            var self =  this;
            var def = this._rpc({
                model: 'hr.department',
                method: 'search_read',
                domain: [['id', '=', self.recordData.department_id.data.id]],
                fields: ['name', 'child_ids']
            }).then(function (record) {
                self.recordData.childs = record[0].child_ids;
            });
            return def
        }
    });
});
