{
    'name': 'partner_gogocarto_export_api',
    'summary': '''HTTP JSON api to send partner data for Gogocarto import''',
    'license': 'AGPL-3',
    'author': (
        'Lokavaluto,'
        'Odoo Community Association (OCA)'
    ),
    'website': 'https://lokavaluto.fr',
    'category': 'Localization',
    'version': '13.0.1.0.0',
    'depends': [
        'base',
        'base_geolocalize'
    ],
    'data': [
        'views/gogocarto_partner.xml',
        'views/gogocarto_config_settings_view.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
}
