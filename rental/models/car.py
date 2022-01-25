from odoo import models, fields, api
from odoo.exceptions import ValidationError

class CarModel(models.Model):
    _name = 'rental.car_model'
    _description = 'Car model'
    
    model_name = fields.Char(required=True)
    manufacturer_logo = fields.Image(string="Manufacturer logo", max_width=256, max_height=256)
    #car_ids = fields.One2many('rental.car', 'model_id')


class CarRentalHistory(models.Model):
    _name = 'rental.history'
    _description = 'Car rental history'

    car_id = fields.Many2one('rental.car', required=True)
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
    _name = 'rental.maintanance_history'
    _description = 'Car maintanance history'


class Car(models.Model):
    _name = 'rental.car'
    _description = 'A car'
    _inherit = 'mail.thread'

    name = fields.Char(compute='_compute_car_name')
    model = fields.Char(required=True) #model_id = fields.Many2one('rental.car_model', required=True)
    number = fields.Char(required=True)
    logo = fields.Image()    #related='model_id.manufacturer_logo')
    year = fields.Integer()
    status = fields.Selection([
        ('in_garage', 'In garage'),
        ('rented', 'Rented'),
        ('on_maintanence', 'On maintanance'),
        ('unavailable', 'Unavailable'),
        ], default= 'in_garage', required=True, tracking=True)
    date_rented = fields.Datetime()
    client_id = fields.Many2one('res.partner', copy=False)
    odometer = fields.Integer(tracking=True)
    active = fields.Boolean(default=True)
    rental_history_ids = fields.One2many('rental.history', 'car_id')

    _sql_constraints = [
        ('unique_number', 'UNIQUE(number)', """Number is unique for every car!"""),
    ]

    @api.model
    def get_model(self, model_name):
        #Some ways of managing the data:
        """values = {'models': self.env['rental.car_model'].sudo().search([('model_name', 'ilike', model_name)]).read(['id', 'model_name'])}
        """
        """values = {'models': self.env['rental.car'].sudo().search_read([('model_name', 'ilike', model_name)], fields = ['model_name', 'id'], limit=5)}
        """
        """records = self.env['rental.car_model'].sudo().search([('model_name', 'ilike', model_name)])
        #values['models'] = [[r.id, r.model_name] for r in records]
        """
        return self.env['rental.car_model'].sudo().search([('model_name', 'ilike', model_name)]).read(['id', 'model_name'])

    @api.depends('model', 'number')
    def _compute_car_name(self):
        for car in self:
            car.name = f'{car.model}_{car.number}'

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
