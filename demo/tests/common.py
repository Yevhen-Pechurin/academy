from odoo.addons.base.tests.common import TransactionCase


class TestDemoCommonBase(TransactionCase):

    def setUp(self):
        super(TestDemoCommonBase, self).setUp()
        self.State = self.env['demo.state']
        self.Demo = self.env['demo.demo']
        self.Partner = self.env['res.partner']

        self.partner_1 = self.Partner.create({
            'name': 'Test Partner',
        })

        self.demo_1 = self.Demo.create({
            'name': 'Person00001',
        })

        self.env['ir.sequence'].search([
            ('code', '=', 'demo.demo'),
        ]).write({
            'name_next': 1,
            'padding': 5,
        })

        self.demo_1 = self.Demo.create({
            'name': 'Person00001',
            'demo_id': self.demo_1.id,
            'state': 'scheduled',
            'partner_id': self.partner_1.id
        })
        self.demo_2 = self.Demo.create({
            'name': 'Person00002',
            'demo_id': self.demo_1.id,
            'state': 'done',
            'partner_id': self.partner_1.id
        })

