# -*- coding: utf-8 -*-

from random import randint

from odoo import models, fields, api, _


class Car(models.Model):
    # _name = 'rental_car.rental_car'
    _name = 'rental_car.car'
    _description = 'Rental Car'

    name = fields.Char()
    number = fields.Char()
    # model = fields.Many2one()
    year = fields.Integer()
    # status = fields.Selection([
    #     ('in_garage', 'In Garage'),
    #     ('rented', 'Rented'),
    #     ('under_repair', 'Under Repair'),
    #     ('unavailable', 'Unavailable'),
    # ], default='in_garage', compute='_compute_status',
    #     store=True, tracking=True)
    lease_data = fields.Date()
    # partner_id = fields.Many2one('res.partner')
    # history_ids = fields.One2many()
    logo_image = fields.Image(string="Image", max_width=256, max_height=256)
    odometer = fields.Integer()
    active = fields.Boolean(default=True)

    @api.depends('active')
    def _compute_status(self):
        for car in self:
            if not car.active:
                car.status = 'rented'
            else:
                car.status = car.status
