from odoo import models, api, fields, exceptions, _


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    department_id = fields.Many2one('hr.department', "Department", required=True)

    @api.multi
    def attendance_action_change(self):
        """ Check In/Check Out action
            Check In: create a new attendance record
            Check Out: modify check_out field of appropriate attendance record
        """
        if len(self) > 1:
            raise exceptions.UserError(_('Cannot perform check in or check out on multiple employees.'))
        action_date = fields.Datetime.now()

        if self.attendance_state != 'checked_in':
            vals = {
                'employee_id': self.id,
                'check_in': action_date,
                'department_id': self._context.get('department_id')
            }
            return self.env['hr.attendance'].create(vals)
        else:
            attendance = self.env['hr.attendance'].search([('employee_id', '=', self.id), ('check_out', '=', False)],
                                                          limit=1)
            if attendance:
                attendance.check_out = action_date
            else:
                raise exceptions.UserError(
                    _('Cannot perform check out on %(empl_name)s, could not find corresponding check in. '
                      'Your attendances have probably been modified manually by human resources.') % {
                        'empl_name': self.name, })
            return attendance
