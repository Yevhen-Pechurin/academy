from odoo.exceptions import ValidationError
from odoo.tests import tagged, Form, HttpCase
from .common import TestBookCommonBase
from psycopg2.errors import UniqueViolation
from odoo import fields
from datetime import timedelta


@tagged('book')
class TestBook(TestBookCommonBase):

    def test_01_action_on_shelf(self):
        self.assertEqual(self.book_1.status, 'on_hand', 'Status is not on_hand')
        self.assertTrue(self.book_1.partner_id)
        self.book_1.action_on_shelf()
        self.assertEqual(self.book_1.status, 'on_shelf', 'Status is not on_hand')
        self.assertFalse(self.book_1.partner_id)

    def test_02_name_constrain(self):
        with self.assertRaises(UniqueViolation):
            self.Book.create({
                'number': self.book_1.number
            })

    def test_03_action_on_hand(self):
        self.assertEqual(self.book_2.status, 'on_shelf', 'Status is not on_shelf')
        result = self.book_2.action_on_hand()
        expected_result = {
            'name': 'On Hand %s' % self.book_2.name,
            'view_mode': 'form',
            'res_model': 'library.wizard.on_hand',
            'type': 'ir.actions.act_window',
            'target': 'new',
            'context': {
                'additional_data': 'Data',
                'default_due_date': fields.Datetime.now() + timedelta(days=10)
            }
        }
        self.assertItemsEqual(expected_result, result)
        form_data = self.env['library.wizard.on_hand'].with_context(**result['context'], active_model='library.book', active_ids=self.book_2.ids)
        form_on_hand = Form(form_data)
        form_on_hand.partner_id = self.partner_1
        with self.assertRaises(ValidationError):
            form_on_hand.due_date = fields.Datetime.now() - timedelta(days=1)
            form_on_hand.save()
        form_on_hand.due_date = fields.Datetime.now() + timedelta(days=10)
        wizard = form_on_hand.save()
        wizard.action_on_hand()
        self.assertEqual(self.book_2.status, 'on_hand', 'Status is not on_hand')

    def test_04_sequence(self):
        self.assertEqual(self.book_1.number, 'Book000001')
        self.assertEqual(self.book_2.number, 'Book000002')


@tagged('book')
class TestBookJs(HttpCase):

    def test_tour(self):
        self.start_tour("/web", 'library_tour', login='admin', timeout=180)
