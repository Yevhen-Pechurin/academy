# -*- coding: utf-8 -*-
{
    'name': "library",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Smartteksas",
    'website': "http://www.smartteksas.com",

    'category': 'Library',
    'version': '0.1',

    # 'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['mail'],

    # always loaded
    'data': [
        'data/ir_cron.xml',
        'security/ir.model.access.csv',
        'wizards/view_wizard_book_on_hand.xml',
        'views/book_views.xml',
        'views/res_partner_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
}
