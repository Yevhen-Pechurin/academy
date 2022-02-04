# -*- coding: utf-8 -*-
{
    'name': "Demo",

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
    'version': '0.1',

    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['mail', 'contacts', 'website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'data/demo_state_data.xml'
        'data/ir_sequence_data.xml',
        'wizards/view_wizard_new_demo.xml',
        'views/demo_views.xml',
        'views/res_partner_views.xml',
        'report/demo_report_views.xml'

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
}
