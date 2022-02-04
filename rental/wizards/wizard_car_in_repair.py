from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class WizardInRepair(models.TransientModel):
    _name = 'rental.wizard.in_repair'
    _description = 'Wizard in Repair'

    description = fields.Char()
    type = fields.Selection([
        ('maintenance', 'Maintenance'),
        ('repair', 'Repair'),
    ])

    def action_in_repair(self):
        ctx = self._context
        car = self.env[ctx['active_model']].sudo().browse(ctx['active_ids'])
        today = fields.Datetime().now()
        car.write({
            'status': 'under_repair',
            'repair_ids': [(0, 0, {
                'car_id': car.id,
                'type': self.type,
                'start_odometer': car.odometer,
                'description': self.description,
                'date_in_repair': today,
            })]
        })

