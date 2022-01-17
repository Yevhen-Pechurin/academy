from odoo import models, fields

class Car(models.Model):
    _name = 'car_rental.car'
    _description = 'Some minimal placeholder description'

    name = fields.Char(required=True)