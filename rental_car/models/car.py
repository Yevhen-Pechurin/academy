# -*- coding: utf-8 -*-

from random import randint

from odoo import models, fields, api, _


class Car(models.Model):
    # _name = 'rental_car.rental_car'
    _name = 'rental_car.car'
    _description = 'Rental Car'

    name = fields.Char()
    number = fields.Integer()
    model = fields.Many2one()
    year = fields.Integer()
    status = fields.Selection([
        ('in_garage', 'In Garage'),
        ('rented', 'Rented'),
        ('under_repair', 'Under Repair'),
        ('unavailable', 'Unavailable'),
    ], default='in_garage', compute='_compute_status',
        store=True, tracking=True)

