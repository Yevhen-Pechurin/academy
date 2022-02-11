{
    'name': "contact_extensions",  # Name for your module
    'summary': """Test""",  # Resume your module
    'description': """Modification for contacts module""",  # Description
    'author': "Shkvalik",  # Author
    'website': "https://resume-valentin-kovalenko.netlify.app/",
    'category': 'Sales',  # Category when will be your module
    'version': '0.1',
    'depends': ['base', 'contacts'],
    'data': [
        'views/contact_skype_view.xml'
    ],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
