from odoo import models, fields, api


class HistoryRent(models.Model):
    _name = 'rent_car.history_rent'
    _description = "History a rented car"

    car_id = fields.Many2one('rent_car.car')
    date_rent = fields.Date()
    date_comeback = fields.Date()
    partner_id = fields.Many2one('res.partner')
    st_odometer_value = fields.Integer()
    fn_odometer_value = fields.Integer()

