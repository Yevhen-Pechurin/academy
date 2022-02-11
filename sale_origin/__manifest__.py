{
    'name': "sale_origin",  # Name for your module
    'summary': """Test""",  # Resume your module
    'description': """Modification for contacts module""",  # Description
    'author': "Shkvalik",  # Author
    'website': "https://resume-valentin-kovalenko.netlify.app/",
    'category': 'Sales',  # Category when will be your module
    'version': '0.1',
    'depends': ['base', 'sale_management', 'sale'],
    'data': [
        'reports/sale_origin_templates.xml',
        'views/sale_origin_product.xml',
        'views/sale_origin_order.xml',
        'views/sale_country_of_origin_templates.xml',
    ],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
