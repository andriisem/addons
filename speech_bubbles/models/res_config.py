from odoo import models, fields


class ResConfig(models.TransientModel):
    _inherit = 'res.config.settings'

    use_speech_bubbles = fields.Boolean(string='Use Speech Bubbles', related='company_id.use_speech_bubbles')
