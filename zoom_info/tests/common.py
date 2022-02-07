from odoo.addons.base.tests.common import TransactionCase


class TestZoomInfoCommonBase(TransactionCase):


    def setUp(self):
        super(TestZoomInfoCommonBase, self).setUp()
        self.partner_1 = self.env['res.partner'].create({
            'name': "Test Partner"
        })
