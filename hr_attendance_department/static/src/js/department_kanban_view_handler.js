odoo.define('hr_attendance_department.employee_kanban_view_handler', function(require) {
"use strict";

var KanbanRecord = require('web.KanbanRecord');


KanbanRecord.include({
    _openRecord: function () {
        if (this.modelName === 'hr.department' && this.$el.parents('.o_hr_department_attendance_kanban').length) {
            var action = {
                type: this.state.context.type,
                name: this.state.context.name,
                tag: this.state.context.tag,
                employee_id: this.state.context.employee_id,
                employee_name: this.state.context.employee_name,
                employee_state: this.state.context.employee_state,
                department_id: this.record.id.raw_value,
                department_name: this.record.name.raw_value,
            };
            this.do_action(action);
        } else {
            this._super.apply(this, arguments);
        }
    }
});

});
