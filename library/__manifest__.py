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
    'version': '0.3',

    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['mail', 'website'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/ir_cron.xml',
        'data/ir_sequence_data.xml',
        'wizards/view_wizard_book_on_hand.xml',
        'views/book_views.xml',
        'views/res_partner_views.xml',
        'views/templates.xml',
        'report/qrcode_book_report.xml',
        'report/qrcode_book_template.xml',
        'report/book_report_views.xml',
        'views/menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'library/static/src/js/tours/library.js',
        ],
    },
    'application': True,
    'installable': True,
}
