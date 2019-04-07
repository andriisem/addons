from odoo import models, fields


class HrAttendance(models.Model):
    _inherit = "hr.attendance"

    department_restaurant_id = fields.Many2one('hr.department.restaurant', "Department", readonly=False)
