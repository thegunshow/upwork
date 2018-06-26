# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    "name": "Sale and Purchase Status",
    "version": "1.0",
    "author": "Anil R. Kesariya",
    "category": "Sale and Purchase",
    "summary": "",
    "depends": [
        'sale_management','purchase'
    ],
    'description': """

Sale and Purchase Status
========================

Added status inside sale and purchse based on deliveries and shipments.

        """,
    "demo": [],
    "data": [
        'views/sp_status_view.xml',
    ],
    "installable": True,
    "auto_install": False,
}
