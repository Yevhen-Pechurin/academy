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

        self.mo1 = self.Mrpproduction.create({
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
            ]
        })

        self.mo2 = self.Mrpproduction.create({
            'product_id': self.product_2.id,
            'product_uom_id': self.product_2.uom_id.id,
            'amount_of_bulk_manufactured': 12.0,
            'amount_of_bulk_returned': 8.0,
            'total_weight_filled': 20.0,
            'approved_fill_weight': 10.0,
            'bulk_received': 5.0
        })

        self.component = self.ComponentRequirement.create({
            'mo_id': self.mo1.id,
            'product_id': self.mo1.product_id.id,
            'uom_id': self.mo1.product_uom_id.id,
            'picked_qty': 18.9,
            'rejected_qty': 3.0,
            'sent_to_client_qty': 0.9
        })

    def test_compute_component_requirements(self):
        self.assertTrue(self.mo1)
        self.assertIsNotNone(self.mo1.component_requirement_ids)

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

    # def test_compute_batch_code_id(self):
    #     self.assertEqual(self.mo1.product_id.tracking, 'none')
    #     self.assertFalse(self.mo1.batch_code_id)

    def test_compute_bulk_yield_else(self):
        result = (self.mo2.total_weight_filled + self.mo2.amount_of_bulk_returned) * 100 / self.mo2.amount_of_bulk_manufactured
        self.assertEqual(self.mo2.bulk_yield, result, f'result -->{result}\nGOT --> {self.mo2.bulk_yield}')

    def test_compute_projected_yield(self):
        result = self.mo2.bulk_received / (self.mo2.approved_fill_weight or 1.0)
        self.assertEqual(self.mo2.projected_yield, result, f'result -->{result}\nGOT --> {self.mo2.projected_yield}')

