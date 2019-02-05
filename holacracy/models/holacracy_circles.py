from odoo import models, fields


class HolacracyCircles(models.Model):
    _name = 'holacracy.circles'
    _description = 'holacracy.circles'

    name = fields.Char(string='Name')
    lead_link = fields.Many2one('hr.employee', string='Lead Link')
    rep_link = fields.Many2one('hr.employee', string='Rep Link')
    purpose = fields.Char(string='Purpose')
    notes = fields.Text(string='Notes')
    parent_id = fields.Many2one('holacracy.circles', string='Related Circle', index=True)
    child_ids = fields.One2many('holacracy.circles', 'parent_id', string='Contacts')
    circles_role_ids = fields.Many2many('circles.roles', string='Role')
    tention_ids = fields.One2many('circles.tention', 'task_id', string='Tention')
