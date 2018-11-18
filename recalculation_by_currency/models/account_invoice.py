from odoo import models, api, fields


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.onchange('currency_id', 'date_invoice')
    def recalculation_amount_by_currency(self):
        for inv in self:
            if inv.origin:
                current_date = inv.date_invoice or fields.Date.today()
                sale_order = inv.env['sale.order'].search([('name', '=', inv.origin)])
                currency = inv.currency_id
                from_currency = sale_order.currency_id.with_context(date=current_date)
                to_currency = inv.currency_id.with_context(date=current_date)
                for inv_line in inv.invoice_line_ids:
                    inv_line.price_unit = currency._compute(from_currency, to_currency,
                                                            inv_line.sale_line_ids.price_unit)
