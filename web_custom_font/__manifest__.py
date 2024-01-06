{
    'name': 'Web custom font',
    'category': 'Tools',
    'description': '''
Web custom font
========================

Adding custom font in DIN 5008 PDF reports
''',
    'version': '17.0.0.0.0',
    'depends': [
        'web',
        'l10n_din5008',
    ],
    'data': [
        'report/din5008_report_extended.xml',
    ],
    'assets': {
        'web.report_assets_common': [
            (
                'after',
                'web/static/fonts/fonts.scss',
                'web_custom_font/static/fonts/fonts.scss',
            ),
        ]
    },
    'license': 'LGPL-3',
}