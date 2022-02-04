from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class WizardInGarage(models.TransientModel):
    _name = 'rental.wizard.in_garage'
    _description = 'Wizard In Garage'

    finish_odometer = fields.Integer()

    def action_in_garage(self):
        ctx = self._context
        car = self.env[ctx['active_model']].sudo().browse(ctx['active_ids'])
        today = fields.Datetime().now()
        if car.history_ids:
            last_history = car.history_ids[-1]
            last_history.write({
                'date_in_garage': today,
                'finish_odometer': self.finish_odometer
            })
        car.sudo().write({
            'status': 'in_garage',
            'client_id': False,
            'odometer': self.finish_odometer
        })

    @api.constrains('finish_odometer')
    def constrain_due_date(self):
        ctx = self._context
        car = self.env[ctx['active_model']].sudo().browse(ctx['active_ids'])
        start_odometer = car.odometer
        if self.finish_odometer <= start_odometer:
            raise ValidationError('Вы не можете выбрать такое число')
