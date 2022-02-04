from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class WizardFromRepair(models.TransientModel):
    _name = 'rental.wizard.from_repair'
    _description = 'Wizard From Repair'

    finish_odometer = fields.Integer()

    def action_from_repair(self):
        ctx = self._context
        car = self.env[ctx['active_model']].sudo().browse(ctx['active_ids'])
        today = fields.Datetime().now()
        if car.repair_ids:
            last_repair = car.repair_ids[-1]
            last_repair.write({
                'date_from_repair': today,
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
