from datetime import timedelta
from odoo import fields
from odoo.tests import tagged
from odoo.tests.common import Form, HttpCase
from .common import TestCarCommonBase
from psycopg2.errors import UniqueViolation
from odoo.tools import mute_logger
import unittest
from odoo.exceptions import ValidationError


@tagged('car')
class TestCar(TestCarCommonBase):

    # @unittest.skip("demonstrating skipping")      # skipping test
    def test_01_action_in_garage(self):
        self.assertEqual(self.car_1.status, 'on_rent', 'Status is not on_rent')
        self.assertTrue(self.car_1.partner_id)
        self.car_1.action_in_garage()
        self.assertEqual(self.car_1.status, 'in_garage', 'Status is not on_rent')
        self.assertFalse(self.car_1.partner_id)


    def test_02_action_in_garage(self):
        with self.assertRaises(UniqueViolation), mute_logger('odoo.sql_db'):
            self.Car.create({
                'number': self.car_1.number
            })


    # def test_03_action_on_hand(self):
    #     self.assertEqual(self.book_2.status, 'on_shelf', 'Status is not on_shelf')
    #     result = self.book_2.action_on_hand()
    #     expected_result = {
    #         'name': 'On Hand %s' % self.book_2.name,
    #         'view_mode': 'form',
    #         'res_model': 'library.wizard.on_hand',
    #         'type': 'ir.actions.act_window',
    #         'target': 'new',
    #         'context': {
    #             'additional_data': 'Data',
    #             'default_due_date': fields.Datetime.now() + timedelta(days=10)
    #         }
    #     }
    #     self.assertItemsEqual(expected_result, result)
    #     form_data = self.env['library.wizard.on_hand'].with_context(**result['context'], active_model='library.book', active_ids=self.book_2.ids)
    #     form_on_hand = Form(form_data)
    #     form_on_hand.partner_id = self.partner_1
    #     # with self.assertRaises(ValidationError):           # test constrain date
    #     #     form_on_hand.due_date = fields.Datetime.now() - timedelta(days=1)
    #     #     form_on_hand.save()
    #     # form_on_hand.due_date = fields.Datetime.now() + timedelta(days=10)   # end
    #     wizard = form_on_hand.save()
    #     wizard.action_on_hand()
    #     self.assertEqual(self.book_2.status, 'on_hand', 'Status is not on_hand')
    #
    #
    # def test_004_action_on_hand(self):       # 004 - helps to be the first
    #     self.assertEqual(self.book_1.number, 'Book000001')
    #     self.assertEqual(self.book_2.number, 'Book000002')


@tagged('car')
class TestCarJs(HttpCase):

    def test_tour(self):
        self.start_tour("/web", 'rental_tour', login='admin', timeout=180)