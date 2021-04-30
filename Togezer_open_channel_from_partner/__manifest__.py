{
    'name': 'togezer_open_channel_from_partner',
    'summary': '''Add button "Send message" in partner form view to open an internal channel with the partner''',
    'license': 'AGPL-3',
    'author': (
        'Stéphan Sainléger - Elabore'
    ),
    'website': 'https://elabore.coop',
    'category': 'Discuss',
    'version': '13.0.1.0.0',
    'depends': [
        'base_setup',
        'mail',
    ],
    'data': [
        'views/res_partner.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
}
