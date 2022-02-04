from odoo import fields, models, api, _


class NewDemo(models.TransientModel):
    _name = "demo.demo.create"
    _description = "Create new demo for partner"

    date = fields.Date()

    def action_create(self):
        partner = self.env['res.partner'].sudo().browse(self.env.context['active_ids'])
        demo = self.env['demo.demo']
        new_demo = demo.create({
            "partner_id": partner.id,
            "user_id": self.env.user.id,
            "date": self.date,
            "status_id":2
        })
        return {
            "res_model": "demo.demo",
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_id": new_demo.id,
        }



