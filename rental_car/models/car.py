# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.odoo.exceptions import ValidationError


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
    # due_date = fields.Datetime(tracking=True)
    # odometr = fields.Char(related='rental_car.car')
    odometr_start = fields.Integer(tracking=True)
    odometr_end = fields.Integer(tracking=True)
    odometr = fields.Integer()



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
    odometr = fields.Integer()
    logo = fields.Image(string='image', max_width=256, max_height=256)
    active = fields.Boolean(default=True)
    status = fields.Selection([
        ('available', 'Available'),
        ('in_rent', 'In Rent'),
        ("fixing", "Fixing"),
        ("unavailable", "Unavailable"),
    ], default='available', compute="_compute_status")

    @api.depends('number', 'model')
    def _name_compute(self):
        for record in self:
            record.name = f'{record.model} {record.number}'
            # record.name = ().join(record.model ?? "" and record.number or "")

    def action_in_garage(self):
        # last_history = self.history_ids[-1]
        # # car = self.
        # if last_history:
        #     last_history.write({
        #         "date_to_return": fields.Datetime.now(),
        #         # "partner_id": False
        #     })
        return {
            "name": "In Garage %s" % self.name,
            'view_mode': "form",
            'res_model': "rental_car.wizard.in_garage",
            'type': 'ir.actions.act_window',
            'target': "new",
            }

    def action_to_rent(self):
        return {
            "name": "To Rent %s" % self.name,
            'view_mode': "form",
            'res_model': "rental_car.wizard.to_rent",
            'type': 'ir.actions.act_window',
            'target': "new",
            }
    def _cron_overdude(self):
        cars = self.env['rental_car.car'].search([
            ('status', '=', 'in_rent'),
            ('odometr', '<', 400),
        ])

        for car in cars:
            body = 'text here %s, %s' % (car.partner_id.name, car.name)
            car.message_post(body=body)

    # @api.constrains("odometr")
    # def constrain_partner_id(self):
    #     if self.odometr < self.odometr:
    #         raise ValidationError("Неверный пробег")

    api.depends("active")
    def _compute_status(self):
        for car in self:
            if not car.active:
                car.status = 'unavailable'
            else:
                car.status = 'available'

