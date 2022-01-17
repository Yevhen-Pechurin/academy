from odoo import fields, models


class WizardOnHand(models.TransientModel):
    _name = 'library.wizard.on_hand'

    _description = 'Wizard for giving books on hand'

    due_date = fields.Date()
    partner_id = fields.Many2one('res.partner')

    def on_hand(self):
        ctx = self.env.context
        book = self.env['library.book'].sudo().search([('id', '=', ctx['active_id'])])
        book.write({'partner_id': self.partner_id.id, 'status': 'on_hand'})
        self.env['library.history'].sudo().create({
            'due_date': self.due_date,
            'partner_id': self.partner_id.id,
            'book_id': book.id
        })
