{
    'name': 'Project Access Solar',
    'version': '18.0',
    'depends': ['project', 'solar_energy_system'],
    'author': 'Arclight Infotech',
    'category': 'Project',
    'description': 'Give access to user for write fields and document upload.',
    'data': [
        "security/groups.xml",
        "security/ir.model.access.csv",
    ],
    'license': "OPL-1",
    'installable': True,
    'application': True,
    'auto_install': False,
}
