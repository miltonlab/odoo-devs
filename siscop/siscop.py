from openerp.osv import fields, osv
from openerp.tools.translate import _

# class purchase_requisition_siscop(osv.osv):
#     _name = 'purchase.requisition.siscop'
#     _inherit = 'purchase.requisition'
#     _description = 'Purchase Requisition for SISCOP'
#     _columns = {
#         'another': fields.char('Another', required=True, size=64, translate=True),
#         }

class purchase_order_line(osv.osv):
    _name = 'purchase.orde.line.siscop'
    _inherit = 'purchase.order.line'
    _description = 'Purchase Order Line for SISCOP'
    _defaults = {
        'date_planned': fields.datetime.now,
        }
