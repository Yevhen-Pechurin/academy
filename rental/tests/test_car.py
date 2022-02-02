from .common import RentalTestCar
from odoo.tests import tagged, Form
from odoo import _


@tagged('car')
class StartTest(RentalTestCar):
    def test_default_values_car(self):
        self.assertEqual(self.test_car.status, 'in_garage')
        self.assertEqual(self.test_car.active, True)

    def test_compute_car(self):
        self.assertEqual(self.test_car.name, self.test_car.model + str(self.test_car.number))

    def test_sequence_car(self):
        self.assertEqual(self.test_car.code, 'Car00007')

    def test_statuses(self):
        self.test_car.action_unavailable()
        self.assertEqual(self.test_car.status, 'unavailable')
        self.test_car.action_repair()
        self.assertEqual(self.test_car.status, 'under_repair')
        self.test_car.action_garage()
        self.assertEqual(self.test_car.status, 'in_garage')
        self.assertEqual(self.test_car.repair_history_ids[-1].end, True)

    def test_get_cars(self):
        self.assertEqual(self.test_car.get_cars('Test', 'model'), [{'id': self.test_car_id, 'key': 'Test'}])
        self.assertEqual(self.test_car.get_cars('TestError', 'model'), [])

    def test_on_loan(self):
        result = self.test_car.action_loan()
        expected = {
            'name': _('On Loan'),
            'res_model': 'rental.wizard.loan',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'target': 'new',

        }
        self.assertEqual(result, expected)
        wizard = Form(self.env['rental.wizard.loan'].with_context({'active_id': self.test_car.id}))
        wizard.partner_id = self.test_partner
        action = wizard.save()
        action.on_loan()

        self.assertEqual(self.test_car.status, 'on_loan')
