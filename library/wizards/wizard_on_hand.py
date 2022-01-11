from odoo import models, fields, http


class WizardOnHand(models.TransientModel):
    _name = 'library.wizard.on_hand'
    _description = 'Wizard for giving books on hand'
    partner_id = fields.Many2one('res.partner')
    due_date = fields.Date()

    def action_on_hand(self):
        ctx=self._context
        book=self.env[ctx['active_model']].browse(ctx['active_id'])
     
        book.write({
            'status':'are_used',
            'partner_id':self.partner_id.id
        })
        self.env['library.history'].create(
            {
                'partner_id':self.partner_id.id,
                'due_date':self.due_date,
                'books_id':book.id
            }
        )