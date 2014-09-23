# -*- coding: utf-8 -*-
{
    'name': 'COMPRAS-UNL',
    'version': '1.0',
    'description': '''
    Module for generate Orders for Public Purchases at Universidad Nacional de Loja. Don't forget 1) load the es_EC translation first 2) Disable Purchase Order Secuence for enable Purchase Order UNL Sequence.

    <b>Finishing Installation</b>
    
    Do not forget the following after installation: 
    * Import product.product.csv file with import_product.product.py script
    ''',
    'author': 'Milton Labanda',
    'website': 'http://1000tonlab.wordpress.com',
    'depends': ['base', 'hr', 'purchase', 'web'],
    'data': [
        'purchase_sequence_unl.xml',
        'hr_view.xml',
        'purchase_view.xml',
        'security/siscop_security.xml',
        'security/ir.model.access.csv',
        'data/config.xml',
        #'data/res.partner.csv',
        #'data/res.user.csv',
        'data/res_user.xml',
        'data/siscop.item_budget.csv',
        #'report_purchaseorder_unl.xml',
        'purchase_report_actions.xml',
        'report_purchaseorder_unl_es.xml',
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
