{
    'name': 'Solar Energy Systems',
    'version': '18.0',
    'depends': ['project', 'sale_management', 'sale','crm', 'account'],
    'author': 'Arclight Infotech',
    'category': 'Project',
    'description': 'Automatically adds custom stages to new projects.',
    'data': [
        "security/ir.model.access.csv",
        "views/project_task_views.xml",
        "views/crm_lead_view.xml",
        "views/payment_detail_view.xml",
        "views/registration_view.xml",
    ],
    'license': "OPL-1",
    'installable': True,
    'application': True,
    'auto_install': False,
}
