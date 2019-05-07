
from odoo import http, registry
from odoo.http import request


class GoogleEngine(http.Controller):

    @http.route('/get/engine_id', type='json', auth="none")
    def get_engine(self):
        vals = {}
        vals['engine_id'] = request.env['res.company']._get_main_company().google_search_id
        return vals
