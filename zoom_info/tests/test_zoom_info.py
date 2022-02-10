from datetime import timedelta

from odoo.exceptions import ValidationError
from odoo.tests import tagged, Form, HttpCase, TransactionCase
from odoo import fields
from odoo.addons.zoom_info.models.zoom_info import ZoomInfo
from ..models.zoom_api import ZoomApi
from odoo.addons.website.tools import MockRequest
from unittest import mock
from odoo.addons.zoom_info.models.zoom_api import ZoomApi

SEARCH_COMPANY = {'maxResults': 1110, 'totalResults': 25, 'currentPage': 1,
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

ENRICH_COMPANY = {'success': True, 'data': {'outputFields': [
            ['name', 'street', 'city', 'state', 'zipcode', 'country', 'phone', 'website', 'logo', 'id']],
            'result': [{'input': {'companyid': '104333869'}, 'data': [
                {'name': 'Tesla', 'street': '13101 Harold Green Road',
                 'city': 'Austin', 'state': 'Texas', 'zipCode': '78725',
                 'country': 'United States', 'phone': '(650) 681-5000',
                 'website': 'www.tesla.com',
                 'logo': 'https://res.cloudinary.com/zoominfo-com/image/upload/w_100,h_100,c_fit/tesla.com',
                 'id': 104333869}], 'matchStatus': 'FULL_MATCH'}]}}


def _zoom_info_request(self, url, params=None):
    response = dict()
    if url == "/search/company":
        response = SEARCH_COMPANY
    if url == "/enrich/company":
        response = ENRICH_COMPANY
    return response['data']


# This method will be used by the mock to replace requests.post
def mocked_requests_post(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == 'https://api.zoominfo.com/authenticate':
        return MockResponse({'jwt': "Token123"}, 200)
    elif args[0] == 'https://api.zoominfo.com/search/company':
        return MockResponse(SEARCH_COMPANY, 200)
    elif args[0] == 'https://api.zoominfo.com/enrich/company':
        return MockResponse(ENRICH_COMPANY, 200)

    return MockResponse(None, 401)


@tagged('-at_install', 'post_install', 'zoom_info')
class TestZoomJs(HttpCase):
    def setUp(self):
        super(TestZoomJs, self).setUp()
        self.patch(ZoomInfo, 'zoom_info_request', _zoom_info_request)

    # @mock.patch('odoo.addons.zoom_info.models.zoom_api.requests.post', side_effect=mocked_requests_post)
    # def test_tour(self, mock_post):
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


@tagged('zoom_info')
class TestZoomInfo(TransactionCase):
    def setUp(self):
        super(TestZoomInfo, self).setUp()
        self.zoom_info_test = self.env['zoom.info'].create([])
        self.patch(ZoomInfo, 'zoom_info_request', _zoom_info_request)
        self.maxDiff = None


    # @mock.patch('odoo.addons.zoom_info.models.zoom_info.requests.post', side_effect=mocked_requests_post)
    def test_creation(self, mock_post):
        companies = self.zoom_info_test.find_company_id('Tesla')
        expected_companies = [{'id': 104333869, 'name': 'Tesla'},
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
                              {'id': 346396693, 'name': 'Tesla Transformers'}]
        self.assertItemsEqual(companies, expected_companies)