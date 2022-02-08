from datetime import timedelta

from odoo.exceptions import ValidationError
from odoo.tests import tagged, Form, HttpCase
from .common import TestZoomInfoCommonBase
from odoo import fields


@tagged('-at_install', 'post_install', 'zoom_info')
class TestZoomJs(HttpCase):

    def test_tour(self):
        self.start_tour("/web", 'zoom_info_tour', login='admin', timeout=180)


# @tagged('zoom_info')
# class TestZoomInfo(TestZoomInfoCommonBase):
#
#     def test_creation(self):
#         ctx = self._context
#         zoom_info = self.env[ctx['active_model']].sudo().browse(ctx['active_ids'])
