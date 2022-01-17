from odoo import models, fields, api
from odoo.exceptions import ValidationError

class CarModel(models.Model):
    _name = 'car_rental.car_model'
    _description = 'Car model'
    
    model_name = fields.Char(required=True)
    manufacturer_logo = fields.Image(string="Manufacturer logo", max_width=256, max_height=256)
    car_ids = fields.One2many('car_rental.car', 'model')


class CarRentalHistory(models.Model):
    _name = 'car_rental.car_rental_history'

    car_id = fields.Many2one('car_rental.car', required=True)
    date_rented = fields.Datetime()
    rentee_id = fields.Many2one('res.partner')
    date_returned = fields.Datetime()
    initial_odometer_value = fields.Integer(default=lambda self: self.car_id.odometer)
    final_odometer_value = fields.Integer()

    @api.constrains('final_odometer_value')
    def check_final_odometer_value(self):
        if self.initial_odometer_value > self.final_odometer_value:
            raise ValidationError('Invalid input: odometer value after rental cannot be smaller than before rental.')


class CarMaintananceHistory(models.Model):
    _name = 'car_rental.car_maintanance_history'


class Car(models.Model):
    _name = 'car_rental.car'
    _description = 'A car'
    _inherit = 'mail.thread'

    name = fields.Char(compute='_compute_car_name')
    model_id = fields.Many2one('car_rental.car_model', required=True)
    number = fields.Char(required=True)
    logo = fields.Image(related='model_id.manufacturer_logo')
    year = fields.Integer()
    status = fields.Selection([
        ('in_garage', 'In garage'),
        ('rented', 'Rented'),
        ('on_maintanence', 'On maintanance'),
        ('unavailable', 'Unavailable'),
        ], required=True, tracking=True)
    date_rented = fields.Datetime()
    client_id = fields.Many2one('res.partner', copy=False)
    odometer = fields.Integer(tracking=True)
    active = fields.Boolean(default=True)
    rental_history_ids = fields.One2many('car_rental.car_rental_history', 'car_id')

    _sql_constraints = [
        ('unique_number', 'UNIQUE(number)', """Number is unique for every car!"""),
    ]

    @api.depends('model', 'number')
    def _compute_car_name(self):
        for car in self:
            car.name = f'{car.model.model_name}_{car.number}'

    @api.onchange('status')
    def onchange_status_rented(self):
        if self.status == 'rented':
            if not self.date_rented:
                self.date_rented = fields.Datetime.now()
        else:
            self.date_rented = False

    @api.depends('active')
    def _compute_status(self):
        for car in self:
            if not car.active:
                car.status = 'unavailable'
            else:
                car.status = 'in_garage'
