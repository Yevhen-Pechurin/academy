# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Model(models.Model):
    _name = 'rental.model'
    _description = 'Model of car'

    name = fields.Char()


class Country(models.Model):
    _name = 'rental.country'
    _description = 'Country of origin'

    name = fields.Char()


class History(models.Model):
    _name = 'rental.history'
    _description = 'History'

    car_id = fields.Many2one('rental.car')
    partner_id = fields.Many2one('res.partner')
    date_on_rent = fields.Date()
    date_in_garage = fields.Date()
    due_date = fields.Date()


class CarInfo(models.Model):
    _name = 'rental.car.info'
    _inherit = 'mail.thread'
    _description = 'Car Info'

    name = fields.Char(tracking=True)
    model_id = fields.Many2one('rental.model', tracking=True)
    country_id = fields.Many2one('rental.country', tracking=True)
    description = fields.Text(tracking=True)


class Car(models.Model):
    _name = 'rental.car'
    _inherit = 'mail.thread'
    _description = 'Car'

    car_id = fields.Many2one('rental.car.info')
    name = fields.Char(related='car_id.name', readonly=False)
    number = fields.Char(copy=False)
    model_id = fields.Many2one(related='car_id.model_id')
    year = fields.Integer()
    mileage = fields.Integer()
    country_id = fields.Many2one(related='car_id.country_id')
    status = fields.Selection([
        ('in_garage', 'In Garage'),
        ('on_rent', 'On Rent'),
        ('unavailable', 'Unavailable'),
    ], default='in_garage', compute='_compute_status', store=True, tracking=True)
    partner_id = fields.Many2one('res.partner')
    history_ids = fields.One2many('rental.history', 'car_id')
    image = fields.Image(string="Image", max_width=256, max_height=256, help="Select image here", verify_resolution=True)
    description = fields.Text(related='car_id.description')
    due_date = fields.Date()
    overdue_notification_date = fields.Date()
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ('number_unig', 'unique (number)', """Only one number can be defined for each car!""")
    ]

    def action_on_rent(self):
        return {
            'name': _('On Rent %s') % self.name,
            'view_mode': 'form',
            'res_model': 'rental.wizard.on_rent',
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
            'status': 'on_rent',
            'partner_id': False
        })

    @api.depends('active')
    def _compute_status(self):
        for car in self:
            if not car.active:
                car.status = 'unavailable'
            else:
                car.status = car.status

