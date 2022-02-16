from datetime import datetime

from odoo.addons.mrp.tests.common import TestMrpCommon


class MrpTest(TestMrpCommon):

    def setUp(self):
        super(MrpTest, self).setUp()
        self.generate_mo()
        self.Mrpproduction = self.env['mrp.production']
        self.ComponentRequirement = self.env['bluesky_mrp_workorder.component_requirement']
        self.StockMove = self.env['stock.move']
        self.Company = self.env['res.company']
        self.StockLocation = self.env['stock.location']
        self.UoM = self.env['uom.uom']
        self.UoMCategory = self.env['uom.category']

        self.company_1 = self.Company.create({
            'name': 'TestComapny',
            'partner_id': self.partner_1.id,
            'currency_id': self.partner_1.currency_id.id,
            'layout_background': 'Blank'
        })

        self.location_1 = self.StockLocation.create({
            'name': 'TestLocation',
            'usage': 'view',
        })

        self.mo = self.Mrpproduction.create({
            'product_id': self.product_2.id,
            'product_uom_id': self.product_2.uom_id.id,
            'move_raw_ids': [
                (0, 0, {
                    'name': self.product_2.name,
                    'date': datetime.now(),
                    'company_id': self.company_1.id,
                    'product_id': self.product_2.id,
                    'product_uom_qty': self.product_2.mrp_product_qty,
                    'product_uom': self.product_2.uom_id.id,
                    'location_id': self.location_1.id,
                    'location_dest_id': self.location_1.id,
                    'procure_method': 'make_to_stock'}),
            ],
        })

        self.component = self.ComponentRequirement.create({
            'mo_id': self.mo.id,
            'product_id': self.mo.product_id.id,
            'uom_id': self.mo.product_uom_id.id,
            'picked_qty': 18.9,
            'rejected_qty': 3.0,
            'sent_to_client_qty': 0.9
        })

    def test_compute_component_requirements(self):
        self.assertTrue(self.mo)
        self.assertIsNotNone(self.mo.component_requirement_ids)

    def test_compute_variance_qty(self):
        result = self.component.picked_qty - self.component.rejected_qty - self.component.sent_to_client_qty
        self.assertEqual(self.component.variance_qty, result,
                         f'\nMust be -->{result}\nGot -->{self.component.variance_qty}')

    def test_compute_consumed_qty(self):
        new_keys = self.component.mo_id._get_raw_moves_requirements_key()
        raw_moves = new_keys.get((self.component.mo_id, self.component.product_id, self.component.uom_id),
                                 self.StockMove)
        result = sum(raw_moves.mapped('product_uom_qty'))
        self.assertEqual(self.component.consumed_qty, result)

    def test_compute_batch_code_id(self):
        self.assertEqual(self.mo.product_id.tracking, 'none')
        self.assertFalse(self.mo.batch_code_id)
