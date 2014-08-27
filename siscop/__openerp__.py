# -*- coding: utf-8 -*-
{
    'name': 'SISCOP UNL',
    'version': '1.0',
    'description': '''
    Module for generate Orders for Public Purchases at Universidad Nacional de Loja. Don't forget load the es_EC translation first.

    *Finishing Installation*
    
    Do not forget the following after installation:
    * 1. Import products.csv file
    * 2. Import item_budgets.csv file if exists.
    ''',
    'author': 'miltonlab',
    'website': 'http://1000tonlab.wordpress.com',
    'depends': ['base', 'hr', 'purchase', 'web'],
    'data': [
        'data/config.xml',
        'hr_view.xml',
        'purchase_view.xml',
        'security/siscop_security.xml',
        'security/ir.model.access.csv',
        'data/users.xml',
        'purchase_report_actions.xml',
        #'report_purchaseorder_unl.xml',
        'report_purchaseorder_unl.es.xml',
    ],
    'demo': [
        'data/products_part.csv',
    ],
    'js' : ['static/src/js/siscop.js'],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
}
