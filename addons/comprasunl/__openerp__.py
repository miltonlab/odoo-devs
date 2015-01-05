
# -*- coding: utf-8 -*-
{
    'name': 'COMPRAS-UNL',
    'version': '1.0',
    'description': '''
    Module for generate Orders for Public Purchases at Universidad Nacional de Loja. 

    Finishing Installation
    
    Do not forget the following after installation: 
    * Disable the Purchase Order Sequence default to enable the module sequence.
    * Import product.product.csv file with import_product.product.py script.
    
    ''',
    'author': 'Milton Labanda',
    'category': 'UNL Applications',
    'website': 'http://1000tonlab.wordpress.com',
    'depends': ['base', 'hr', 'purchase', 'web'],
    'data': [
        'data/config.xml',
        'purchase_sequence_unl.xml',
        'security/siscop_security.xml',
        'security/ir.model.access.csv',
        'data/res_user.xml',
        'data/siscop.item_budget.csv',
	'data/res.users.csv',
        'data/hr.department.csv',
        'data/hr.employee.csv',
        'product_view.xml',
        'hr_view.xml',
        'purchase_view.xml',
        'purchase_workflow.xml',
        'purchase_report_actions.xml',
        'report_header.xml',
        'report_purchaseorder_unl.xml',
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
