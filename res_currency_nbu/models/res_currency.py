# -*- coding: utf-8 -*-

from odoo import api, models
from ..utils.parse_rates import get_rates_by_code


class ResCurrency(models.Model):
    _inherit = 'res.currency'

    @api.model
    def _parse_nbu_rates(self):
        company_ids = self.env['res.company'].search([])
        for company in company_ids:

            active_currencies = company.currency_id.search([('active', '=', 't')])
            curr_codes = active_currencies.mapped('name')

            rates_dict = get_rates_by_code(curr_codes)

            default_currency = company.currency_id.env.ref('base.main_company').currency_id

            rates_dict = {
                k: (v/rates_dict[default_currency.name]) for
                (k, v) in rates_dict.items()
            }

            for currency in active_currencies:
                self.env['res.currency.rate'].create(
                    {
                        'currency_id': currency.id,
                        'rate': rates_dict[currency.name],
                        'company_id': company.id
                    })

    @api.multi
    def action_parse_nbu_rates(self):
        self._parse_nbu_rates()
