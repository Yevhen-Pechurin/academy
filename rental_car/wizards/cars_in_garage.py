from odoo import fields, models, api, _


class CarInGarage(models.TransientModel):
    _name = "rental_car.car.in_garage"
    _description = "Car In Garage"

    odometer_end_value = fields.Integer()


    def action_back_to_garage(self):
        ctx = self.env.context
        car = self.env['rental_car.car'].sudo().search([('id', '=', ctx['active_id'])])
        history = car.rent_history_id[-1]#sudo().search([('id', '=', ctx['active_id'])])
        car.write({
            'client_id': False,
            'status': 'in_garage',
            'odometer_value': self.odometer_end_value,
        })
        if history:
            history.write({
                'date_in_garage': fields.Datetime.now(),
                'odometer_end_value': self.odometer_end_value
            })

