{
    'name': 'Sale Order PDF Button',
    'version': '18.0',
    'summary': 'Generate a custom PDF report from Sale Order header button',
    'depends': ['sale_management'],
    'data': [
        'reports/sale_report_template.xml',
        'reports/sale_report_proposal_template.xml',
        'reports/sale_report_action.xml',
        'views/sale_order_form_button.xml',
    ],
    'installable': True,
    'application': False,
}
