from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    google_search_id = fields.Char(string='Search Engine ID', config_parameter='google_search_id')
