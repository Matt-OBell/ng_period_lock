# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014-Today Mattobell (<http://www.mattobell.com>)

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################

from openerp.osv import osv, fields
from datetime import datetime, timedelta

MODEL_DOMAIN = ['account.invoice','account.bank.statement','account.move','account.voucher',
                'account.transfer','account.asset.asset','asset.disposal','asset.maintanance',
                'cash.advance','hr.attendance','hr.holidays','hr_evaluation.evaluation',
                'hr.expense.expense','hr.overtime','hr.payslip','internal.requisition',
                'mrp.production','purchase.order','refund.advance','ret.expense',
                'salary.advance','salary.increment','sale.order','stock.move','stock.picking',]

class period_lock(osv.osv):
    _name = "period.lock"
    
    def _check_state(self, cr, uid, ids, context=None):
        state_brw = self.browse(cr, uid, ids, context=context)[0]
        state_help_list = state_brw.help_state
        state_help_list = state_help_list.split(',')
        state = state_brw.state
        if state:
            if not state in state_help_list:
                return False
        return True
    
    _columns = {
        'model_id' : fields.many2one('ir.model', 'Select Model', required=1, domain =[('model','in', MODEL_DOMAIN)]),
        'create': fields.boolean('Create'),
        'write' : fields.boolean('Write'),
        'delete':fields.boolean('Delete'),
        'duplicate': fields.boolean('Duplicate'),
        'model_str':fields.related('model_id', 'model', store=True, type='char',string="Model Name"),
        'state':fields.char('State'),
        'help_state': fields.char('State Help'),
        'lock_start_date' : fields.datetime('Lock Start Date', required=1),
        'lock_end_date': fields.datetime('Lock End Date'),
        'date_create':fields.date('Create Date',required=1),
        'user_id': fields.many2many('res.users','res_users_lock_id','lock_id','user_id','Select User'),
        'group_ids': fields.many2many('res.groups','res_group_lock_id','lock_grp_id','group_id','Select Group'),
        'warning': fields.text('Warning Message'),
        'active': fields.boolean('Active'),
        'company_id':fields.many2one('res.company','Company', required=1),
        'resp_user_id': fields.many2one('res.users','Responsible', required=1),
        'email_template_id': fields.many2one('email.template','Email Template')
    }
    _rec_name = 'model_str'
    _constraints = [
        (_check_state, 'Please enter valid state!',['state'])
    ]
    
    _defaults = {
        'active': True,
        'date_create': fields.date.context_today,
        'company_id': lambda self, cr, uid, context: \
                self.pool.get('res.users').browse(cr, uid, uid,
                    context=context).company_id.id,
        'resp_user_id': lambda self, cr, uid, context: self.pool.get('res.users').browse(cr, uid, uid, context).id ,
    }
    
    def on_change_model(self, cr, uid, ids,  model_id, context=None):
        result = {}
        if model_id:
            model_record = self.pool.get("ir.model").browse(cr, uid, model_id, context=context)
            res= dict(self.pool.get(model_record.model).fields_get(cr, uid, allfields=[], context=context))
            if res.get('state', False):
                states = res['state']['selection']
                state_list = []
                for key in states:
                    state_list.append(key[0])
                value_to_set = ','.join(map(str, state_list))
                result.update({
                    'help_state':value_to_set,
                    'state':False
                })
            else:
                result.update({
                    'help_state': 'Please do not use state.',
                    'state':False
                })
        return {'value': result} 

period_lock()       
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
