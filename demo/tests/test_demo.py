from odoo.exceptions import ValidationError
from odoo.tests import tagged, Form, HttpCase
from odoo.tools import mute_logger
from .common import TestDemoCommonBase
from psycopg2.errors import UniqueViolation
from odoo import fields
from datetime import timedelta


@tagged('demo')
class TestDemo(TestDemoCommonBase):


    def test_01_name_constrain(self):
        with self.assertRaises(UniqueViolation), mute_logger('odoo.sql_db'):
            self.Demo.create({
                'name': self.book_1.name
            })

    def test_02_sequence(self):
        self.assertEqual(self.book_1.name, 'Person000001')
        self.assertEqual(self.book_2.name, 'Person000002')



@tagged('demo')
class TestDemoJs(HttpCase):

    def test_tour(self):
        self.start_tour("/web", 'demo_tour', login='admin', timeout=180)
