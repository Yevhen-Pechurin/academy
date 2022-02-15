{
    'name': "BlueSky MRP Workorder",
    'summary': """BlueSky MRP Workorder customisations""",
    'license': 'LGPL-3',
    'author': "Smart IT",
    'website': 'https://smart-ltd.co.uk',
    'category': 'Tools',
    'version': '13.0.3.0.0',
    'depends': [
        'mrp',
        'mrp_workorder',
        'sale',
        'web',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/mrp_bom_view.xml',
        'views/mrp_workorder_views.xml',
        'views/mrp_production_view.xml',
    ],
    'application': False,
    'installable': True,
}
