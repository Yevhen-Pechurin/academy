# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Car(models.Model):
    _name = 'rental_car.car'
    _description = 'Car'
    _inherit = 'mail.thread'

    name = fields.Char(tracking=True, readonly=True, compute='_name_compute')
    number = fields.Char()
    model = fields.Char()


    status = fields.Selection([
        ('available', 'Available'),
        ('in_rent', 'In Rent'),
        ("fixing", "Fixing"),
        ("unavailable", "Unavailable"),
    ], default='available')

    @api.depends('number', 'model')
    def _name_compute(self):
        for record in self:
            record.name = f'{record.model} {record.number}'
