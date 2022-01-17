# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Odometr(models.Model):
    _name = 'rental_car.odometr'
    _description = 'Odometr'

    name = fields.Char(compute='_name_compute' ,tracking=True)
    disctance = fields.Integer(tracking=True)
    date = fields.Date(tracking=True)
    # car_id = fields.One2many('rental_car', 'odometr_id')

    @api.depends('disctance')
    def _name_compute(self):
        for record in self:
            record.name = f'{record.disctance}'


class History(models.Model):
    _name = 'rental_car.history'
    _description = 'History'

    car_id = fields.Many2one('rental_car.car')
    partner_id = fields.Many2one('res.partner')
    date_to_rent = fields.Datetime(tracking=True)
    date_to_return = fields.Datetime(tracking=True)
    due_date = fields.Datetime(tracking=True)
    odometr_id = fields.Many2one('rental_car.odometr')
    odometr_start = fields.Integer(tracking=True)
    odometr_end = fields.Integer(tracking=True)


class Car(models.Model):
    _name = 'rental_car.car'
    _description = 'Car'
    _inherit = 'mail.thread'

    name = fields.Char(tracking=True, readonly=True, compute='_name_compute')
    number = fields.Char(tracking=True)
    model = fields.Char(tracking=True)
    year_edition = fields.Integer(tracking=True)
    partner_id = fields.Many2one('res.partner')
    history_ids = fields.One2many('rental_car.history', 'car_id')
    odometr_id = fields.Many2one('rental_car.odometr')

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
