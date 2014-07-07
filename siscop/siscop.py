from openerp.osv import fields, osv
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
        #'number' : fields.function(_get_number, string='No',                            digits_compute=dp.get_precision('Account')),
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
        'requester' : fields.many2one('hr.employee', 'Requester'), 
        'purchase_project' : fields.char('Project', size=255, required=True),
        'item_budget_id' : fields.many2one('siscop.item_budget', 'Item Budget', required=True),
        'code' : fields.related('item_budget_id', 'code',  type='integer',
                                relation='item_budget.code', store=False,
                                string='Item Budget Code'),
        'balance' : fields.related('item_budget_id', 'balance',  type='float',
                                   store=True,string='Item Budget Balance'),
    }

    def default_get(self, cr, uid, fields, context=None):
        print 'iniciando ....'
        res = super(purchase_order_siscop, self).default_get(cr, uid, fields, context=context)
        res_partner = self.pool['res.partner']
        # The first supplier found
        # Incop Supplier a provider by default.
        ###ids = res_partner.search(cr, uid, [('id', '=', 0)], context=context)
        ids = res_partner.search(cr, uid, [('supplier', '=', True)], context=context)
        print 'ids: ', ids
        if ids:
            res['partner_id'] = ids[0]
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
