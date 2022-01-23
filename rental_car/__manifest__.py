# -*- coding: utf-8 -*-
{
    'name': "rental_car",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Smartteksas",
    'website': "https://smartteksas.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Car',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['mail'],

    'license': 'LGPL-3',

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views_car.xml',
        # 'views/templates.xml',
        'wizards/view_wizard_car_rented.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_qweb': [
            # 'rental_car/static/src/xml/car_widget.xml',
            # 'rental_car/static/src/xml/car.xml',
        ],
        'web.assets_backend': [
            'rental_car/static/src/js/car_widget.js',
            # 'rental_car/static/src/js/car.js',
            # 'rental_car/static/src/js/engine.js',
            # 'rental_car/static/src/js/frame.js',
        ],
    },
    'application': True,
}
