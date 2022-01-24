# -*- coding: utf-8 -*-
{
    'name': "rental_car",

    'summary': """
apps.rental-car.com""",

    'description': """
        web for car rent
    """,

    'author': "SmartTeck",
    'website': "http://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '15.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'website', 'web'],
    'assets': {
        'web.assets_backend': [
            'rental_car/static/src/js/**/*',
        ],
    },

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/view_wizard_to_rent.xml',
        'wizard/view_wizard_in_garage.xml',
        'views/views.xml',
        'views/templates.xml',
        'data/ir_cron.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "application": True,
    'license': 'LGPL-3',
}
