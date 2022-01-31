from odoo import fields, models


class WizardDemo(models.TransientModel):
    _name = 'demo.wizard.demo'

    _description = 'Wizard for user'

    date = fields.Date()

    def demo(self):
        partner = self.env['res.partner'].sudo().browse(self.env.context['active_ids'])
        res_id = self.env['demo.demo'].create([{
            # 'name': 'Demo for %s' % partner.name,
            'user_id': self.env.user.id,
            'partner_id': partner.id,
            'date': self.date
        }]).id
        action = self.env["ir.actions.actions"]._for_xml_id('demo.all_demo_action')
        action.update({
            'view_mode': 'form',
            'res_id': res_id,
            'views': [(False, 'form')],
        })
        return action
