# -*- coding: utf-8 -*-


{
    'name': 'Car Rental',
    'category': 'Services/Car Rental',
    'depends': [
        'mail',
	],
    'data': [
        'security/ir.model.access.csv',
        'views/car_views.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'rental/static/src/js/*.js',
    ],
        'web.assets_qweb': [
            'rental/static/src/xml/*.xml',
        ]},
    'application': True,
    'installable': True,
    'license': 'GPL-3'
}
