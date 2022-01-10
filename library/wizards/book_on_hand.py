from odoo import fields, models, api, _


class BookOnHand(models.TransientModel):
    _name = "library.book.on_hand"
    _description = "Book On Hand"

    client_id = fields.Many2one("res.partner")
    due_date = fields.Datetime()

    def action_on_hand(self):
        context = self._context
        book = self.env[context['active_model']].browse(context['active_ids'])
        today = fields.Datetime().now()
        book.write({
            "client_id": self.client_id.id,
            "due_date": self.due_date,
            "status": "on_hand"
        })
        self.env['library.history'].create({
            'book_id': book.id,
            'client_id': self.client_id.id,
            'date_on_hand': today,
            'due_date': self.due_date,
        })


