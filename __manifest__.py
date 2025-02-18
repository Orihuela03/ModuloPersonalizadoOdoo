# -*- coding: utf-8 -*-
{
    'name': 'Custom Project Management',
    'version': '1.0',
    'summary': """Gestión personalizada de proyectos para empresas de desarrollo de software""",
    'depends': ['base', 'project'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/contracting_company_views.xml',
        'views/project_views.xml',
        'views/task_views.xml',
        'views/subtask_views.xml'
    ],
    'installable': True,
    'application': True,
    'images': ['static/description/icon.png'],
}
