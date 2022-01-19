from odoo import fields, models, api, _


class CarForRent(models.TransientModel):
    _name = "rental_car.car.for_rent"
    _description = "Car For Rent"

    client_id = fields.Many2one("res.partner")
    due_date = fields.Datetime()

    def action_for_rent(self):
        context = self._context
        car = self.env[context['active_model']].browse(context['active_ids'])
        time_now = fields.Datetime().now()
        car.write({
            "client_id": self.client_id.id,
            "due_date": self.due_date,
            "status": "for_rent"
        })
        self.env['rental_car.history'].create({
            'car_id': car.id,
            'client_id': self.client_id.id,
            'date_for_rent': time_now,
            'odometer_start_value': car.odometer_value,
            'due_date': self.due_date,
        })


