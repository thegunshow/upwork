# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class SaleOrder(models.Model):

    _inherit = "sale.order"

    @api.depends('picking_ids.state')
    def check_status(self):
        """
         Check all deliveries are done or not.If all deliveries done return done else open.
        :return: status done or open.
        """
        for order in self:
            done = 0
            if order.picking_ids:
                for picking in order.picking_ids:
                    if picking.state == 'done':
                        done += 1
                if done == order.delivery_count:
                    order.status = 'done'
                else:
                    order.status = 'open'
            else:
                order.status = 'open'

    status = fields.Selection([
        ('done', 'Done'),
        ('open', 'Open'),
    ], compute='check_status', string='DO Status', store=True, default='open')

class PurchaseOrder(models.Model):

    _inherit = "purchase.order"

    @api.depends('picking_ids.state')
    def check_status(self):
        """
         Check all shipments are done or not.If all shipments done return done else open.
        :return: status done or open.
        """
        for order in self:
            done = 0
            if order.picking_ids:
                for picking in order.picking_ids:
                    if picking.state == 'done':
                        done += 1
                if done == order.picking_count:
                    order.status = 'done'
                else:
                    order.status = 'open'
            else:
                order.status = 'open'


    status = fields.Selection([
        ('done', 'Done'),
        ('open', 'Open'),
    ], compute='check_status', string='DO Status', store=True, default='open')
