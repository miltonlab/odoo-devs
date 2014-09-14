# -*- coding: utf-8 -*-
{
    'name': 'DDS Projects',
    'version': '1.0',
    'category': 'Project Management',
    'description': '''
Customization of Project Module for Software Development Department UNL
Testing in OpenERP v8.0 dev2014-03-14
''',
    'author': 'miltonlab',
    'website': 'http://1000tonlab.wordpress.com',
    'depends': ['base', 'project'],
    'data': [
        'project_view.xml',
    ],
    'test': [
    ],
    # Set to False if you want to prevent the module to be known by OpenERP
    # (and thus appearing in the list of modules).
    'installable': True,
    # Set to True if you want the module to be automatically whenever all its
    # dependencies are installed.
    'auto_install': False,
}
