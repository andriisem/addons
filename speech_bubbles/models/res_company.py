from odoo import models, fields


class Company(models.Model):
    _inherit = 'res.company'

    use_speech_bubbles = fields.Boolean(string='Use Speech Bubbles')
