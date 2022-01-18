# -*- coding: utf-8 -*-

from random import randint

from odoo import models, fields, api, _


class CarInfo(models.Model):
    _name = 'rental_car.car.info'
    # _inherit = 'mail.thread'
    _description = 'Car Info'

    name = fields.Char(tracking=True)
    model_id = fields.Many2one('car.model', tracking=True)
    year = fields.Integer()
    description = fields.Text(tracking=True, index=True)


class CarModel(models.Model):
    _name = 'car.model'
    _description = 'Car Model'

    name = fields.Char()


# class HistoryRepair(models.Model):
#     _name = 'car.history_repair'
#     _description = 'History Repair'
#
#     lease_date = fields.Date()
#     partner_id = fields.Many2one('res.partner')
#     date_in_garage = fields.Datetime()
#     odometer_start = fields.Integer()
#     odometer_end = fields.Integer()
#     car_id = fields.Many2one('rental_car.car')


# class HistoryRented(models.Model):
#     _name = 'car.history_rented'
#     _description = 'History Rented'
#
#     date_under_repair = fields.Datetime()
#     description = fields.Text(tracking=True, index=True)
#     car_id = fields.Many2one('rental_car.car')
#     odometer = fields.Integer()

class History(models.Model):
    _name = 'car.history'
    _description = 'History'

    car_id = fields.Many2one('rental_car.car')
    lease_date = fields.Date()
    partner_id = fields.Many2one('res.partner')
    date_in_garage = fields.Datetime()
    odometer = fields.Integer()
    odometer_start = fields.Integer()
    odometer_end = fields.Integer()
    date_under_repair = fields.Datetime()
    description = fields.Text(tracking=True, index=True)


class Car(models.Model):
    # _name = 'rental_car.rental_car'
    _name = 'rental_car.car'
    _description = 'Rental Car'

    name = fields.Char(compute='_compute_name', store="True", default='-')
    car_id = fields.Many2one('rental_car.car.info')
    number = fields.Char()
    # model = fields.Many2one('car.model', tracking=True)
    model = fields.Many2one('car.model')
    year = fields.Integer()
    status = fields.Selection([
        ('in_garage', 'In Garage'),
        ('rented', 'Rented'),
        ('under_repair', 'Under Repair'),
        ('unavailable', 'Unavailable'),
    ], default='in_garage', compute='_compute_status',
        store=True, tracking=True)
    lease_date = fields.Date()
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

    def action_rented(self):
        return {
            'name': _('Rented %s') % self.name,
            'view_mode': 'form',
            'res_model': 'library.wizard.rented',
            'type': 'ir.actions.act_window',
            'target': 'new'
        }

    def action_in_garage(self):
        last_history = self.history_ids[-1]
        if last_history:
            last_history.write({
                'date_in_garage': fields.Datetime.now()
            })
        self.write({
            'status': 'in_garage',
            'partner_id': False
        })

    # def action_under_repair(self):
    #     last_history = self.history_ids[-1]
    #     if last_history:
    #         last_history.write({
    #             'date_under_repair': fields.Datetime.now()
    #         })
    #     self.write({
    #         'status': 'under_repair',
    #         'partner_id': False
    #     })

    @api.depends('model', 'number')
    def _compute_name(self):
        for record in self:
            record.name = str(record.model) + " " + str(record.number)

    # @api.onchange('number')
    # def set_caps(self):
    #     val = str(self.number)
    #     self.number = val.upper()
