from odoo import models, fields


class CarReport(models.Model):
    _name = "rental_car.report"
    _description = "Model"
    _auto = False

    car_id = fields.Many2one("rental_car.car")
    client_id = fields.Many2one("res.partner")
    max_odometer_value = fields.Integer(group_operator="max")
    min_odometer_value = fields.Integer(group_operator="min")
    brand_id = fields.Many2one("rental_car.brand")
    model_id = fields.Many2one("rental_car.model")

    @property
    def _table_query(self):
        return """
            SELECT 
                rental_car_car.id,
                rental_car_car.id car_id,
                COALESCE (odometer_value, 0) max_odometer_value,
                COALESCE (odometer_value, 0) min_odometer_value
                
            FROM rental_car_car
            
        """
