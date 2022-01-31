from odoo.tests import tagged
from .common import TestCarCommonBase


@tagged('car')
class TestCar(TestCarCommonBase):

    def test_action_in_garage(self):
        self.assertEqual(self.car_1.status, 'on_loan', 'Status is not on_loan')
        self.assertTrue(self.car_1.partner_id)
        self.car_1.action_in_garage()
        self.assertEqual(self.car_1.status, 'in_garage', 'Status is not in_garage')
        self.assertFalse(self.car_1.partner_id)


