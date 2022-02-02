from odoo import models, fields

class WizardPassToClient(models.TransientModel):
    _name = 'rental.wizard.pass_to_client'
    _description = 'Wizard Pass to Client'

    rentee_id = fields.Many2one('res.partner', required=True)
    initial_odometer_value = fields.Integer(readonly=True)

    def action_pass_car_to_client(self):
        ctx = self._context
        car = self.env[ctx['active_model']].sudo().browse(ctx['active_ids'])
        date_rented = fields.Datetime().now()
        # self._context.get('mail_create_nolog') and not self._context.get('mail_notrack')
        car.with_context(mail_notrack=True).write({
            'rentee_id': self.rentee_id.id,
            'date_rented': date_rented,
            'status': 'rented',
            'rental_history_ids': [(0, 0, {
                'car_id': car.id,
                'rentee_id': self.rentee_id.id,
                'date_rented': date_rented,
                'initial_odometer_value': self.initial_odometer_value,
            })]
        })
