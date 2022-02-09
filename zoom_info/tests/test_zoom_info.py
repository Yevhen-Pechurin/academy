from datetime import timedelta

from odoo.exceptions import ValidationError
from odoo.tests import tagged, Form, HttpCase
from odoo import fields
from odoo.addons.zoom_info.models.zoom_info import ZoomInfo


def _zoom_info_request(self, url, params=None):
    response = dict()
    if url == "/search/company":
        response = {'maxResults': 1110, 'totalResults': 25, 'currentPage': 1,
                    'data': [{'id': 104333869, 'name': 'Tesla'},
                             {'id': 460341917, 'name': 'BELGRADE AIRPORT d.o.o'},
                             {'id': 118473316, 'name': 'Tesla Exploration'},
                             {'id': 430439652, 'name': 'Tesla-TAN'},
                             {'id': 112033901, 'name': 'TESLA ENGINEERING'},
                             {'id': 127435456, 'name': 'MicroTesla'},
                             {'id': 368769862, 'name': 'TESLA Electric'},
                             {'id': 372554166, 'name': 'Tesla a.s'}, {'id': 431554339, 'name': 'Tesla SRL'},
                             {'id': 459522004, 'name': 'Tesla'}, {'id': 372615736, 'name': 'teslauia.com'},
                             {'id': 359519634, 'name': 'Tesla Energy Services'},
                             {'id': 382363370, 'name': 'Tesla Electric'},
                             {'id': 60588176, 'name': 'Tesla Power'},
                             {'id': 68567269, 'name': 'Tesla Offshore'},
                             {'id': 358654803, 'name': 'Coil Innovation GmbH'},
                             {'id': 49596315, 'name': 'Everson Tesla'},
                             {'id': 458930442, 'name': 'TESLA CARGO SOLUTIONS'},
                             {'id': 370222239, 'name': 'Tesla Outsourcing Services Canada'},
                             {'id': 532572028, 'name': 'Tesla Engenharia Elétrica'},
                             {'id': 372624875, 'name': 'Tesla Technologies & Software'},
                             {'id': 407004731, 'name': 'Nikola Tesla Educational Corporation'},
                             {'id': 455952800, 'name': 'ecar-rent'},
                             {'id': 373839676, 'name': 'Tesla InfoTech'},
                             {'id': 346396693, 'name': 'Tesla Transformers'}]}
    if url == "/enrich/company":
        response = {'success': True, 'data': {'outputFields': [
            ['name', 'street', 'city', 'state', 'zipcode', 'country', 'phone', 'website', 'logo', 'id']],
            'result': [{'input': {'companyid': '104333869'}, 'data': [
                {'name': 'Tesla', 'street': '13101 Harold Green Road',
                 'city': 'Austin', 'state': 'Texas', 'zipCode': '78725',
                 'country': 'United States', 'phone': '(650) 681-5000',
                 'website': 'www.tesla.com',
                 'logo': 'https://res.cloudinary.com/zoominfo-com/image/upload/w_100,h_100,c_fit/tesla.com',
                 'id': 104333869}], 'matchStatus': 'FULL_MATCH'}]}}
    return response['data']


@tagged('-at_install', 'post_install', 'zoom_info')
class TestZoomJs(HttpCase):
    def setUp(self):
        super(TestZoomJs, self).setUp()
        self.patch(ZoomInfo, 'zoom_info_request', _zoom_info_request)

    def test_tour(self):
        self.start_tour("/web", 'zoom_info_tour', login='admin', timeout=180)
        partner = self.env['res.partner'].search([('name', '=', 'Tesla')], limit=1)
        self.assertItemsEqual(partner.name, 'Tesla')
        self.assertItemsEqual(partner.street, '13101 Harold Green Road')
        self.assertItemsEqual(partner.city, 'Austin')
        self.assertItemsEqual(partner.state_id.name, 'Texas')
        self.assertItemsEqual(partner.zip, '78725')
        self.assertItemsEqual(partner.country_id.name, 'United States')
        self.assertItemsEqual(partner.phone, '(650) 681-5000')
        self.assertItemsEqual(partner.website, self.env['res.partner']._clean_website('www.tesla.com'))


# @tagged('zoom_info')
# class TestZoomInfo(TestZoomInfoCommonBase):
#
#     def test_creation(self):
#         ctx = self._context
#         zoom_info = self.env[ctx['active_model']].sudo().browse(ctx['active_ids'])
