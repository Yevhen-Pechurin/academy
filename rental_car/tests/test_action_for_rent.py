from odoo.tests import Form, tagged
from odoo.addons.mrp.tests.common import TestMrpCommon
from .common import RentalCarTests



@tagged('rental_car')
class TestStatus(RentalCarTests):

    def test_action_for_rent(self):
        self.assertEqual(self.car_1.status, "in_garage", "Incorrect Status")

        context = self.car_1.action_for_rent()
        # self.assertEqual(context["status"], "for_rent", "Incorrect Status")
        expected_res = {
            'name': 'For Rent',
            'view_mode': 'form',
            'res_model': 'rental_car.car.for_rent',
            'type': 'ir.actions.act_window',
            'target': 'new'
        }
        self.assertItemsEqual(context, expected_res)

    # def test_action_in_garage(self):
    #     self.car_2.action_in_garage()
    #     self.assertEqual(self.car_2.status, "for_rent", "Incorrect Status")
    #
    #     context = self.car_2.action_in_garage()
    #     expected_res = {
    #         'name': 'In Garage',
    #         'view_mode': 'form',
    #         'res_model': 'rental_car.car.in_garage',
    #         'type': 'ir.actions.act_window',
    #         'target': 'new'
    #     }
    #     self.assertItemsEqual(context, expected_res)
