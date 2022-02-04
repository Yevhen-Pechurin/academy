# -*- coding: utf-8 -*-
{
    'name': "rental",

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
    'category': 'Uncategorized',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'web'],

    # always loaded
    'data': [
        'data/ir_sequence_data.xml',
        'security/ir.model.access.csv',
        'wizards/view_wizard_on_loan.xml',
        'wizards/view_wizard_in_garage.xml',
        'views/car_views.xml',
        'views/templates.xml',
        'report/barcode_car_report.xml',
        'report/barcode_car_template.xml',
        'report/car_report_views.xml',
        'views/menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_qweb': [
            'rental/static/src/xml/*.xml',
        ],
        'web.assets_backend': [
            'rental/static/src/js/*.js',
            'rental/static/src/js/tours/rental.js',
        ],
    },
    'license': 'LGPL-3',
}
