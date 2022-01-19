from odoo import fields, models, api, _


class CarUnderRepair(models.TransientModel):
    _name = "rental_car.car.under_repair"
    _description = "Car Under Repair"

    repair_description = fields.Char()

    def action_under_repair(self):
        ctx = self.env.context
        car = self.env['rental_car.car'].sudo().search([('id', '=', ctx['active_id'])])
        history = self.env['rental_car.repair_history']
        car.write({
            'status': 'under_repair'

        })
        history.create({
            'car_id': car.id,
            'start_date': fields.Datetime.now(),
            'repair_description': self.repair_description
        })
