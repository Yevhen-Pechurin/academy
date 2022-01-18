# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Car(models.Model):
    _name = 'rent_car.car'
    _description = 'Info Car'
    _inherit = ['mail.thread']

    name = fields.Char(compute='_create_name', store=True, readonly=True)
    number = fields.Char()
    model = fields.Char()
    year = fields.Integer()
    status = fields.Selection([('in_garage', 'In Garage'), ('in_rent', 'In Rent'), ('on_repair', 'On Repair'), ('unavailable', 'Unavailable'), ], default='in_garage', tracking=True)
    date_rent = fields.Date()
    partner_id = fields.Many2one('res.partner')
    description = fields.Text()
    history_rent_ids = fields.One2many('rent_car.history_rent', 'car_id')
    history_repair_ids = fields.One2many('rent_car.history_repairs', 'car_id')
    logo = fields.Image(max_width=256, max_height=256)
    odometer = fields.Integer()

    _sql_constraints = [('number_uniq', 'unique (number)', "Only one number can be defined for each books!")]

    @api.depends('number', 'model')
    def _create_name(self):
        for s in self:
            s.name = str(s.model) + str(s.number)


#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
