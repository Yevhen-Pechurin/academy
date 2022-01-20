# -*- coding: utf-8 -*-
{
    'name': "Rental Car",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Rental Car',
    'version': '0.1',

    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['mail', 'web'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'wizards/view_wizard_car_on_rent.xml',
        'views/car_views.xml',
        'views/templates.xml',
    ],

    'assets': {
        'web.assets_qweb': {
            'rental/static/src/xml/model_widget.xml',
        },
        'web.assets_backend': [
            'rental/static/src/js/model_widget.js',
            'rental/static/src/js/animal.js',
            'rental/static/src/js/dog.js',
            'rental/static/src/js/engine.js',
            'rental/static/src/js/car.js',
        ],
    },

    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
}
