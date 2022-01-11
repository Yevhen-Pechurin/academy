from odoo import models, fields


class WizardOnHand(models.TransientModel):
    _name = 'library.wizard.on_hand'

    partner_id = fields.Many2one('res.partner')
    due_date = fields.Date()

    def action_on_hand(self):
        ctx = self._context
        book = self.env[ctx['active_model']].browse(ctx['active_ids'])
        today = fields.Date().today()
        book.write({
            'partner_id': self.partner_id.id,
            'due_date': self.due_date,
            'state': 'on_hand'
        })
        self.env['library.history'].create({
            'book_id':book.id,
            'partner_id': self.partner_id.id,
            'date_on_hand': today,
            'due_date': self.due_date,
        })
