from datetime import timedelta

from odoo.exceptions import ValidationError
from odoo.tests import tagged, Form, HttpCase
from .common import TestCarCommonBase
from odoo import fields


@tagged('car')
class TestCar(TestCarCommonBase):

    def test_action_in_garage(self):
        self.assertEqual(self.car_1.status, 'on_loan', 'Status is not on_loan')
        self.assertTrue(self.car_1.client_id)
        self.car_1.action_in_garage()
        self.assertEqual(self.car_1.status, 'in_garage', 'Status is not in_garage')
        self.assertFalse(self.car_1.client_id)

    def test_01_sequence(self):
        self.assertEqual(self.car_1.number, 'Car000001')
        self.assertEqual(self.car_2.number, 'Car000002')

    def test_action_on_loan(self):
        self.assertEqual(self.car_2.status, 'in_garage', 'Status is not in_garage')
        result = self.car_2.action_on_loan()
        expected_result = {
            'name': 'On Loan %s' % self.car_2.name,
            'view_mode': 'form',
            'res_model': 'rental.wizard.on_loan',
            'type': 'ir.actions.act_window',
            'target': 'new',
            'context': {
                'additional_data': 'Data',
                'default_date_on_loan': fields.Datetime.now() + timedelta(days=10)
            }
        }
        self.assertItemsEqual(expected_result, result)
        form_data = self.env['rental.wizard.on_loan'].with_context(**result['context'], active_model='rental.car', active_ids=self.car_2.ids)
        form_on_loan = Form(form_data)
        form_on_loan.client_id = self.partner_1
        with self.assertRaises(ValidationError):
            form_on_loan.date_on_loan = fields.Datetime.now() - timedelta(days=1)
            form_on_loan.save()
        form_on_loan.date_on_loan = fields.Datetime.now() + timedelta(days=10)
        wizard = form_on_loan.save()
        wizard.action_on_loan()
        self.assertEqual(self.car_2.status, 'on_loan', 'Status is not on_loan')


@tagged('post_install', 'car')
class TestCarJs(HttpCase):

    def test_tour(self):
        self.start_tour("/web", 'rental_tour', login='admin', timeout=180)
