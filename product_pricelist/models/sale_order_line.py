# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrderInherited(models.Model):
    _inherit = "sale.order.line"

    pricelist_id = fields.Many2one("product.pricelist", string="Pricelist")

    @api.onchange("product_id")
    def onchange_product_id(self):
        """Method to set the lowest price unit"""
        if self.product_id:
            pricelist_id = (
                self.env["product.pricelist"]
                .search([])
                .item_ids.filtered(
                    lambda l: l.product_tmpl_id.id
                    == self.product_id.product_tmpl_id.id
                )
            )
            if pricelist_id and len(pricelist_id) > 1:
                min_pricelist = min(pricelist_id.mapped("fixed_price"))
                pricelist = pricelist_id.filtered(
                    lambda l: l.fixed_price == min_pricelist
                )
                if pricelist:
                    self.pricelist_id = pricelist[-1].id
                    self.price_unit = min_pricelist
                else:
                    self.pricelist_id = self.order_id.pricelist_id.id
