# -*- coding: utf-8 -*-

from random import randint

from odoo import models, fields, api, _


class History(models.Model):
    _name = 'car.history'
    _description = 'History'

    car_id = fields.Many2one('rental_car.car')
    partner_id = fields.Many2one('res.partner')
    odometer_start = fields.Integer()
    odometer_end = fields.Integer()
    # date_on_hand = fields.Datetime()
    lease_data = fields.Date()


class Car(models.Model):
    # _name = 'rental_car.rental_car'
    _name = 'rental_car.car'
    _description = 'Rental Car'

    name = fields.Char(compute='_compute_name', store="True", default='-')
    number = fields.Char()
    model = fields.Char()
    year = fields.Integer()
    # status = fields.Selection([
    #     ('in_garage', 'In Garage'),
    #     ('rented', 'Rented'),
    #     ('under_repair', 'Under Repair'),
    #     ('unavailable', 'Unavailable'),
    # ], default='in_garage', compute='_compute_status',
    #     store=True, tracking=True)
    lease_data = fields.Date()
    partner_id = fields.Many2one('res.partner')
    logo_image = fields.Image(string="Image", max_width=256, max_height=256)
    odometer = fields.Integer()
    active = fields.Boolean(default=True)
    history_ids = fields.One2many('car.history', 'car_id')

    @api.depends('active')
    def _compute_status(self):
        for car in self:
            if not car.active:
                car.status = 'rented'
            else:
                car.status = car.status

    @api.depends('model', 'number')
    def _compute_name(self):
        for record in self:
            record.name = str(record.model) + " " + str(record.number)


    # @api.onchange('number')
    # def set_caps(self):
    #     val = str(self.number)
    #     self.number = val.upper()
