# -*- coding: utf-8 -*-
{
    'name': "Library",

    'summary': """
       Test Library by inspiration679""",

    'description': """
        future description of Test Library by inspiration679
    """,

    'author': "Inpiration679",
    'website': "https://github.com/Inspiration679",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Library',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail','crm'],
    'license': 'LGPL-3',

# always loaded
'data': [
    'security/ir.model.access.csv',
    'views/views.xml',
    'wizards/wizard_on_hand.xml',
    'data/ir_chron.xml'
],
# only loaded in demonstration mode
# 'demo': [
#     'demo/demo.xml',
# ],
}
