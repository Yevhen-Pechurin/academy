from odoo.addons.mrp.tests.common import TestMrpCommon


class MrpTest(TestMrpCommon):

    def setUp(self):
        super(MrpTest, self).setUp()
        self.generate_mo()
        self.mo = self.env['mrp.production'].create({
            'product_id': self.product_2.id,
            'product_uom_id': self.product_2.uom_id.id,
        })
        self.env['bluesky_mrp_workorder.component_requirement']

    def test_compute_component_requirements(self):
        self.assertTrue(self.mo)
        self.assertTrue(self.mo.component_requirement_ids)
