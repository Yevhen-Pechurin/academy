from odoo import models, fields, api

class CarModel(models.Model):
    _name = 'car_rental.car_model'
    _description = 'Car model'
    
    model_name = fields.Char(required=True)
    car_ids = fields.One2many('car_rental.car', 'model')

class CarRentalHistory(models.Model):
    _name = 'car_rental.car_rental_history'

class CarMaintananceHistory(models.Model):
    _name = 'car_rental.car_maintanance_history'

class Car(models.Model):
    _name = 'car_rental.car'
    _description = 'Some minimal placeholder description'

    name = fields.Char(compute='_compute_car_name')
    model = fields.Many2one('car_rental.car_model', required=True)
    number = fields.Char(required=True)
    year = fields.Integer()
    status = fields.Selection([
        ('in_garage', 'In garage'),
        ('rented', 'Rented'),
        ('on_maintanence', 'On maintanance'),
        ('unavailable', 'Unavailable'),
        ])
    date_rented = fields.Datetime()
    client_id = fields.Many2one('res.partner', copy=False)
    odometer = fields.Integer()

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