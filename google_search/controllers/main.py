
from odoo import http, registry
from odoo.http import request


class GoogleEngine(http.Controller):

    @http.route('/get/engine_id', type='json', auth="none")
    def get_engine(self):
        google_search_id = request.env['ir.config_parameter'].sudo().get_param('google.google_search_id')
        return {'engine_id': google_search_id}
