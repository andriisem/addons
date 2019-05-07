from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    google_search_id = fields.Char(string='Search Engine ID', related='company_id.google_search_id', readonly=False)
