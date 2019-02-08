from odoo import models, fields


class HrAttendance(models.Model):
    _inherit = "hr.attendance"

    department_id = fields.Many2one('hr.department', "Department", related='', readonly=False)
