# -*- coding: utf-8 -*-

from random import randint

from odoo import models, fields, api, _


class CarModel(models.Model):
    _name = 'car.model'
    _description = 'Car Model'

    name = fields.Char()


class CarInfo(models.Model):
    _name = 'rental_car.car.info'
    _inherit = 'mail.thread'
    _description = 'Car Info'

    name = fields.Char(tracking=True)
    model_id = fields.Many2one('car.model', tracking=True)
    year = fields.Integer(tracking=True)
    odometer = fields.Integer()
    description = fields.Text(tracking=True)


class History(models.Model):
    _name = 'car.history'
    _description = 'History'

    car_id = fields.Many2one('rental_car.car')
    partner_id = fields.Many2one('res.partner')
    lease_date = fields.Date()
    date_in_garage = fields.Datetime()
    # date_under_repair = fields.Datetime()
    # odometer = fields.Integer()
    odometer_start = fields.Integer()
    odometer_end = fields.Integer()
    # description = fields.Text(tracking=True, index=True)


class Car(models.Model):
    _name = 'rental_car.car'
    _inherit = 'mail.thread'
    _description = 'Rental Car'

    name = fields.Char()
    number = fields.Char()
    model_id = fields.Char()
    name_order = fields.Char(compute='_compute_name_order', store="True", default='-')
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
    history_ids = fields.One2many('car.history', 'car_id')
    logo_image = fields.Image(string="Image", max_width=256, max_height=256)
    odometer = fields.Integer()
    active = fields.Boolean(default=True)
    description = fields.Text()

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
            'res_model': 'rental_car.wizard.rented',
            'type': 'ir.actions.act_window',
            'target': 'new'
        }

    def action_under_repair(self):
        return {
            'name': _('Under Repair %s') % self.name,
            'view_mode': 'form',
            'res_model': 'rental_car.wizard.under_repair',
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

    @api.depends('model_id', 'number')
    def _compute_name_order(self):
        for record in self:
            record.name_order = str(record.model_id) + " " + str(record.number)

    # @api.onchange('number')
    # def set_caps(self):
    #     val = str(self.number)
    #     self.number = val.upper()
