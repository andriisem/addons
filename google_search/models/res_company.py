from odoo import models, fields


class ResCompany(models.Model):
    _inherit = 'res.company'

    google_search_id = fields.Char(string='Search Engine ID')
    