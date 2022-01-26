# -*- coding: utf-8 -*-
from random import randint

from odoo import models, fields, api, _


class History(models.Model):
    _name = 'rental.history'
    _description = 'History'

    car_id = fields.Many2one('rental.car')
    partner_id = fields.Many2one('res.partner')
    start_odometer = fields.Integer()
    finish_odometer = fields.Integer()
    date_in_garage = fields.Datetime()
    date_on_loan = fields.Datetime()



class Car(models.Model):
    _name = 'rental.car'
    _inherit = 'mail.thread'
    _description = 'Car'

    name = fields.Char(compute='_compute_car_name')
    number = fields.Char(copy=False, readonly=True, default='New')
    model = fields.Char(tracking=True, required=True)
    year = fields.Integer(tracking=True, required=True)
    status = fields.Selection([
        ('in_garage', 'In Garage'),
        ('on_loan', 'On Loan'),
        ('under_repair', 'Under Repair'),
        ('unavailable', 'Unavailable'),
    ], default='in_garage', compute='_compute_status',
        store=True, tracking=True)
    rental_start_date = fields.Date()
    partner_id = fields.Many2one('res.partner')
    history_ids = fields.One2many('rental.history', 'car_id')
    image = fields.Image(string="Image", max_width=256, max_height=256)
    active = fields.Boolean(default=True)
    odometer = fields.Integer()
    date_on_loan = fields.Date()
    _sql_constraints = [
        ('number_uniq', 'unique (number)', """Only one number can be defined for each car!"""),
    ]

    def action_on_hand(self):
        pass
        return {
            'name': _('On Hand %s') % self.name,
            'view_mode': 'form',
            'res_model': 'rental.wizard.on_hand',
            'type': 'ir.actions.act_window',
            'target': 'new'
        }

    @api.depends('model', 'number')
    def _compute_car_name(self):
        for car in self:
            car.name = f'{car.model}{car.number}'

    def action_on_shelf(self):
        last_history = self.history_ids[-1]
        if last_history:
            last_history.write({
                'date_in_garage': fields.Datetime.now()
            })
        self.sudo().write({
            'status': 'in_garage',
            'partner_id': False
        })

    @api.depends('active')
    def _compute_status(self):
        for car in self:
            if not car.active:
                car.status = 'unavailable'
            else:
                car.status = 'in_garage'

    @api.model
    def get_model(self, query):
        values = {
            'model_list': self.env['rental.car'].sudo().search_read([('model', 'ilike', query)], fields = ['model', 'id'], limit=5)
        }
        return values

    @api.model
    def create(self, vals):
        if vals.get('number', _('New')) == _('New'):
            vals['number'] = self.env['ir.sequence'].next_by_code('rental.car') or _('New')
            return super(Car, self).create(vals)

