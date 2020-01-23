# -*- coding: utf-8 -*-

from odoo import _, api, fields, models, tools


class IrUiMenu(models.Model):
    _inherit = 'ir.ui.menu'

    company_id = fields.Many2one('res.company', string='Company')

    @api.model
    @tools.ormcache('frozenset(self.env.user.groups_id.ids)', 'debug')
    def _visible_menu_ids(self, debug=False):
        visible = self.browse()
        res = super(IrUiMenu, self)._visible_menu_ids(debug)
        company_id = self.env.user.company_id.id
        for menu in self.browse(res):
            if menu.company_id:
                if menu.company_id.id == company_id:
                    visible += menu
            else:
                visible += menu
        return set(visible.ids)
