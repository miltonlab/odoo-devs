
import xmlrpclib
import logging
import csv

username = 'admin' #the user
pwd = 'comprasunl' #the password of the user
dbname = 'comprasunl' #the database
host = 'localhost'
port = 8068

def main():
    logging.basicConfig(filename="/tmp/odoo_load_products.log")
    logging.info('Starting Load product ...')
    sock_common = xmlrpclib.ServerProxy ('http://%s:%s/xmlrpc/common' % (host,port))
    uid = sock_common.login(dbname, username, pwd)
    sock = xmlrpclib.ServerProxy('http://%s:%s/xmlrpc/object' % (host,port))

    #load categories first
    # filename = "data/product.product.csv"
    # reader = csv.reader(open(filename,"rb"))
    # for row in reader:
    #     category = {
    #         'name': row[1],
    #         'active': True,
    #     }
    #     category_id = sock.execute(dbname, uid, pwd, 'res.partner.category', 'create', category)
    #     print category_id
    #     print "End categories load"
        
    # filename = "product.product.csv"
    # reader = csv.reader(open(filename,"rb"))
    # for row in reader:
    #     product_template = {
    #         'name' : row[2].strip(),
    #         'supply_method':'produce',
    #         'standard_price':1,
    #         'mes_type':'fixed',
    #         'uom_id':1,
    #         'uom_po_id':1,
    #         'type':'product',
    #         'procure_method':'make_to_stock',
    #         'cost_method':'standard',
    #         'categ_id':1,
    #         'categ_id':1,            
    #     }
    #     template_id = sock.execute(dbname, uid, pwd, 'product.template', 'create', product_template)
    #     print template_id

    filename = "product.product.csv"
    reader = csv.reader(open(filename,"rb"))
    for row in reader:        
        product_product = {
            'default_code' : row[1].strip(),
            'name' : row[2].strip(),
            'taxes_id' : row[3],
            'supplier_taxes_id' : row[4],
        }
        product_id = sock.execute(dbname,uid,pwd,'product.product','create',product_product)
        logging.info('Created: {0}'.format(product_product))
        logging.info('Id product: {0}'.format(product_id))
    logging.info('Product Load finished !!!')
    
if __name__ == '__main__':
    try:
        main()
    except Exception, ex:
        print 'Error loading product: ', str(ex)
