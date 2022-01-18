from odoo import models, fields, api


class HistoryRepairs(models.Model):
    _name = 'rent_car.history_repairs'
    _description = "History a repaired car"

    car_id = fields.Many2one('rent_car.car')
    date_repair = fields.Date()
    description = fields.Text()
    type_repair = fields.Selection([('t_o', 'T.O'), ('repair', 'Repair')])
    odometer = fields.Integer()