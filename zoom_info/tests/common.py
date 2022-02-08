from datetime import timedelta
from odoo.addons.zoom_info.models.zoom_info import ZoomInfo
from odoo import fields
from odoo.tests import TransactionCase, SavepointCase


class TestZoomInfoCommonBase(TransactionCase):

    def setUp(self):
        super(TestZoomInfoCommonBase, self).setUp()
        self.partner_1 = self.env['res.partner'].create({
            'name': 'Test Partner'
        })

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

        self.patch(ZoomInfo, 'zoom_info_request', _zoom_info_request)
