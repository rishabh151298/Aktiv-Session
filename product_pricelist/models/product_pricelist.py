# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductPricelistInherited(models.Model):
    _inherit = "product.pricelist"

    start_date = fields.Datetime(string="Start Date")
    end_date = fields.Datetime(string="End Date")
    partner_id = fields.Many2one("res.partner", string="Customer")
    current_date = fields.Datetime(
        string="Current Date", default=fields.Datetime.now
    )
