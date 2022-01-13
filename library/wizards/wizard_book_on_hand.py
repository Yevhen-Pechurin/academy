from odoo import models, fields, api, SUPERUSER_ID
from odoo.exceptions import ValidationError, UserError


class WizardOnHand(models.TransientModel):
    _name = 'library.wizard.on_hand'
    _description = 'Wizard On Hand'

    partner_id = fields.Many2one('res.partner')
    due_date = fields.Date()

    def action_on_hand(self):
        ctx = self._context
        book = self.env[ctx['active_model']].sudo().browse(ctx['active_ids'])
        today = fields.Datetime().now()
        book.write({
            'partner_id': self.partner_id.id,
            'due_date': self.due_date,
            'status': 'on_hand',
            'history_ids': [(0, 0, {
                'book_id': book.id,
                'partner_id': self.partner_id.id,
                'date_on_hand': today,
                'due_date': self.due_date,
            })]
        })

    @api.constrains('due_date')
    def constrain_due_date(self):
        if self.due_date <= fields.Date.today():
            raise ValidationError('Вы не можете выбрать такую дату')
