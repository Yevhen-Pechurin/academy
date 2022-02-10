# -*- coding: utf-8 -*-
{
    'name': "sale_origin",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Modification for sales module
    """,
    'author': "Shkvalik",
    'website': "http://www.yourcompany.com",
    'category': 'Sales',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],
    # always loaded
    'data': [
        'reports/sale_origin_templates.xml',
        'views/sale_origin_product.xml',
        'views/sale_origin_order.xml',
        'views/sale_country_of_origin_templates.xml',
    ],
    # only loaded in demonstration mode
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
