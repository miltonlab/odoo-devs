from openerp.osv import fields, osv
from openerp.tools.translate import _

class project_task_type(osv.osv):
    _name = 'project.project'
    _inherit = 'project.proyect'
    _description = 'Project DDS UNL'
    #_order = 'sequence'
    _columns = {
        'relevance': fields.char('Relevance', required=True, size=64, translate=True),
        }

