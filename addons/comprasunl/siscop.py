from openerp.osv import fields, osv
from openerp import api
from openerp.tools.translate import _
import openerp.addons.decimal_precision as dp

# class purchase_requisition_siscop(osv.osv):
#     _name = 'purchase.requisition.siscop'
#     _inherit = 'purchase.requisition'
#     _description = 'Purchase Requisition for SISCOP'
#     _columns = {
#         'another': fields.char('Another', required=True, size=64, translate=True),
#         }

class purchase_order_line_siscop(osv.osv):
    _name = 'purchase.order.line'
    _inherit = 'purchase.order.line'
    _description = 'Purchase Order Line for SISCOP'

    # def _get_number(self, cr, uid, ids, prop, arg, context=None):
    #     res = {}
    #     for i, line in enumerate(self.browse(cr, uid, ids)):
    #         res[line.id] = i
    #     return res


    _columns = {
        #'number' : fields.function(_get_number, string='No', digits_compute=dp.get_precision('Account')),
        'sequence' : fields.integer('Item'),
    }

    _defaults = {
        #'date_planned': fields.datetime.now,
        'sequence' : 0,
    }

    def create(self, cr, uid, vals, context=None):
        if vals.get('sequence',0)==0 and vals.get('order_id',None):
            all_lines = self.search(cr, uid, [('order_id', '=', vals['order_id'])])
            vals['sequence'] = len(all_lines) + 1
        return super(purchase_order_line_siscop, self).create(
            cr, uid, vals, context)     


class purchase_order_siscop(osv.osv):
    _name = 'purchase.order'
    _inherit = 'purchase.order'
    _description = 'Purchase Order for SISCOP'
    _defaults = {
        'purchase_project' : 'New Purchase Project',
    }

    _columns = {
        'requester' : fields.many2one('hr.employee', 'Requester', required=True), 
        'purchase_project' : fields.char('Project', size=255, required=True),
        'item_budget_id' : fields.many2one('siscop.item_budget', 'Item Budget', required=True),
        'code' : fields.related('item_budget_id', 'code',  type='integer',
                                relation='item_budget.code', store=False,
                                string='Item Budget Code'),
        'balance' : fields.related('item_budget_id', 'balance',  type='float',
                                   store=True,string='Item Budget Balance'),
        'approver' : fields.many2one('hr.employee', 'Approved by', required=True), # HalfOverriding 
    }

    def default_get(self, cr, uid, fields, context=None):
        res = super(purchase_order_siscop, self).default_get(cr, uid, fields, context=context)
        res_partner = self.pool['res.partner']
        # The first supplier found
        # Incop Supplier a provider by default.
        ids = res_partner.search(cr, uid, [('supplier', '=', True)], context=context)
        if ids:
            res['partner_id'] = ids[0]
        return res


    # TEST next:
    # @api.onchange('item_budget_id')
    # def onchange_item_budget_id(self):
    def onchange_item_budget_id(self, cr, uid, ids, item_budget_id, code, balance):
        item_budget = self.pool.get('siscop.item_budget').browse(cr, uid, item_budget_id)
        res = {'value':{}}
        orders = self.browse(cr, uid, ids)
        if orders:
            order = self.browse(cr, uid, ids)[0]
            new_balance = item_budget.balance - order.amount_total
        else:
            new_balance = item_budget.balance
        if new_balance < 0:
            res.update({'error':{'title':'error','message':_(
               'The item budget does not have sufficient balance !!!')}})
            order.item_budget_id = None
            res['value'].update({'code' : 0})
            res['value'].update({'balance' : 0.00})
        elif new_balance == 0:
            # res.update({'warning':{'title':'warning','message':_(
            #     'The item budget will be empty !!!')}})
            res['value'].update({'code' : item_budget.code})
            res['value'].update({'balance' : item_budget.balance})
        else:
            res['value'].update({'code' : item_budget.code})
            res['value'].update({'balance' : item_budget.balance})
        return res
            
    #item_budget_id_change = _onchange_item_budget_id

    def write(self, cr, uid, ids, vals, context=None):
        # order = self.browse(cr, uid, ids)[0]
        # if 'item_budget_id' in vals.keys() or 'order_line' in  vals.keys():
        #     print "*** changes ",order.item_budget_id.balance, ' *** ',  order.amount_total
        #     new_balance = order.item_budget_id.balance - order.amount_total
        #     if new_balance < 0:
        #         print "error ********* balance < 0 "
        #     else:
        #         order.item_budget_id.balance = new_balance
        #         ########## XXXXXXXX ESTO SE DEBE HACER SOLO AL CONFIRMAR LA ORDEN
        #         order.item_budget_id.write({'balance' : new_balance})
        #     ### order.item_budget_id.write() #####
        #     print '********* new balance: ', order.item_budget_id.balance
        res= super(purchase_order_siscop, self).write(cr, uid, ids, vals, context=context)
        return res

    def _amount_all(self, cr, uid, ids, field_name, arg, context=None):
        print '********* Calculating subtotals **********'
        res = super(purchase_order_siscop, self)._amount_all(
            self, cr, uid, ids, field_name, arg, context=context)
        return res


class item_budget(osv.osv):
    _name = 'siscop.item_budget'
    _description = 'Items Budget related to one Purchase Order'
    _columns = {
        'code' : fields.integer('Code'),
        'name' : fields.char('Name Item Budget', size=32, required=True),
        'balance' : fields.float('Balance', required=False)
    }

#purchase_order_line()
#purchase_order_siscop()
