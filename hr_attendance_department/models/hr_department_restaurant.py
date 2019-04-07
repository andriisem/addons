from odoo import models, fields


class DepartmentRestaurant(models.Model):
    _name = "hr.department.restaurant"
    _description = "HR Department Restaurant"

    name = fields.Char('Department Name', required=True)
    active = fields.Boolean('Active', default=True)
    parent_id = fields.Many2one('hr.department.restaurant', string='Parent Department', index=True)
    child_ids = fields.One2many('hr.department.restaurant', 'parent_id', string='Child Departments')
    manager_id = fields.Many2one('hr.employee', string='Manager', track_visibility='onchange')
