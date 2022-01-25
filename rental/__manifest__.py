# -*- coding: utf-8 -*-


{
    'name': 'Car Rental',
    'category': 'Services/Car Rental',
    'depends': [
        'mail',
	],
    'demo': [
        'demo/demo.xml',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/car_views.xml',
        'report/car_barcode_report.xml',
        'report/car_barcode_template.xml',
    ],
    'assets': {
        'web.assets_qweb': [
            'rental/static/src/xml/*.xml',
            'rental/static/src/components/*/*.xml',
        ],
        'web.assets_backend': [
            'rental/static/src/js/*.js',
            'rental/static/src/components/*/*.js'
        ],
    },
    'application': True,
    'installable': True,
    'license': 'GPL-3'
}
