from odoo.exceptions import ValidationError
from odoo.tests import tagged, Form, HttpCase
# from odoo.tools import mute_logger
from .common import TestZoomInfoCommonBase
# from psycopg2.errors import UniqueViolation
# from odoo import fields
# from datetime import timedelta

import odoo.tests


@odoo.tests.tagged('post_install', '-at_install')
class TestUi(odoo.tests.HttpCase):

    def test_01_zoom_info_tour(self):
        self.start_tour("/web#action=contacts.action_contacts&view_type=tree", 'zoom_info_tour', login="admin")





# @tagged('zoom_info')
# class TestZoomInfoJs(HttpCase):
#
#     def test_tour(self):
#         self.start_tour("/web", 'zoom_info_tour', login='admin', timeout=180)
