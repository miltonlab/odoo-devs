# -*- coding: utf-8 -*-

import xmlrpclib
import logging
import csv

USR = 'admin' #the user
PWD = 'comprasunl' #the password of the user
DBNAME = 'comprasunl' #the database
HOST = 'localHOST'
PORT = 8068

def main():
    logging.basicConfig(filename="/tmp/odoo_load_products.log",
                        level   = logging.DEBUG, 
                        datefmt = '%Y/%m/%d %I:%M:%S %p', 
                        format  = '%(asctime)s : %(levelname)s - %(message)s'
    )

    logging.info('Starting Load product ...')
    sock_common = xmlrpclib.ServerProxy ('http://%s:%s/xmlrpc/common' % (HOST,PORT))
    uid = sock_common.login(DBNAME, USR, PWD)
    sock = xmlrpclib.ServerProxy('http://%s:%s/xmlrpc/object' % (HOST,PORT))

    # Category creation
    category = {'name': 'Catálogo de Compras Públicas', 'parent_id': 1, 'active': True,}
    category_id = sock.execute(DBNAME, uid, PWD, 'product.category', 'create', category)
    # Product creation
    filename = "product.product.csv"
    #filename = "product.product.test.csv"
    reader = csv.reader(open(filename,"rb"))
    # Skip the headers
    reader.next()
    for row in reader:        
        product_product = {
            'default_code' : row[1].strip(),
            'name' : row[2].strip(),
            'taxes_id' : row[3],
            'supplier_taxes_id' : row[4],
            'uom_id' : 1,
            'uom_po_id' : 1,
            'categ_id' : category_id,
            'sale_ok' : False, 
        }
        product_id = sock.execute(DBNAME,uid,PWD,'product.product','create',product_product)
        logging.info('Created: {0}'.format(product_product))
        logging.info('Id product: {0}'.format(product_id))


    logging.info('Product Load finished !!!')
    
if __name__ == '__main__':
    try:
        main()
    except Exception, ex:
        print 'Error loading product: ', str(ex)
