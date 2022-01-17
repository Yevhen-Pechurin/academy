from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class WizardOnHand(models.TransientModel):
    _name = 'rental.wizard.on_hand'
    _description = 'Wizard On Hand'

    partner_id = fields.Many2one('res.partner')
    date_on_loan = fields.Date()

    def action_on_hand(self):
        ctx = self._context
        car = self.env[ctx['active_model']].sudo().browse(ctx['active_ids'])
        today = fields.Datetime().now()
        car.write({
            'partner_id': self.partner_id.id,
            'date_on_loan': self.date_on_loan,
            'status': 'on_loan',
            'history_ids': [(0, 0, {
                'car_id': car.id,
                'partner_id': self.partner_id.id,
                'date_in_garage': today,
                'date_on_loan': self.date_on_loan,
            })]
        })

    @api.constrains('due_date')
    def constrain_due_date(self):
        if self.due_date <= fields.Date.today():
            raise ValidationError('Вы не можете выбрать такую дату')
