# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Car(models.Model):
    _name = 'rental_car.car'
    _description = 'Car'
    _inherit = 'mail.thread'

    name = fields.Char(tracking=True)
    number = fields.Char()
    model = fields.Char()

    status = fields.Selection([
        ('available', 'Available'),
        ('in_rent', 'In Rent'),
        ("fixing", "Fixing"),
        ("unavailable", "Unavailable"),
    ], default='available')

