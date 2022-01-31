# -*- coding: utf-8 -*-


{
    'name': 'Car Rental',
    'category': 'Services/Car Rental',
    'sequence': -50,
    'depends': [
        'mail',
        'contacts',
	],
    'demo': [
        'demo/demo.xml',
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/res_config_settings.xml',
        'views/res_partner_views.xml',
        'views/car_views.xml',
        'report/car_barcode_report.xml',
        'report/car_barcode_template.xml',
        'report/car_report_views.xml',
        'views/car_menus.xml',
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
    'license': 'LGPL-3'
}
