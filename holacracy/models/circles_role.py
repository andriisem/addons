from odoo import models, fields


class RoleType(models.Model):
    _name = 'role.type'
    _description = 'role.type'

    name = fields.Char(string='Name', required=True)


class CirclesRole(models.Model):
    _name = 'circles.roles'
    _description = 'circles.roles'

    name = fields.Char(string='Name', required=True)
    type_role = fields.Many2one('role.type', string='Type', required=True)
    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    goals = fields.Char(string='Goals')
    kpi = fields.Char(string='KPI')
    expectations = fields.Char(string='Expectations')
