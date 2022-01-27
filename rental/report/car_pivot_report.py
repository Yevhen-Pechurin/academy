from odoo import fields, models, api


class CarReport(models.Model):
    _name = 'rental.car_report'
    _description = 'Class for car`s report'
    _auto = False

    partner_id = fields.Many2one('res.partner')
    avg_odometr = fields.Integer(group_operator='avg')
    max_odometr = fields.Integer(group_operator='max')
    min_odometr = fields.Integer(group_operator='min')
    all_odometr = fields.Integer(group_operator='sum')

    @property
    def _table_query(self):
        return """
        SELECT
        rental_car.id,
        rental_car.partner_id,
        COALESCE(rental_car.odometer,0) max_odometr,
        COALESCE(rental_car.odometer,0) min_odometr,
        COALESCE(rental_car.odometer,0) all_odometr,
        COALESCE(rental_car.odometer,0) avg_odometr
        FROM rental_car"""
