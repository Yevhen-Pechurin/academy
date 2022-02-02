from odoo import models, fields


class CarReport(models.Model):
    _name = 'rental.car.report'
    _description = 'Car Report'
    _auto = False

    car_id = fields.Many2one('rental.car')
    date_on_loan = fields.Date()
    partner_id = fields.Many2one('res.partner')
    max_odometer = fields.Integer(group_operator='max')

    @property
    def _table_query(self):
        return """
            SELECT
                rc.id,
                rc.id car_id,
                rc.date_on_loan date_on_loan,
                client_id,
                COALESCE (odometer, 0) max_odometer
            FROM rental_car rc                
        """

