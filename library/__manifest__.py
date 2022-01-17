# -*- coding: utf-8 -*-
{
    'name': "Library",

    'summary': """
    The best Library""",

    'description': """
        My Library
    """,

    'author': "Stepanov Bohdan",
    'website': "http://www.Bohdan_smart.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '15.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizards/view_wizard_od_hand.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "application": True,
}
