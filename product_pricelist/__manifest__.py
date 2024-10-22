# -*- coding: utf-8 -*-

{
    "name": "Product Pricelist",
    "version": "17.0.0.0.1",
    "category": "Product",
    "summary": "Price of Product",
    "description": """
        Product Pricelist
        ========================================
        This module filtered the price of products based on the partners
        """,
    "author": "Aktiv Software",
    "company": "Aktiv Software",
    "website": "https://www.aktivsoftware.com",
    "depends": ["sale", "product"],
    "data": [
        "views/product_pricelist_views.xml",
        "views/sale_order_views.xml",
    ],
    "installable": True,
    "auto_install": False,
    "application": False,
    "license": "LGPL-3",
}
