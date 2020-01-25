from odoo import models, fields


class CirclesTention(models.Model):
    _name = 'circles.tention'
    _description = 'circles.tention'

    task_id = fields.Many2one('project.task', string='Task')
