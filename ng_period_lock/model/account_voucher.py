##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-TODAY OpenERP S.A. <http://www.openerp.com>
#    Copyright (C) 2014-TODAY Mattobell (<http://www.mattobell.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import osv, fields
from datetime import datetime, timedelta

class account_voucher(osv.osv):
    _inherit = "account.voucher"
    
    def create(self, cr, uid, vals, context=None):
        current_date = datetime.now()
        p_lock_id = self.pool.get("period.lock").search(cr, uid, [('model_str','=','account.voucher')],context=context)
        period_brw = self.pool.get("period.lock").browse(cr, uid, p_lock_id, context=context)
        for rec in period_brw:
            if not rec.create:
                continue
            warning = rec.warning
            lock_group_user = []
            for grp_id in rec.group_ids:
                lock_group_user += [u.id for u in grp_id.users]
            lock_user = [usr_id.id for usr_id in rec.user_id]
            
            lock_start_date = datetime.strptime(rec.lock_start_date, "%Y-%m-%d %H:%M:%S")
            if uid in lock_user or uid in lock_group_user:
                if rec.create == True:
                    if rec.lock_end_date:
                        lock_end_date = datetime.strptime(rec.lock_end_date, "%Y-%m-%d %H:%M:%S")
                        if current_date >= lock_start_date and current_date <= lock_end_date:
                            raise osv.except_osv(('Warning'),('%s')%(warning,))
                    elif current_date >= lock_start_date:
                        raise osv.except_osv(('Warning'),('%s')%(warning,))
        return super(account_voucher, self).create(cr, uid, vals, context=context)
    
    def write(self, cr, uid, ids, vals, context=None):
        new_state = vals.get('state', False)
        current_date = datetime.now()
        p_lock_id = self.pool.get("period.lock").search(cr, uid, [('model_str','=','account.voucher')],context=context)
        period_brw = self.pool.get("period.lock").browse(cr, uid, p_lock_id, context=context)
        for rec in period_brw:
            lock_state = rec.state
            warning = rec.warning
            lock_user = [usr_id.id for usr_id in rec.user_id]
            lock_group_user = []
            for grp_id in rec.group_ids:
                lock_group_user += [u.id for u in grp_id.users]
            lock_start_date = datetime.strptime(rec.lock_start_date, "%Y-%m-%d %H:%M:%S")
            if uid in lock_user or uid in lock_group_user:
                if rec.write == False and lock_state and new_state:
                    if rec.lock_end_date:
                        lock_end_date = datetime.strptime(rec.lock_end_date, "%Y-%m-%d %H:%M:%S")
                        if current_date >= lock_start_date and current_date <= lock_end_date:
                            if new_state == lock_state:
                                raise osv.except_osv(('Warning'),('%s')%(warning,))
                    elif current_date >= lock_start_date:
                        if new_state == lock_state:
                            raise osv.except_osv(('Warning'),('%s')%(warning,))
                elif rec.write == True and not lock_state:
                    if rec.lock_end_date:
                        lock_end_date = datetime.strptime(rec.lock_end_date, "%Y-%m-%d %H:%M:%S")
                        if current_date >= lock_start_date and current_date <= lock_end_date:
                            raise osv.except_osv(('Warning'),('%s')%(warning,))
                    elif current_date >= lock_start_date:
                        raise osv.except_osv(('Warning'),('%s')%(warning,))
                elif rec.write == True and lock_state:
                    if rec.lock_end_date:
                        lock_end_date = datetime.strptime(rec.lock_end_date, "%Y-%m-%d %H:%M:%S")
                        if current_date >= lock_start_date and current_date <= lock_end_date:
                            raise osv.except_osv(('Warning'),('%s')%(warning,))
                    elif current_date >= lock_start_date:
                        raise osv.except_osv(('Warning'),('%s')%(warning,))
        return super(account_voucher, self).write(cr, uid, ids, vals, context=context)
    
    def unlink(self, cr, uid, ids, context=None):
        current_date = datetime.now()
        p_lock_id = self.pool.get("period.lock").search(cr, uid, [('model_str','=','account.voucher')],context=context)
        period_brw = self.pool.get("period.lock").browse(cr, uid, p_lock_id, context=context)
        for rec in period_brw:
            if not rec.delete:
                continue
            lock_group_user = []
            for grp_id in rec.group_ids:
                lock_group_user += [u.id for u in grp_id.users]
            warning = rec.warning
            lock_user = [usr_id.id for usr_id in rec.user_id]
            lock_start_date = datetime.strptime(rec.lock_start_date, "%Y-%m-%d %H:%M:%S")
            if uid in lock_user or uid in lock_group_user:
                if rec.delete == True:
                    if rec.lock_end_date:
                        lock_end_date = datetime.strptime(rec.lock_end_date, "%Y-%m-%d %H:%M:%S")
                        if current_date >= lock_start_date and current_date <= lock_end_date:
                            raise osv.except_osv(('Warning'),('%s')%(warning,))
                    elif current_date >= lock_start_date:
                        raise osv.except_osv(('Warning'),('%s')%(warning,))
        return super(account_voucher,self).unlink(cr, uid, ids, context=context)
    
    def copy(self, cr, uid, id, default=None, context=None):
        current_date = datetime.now()
        p_lock_id = self.pool.get("period.lock").search(cr, uid, [('model_str','=','account.voucher')],context=context)
        period_brw = self.pool.get("period.lock").browse(cr, uid, p_lock_id, context=context)
        for rec in period_brw:
            if not rec.duplicate:
                continue
            warning = rec.warning
            lock_group_user = []
            for grp_id in rec.group_ids:
                lock_group_user += [u.id for u in grp_id.users]
            lock_user = [usr_id.id for usr_id in rec.user_id]
            lock_start_date = datetime.strptime(rec.lock_start_date, "%Y-%m-%d %H:%M:%S")
            if uid in lock_user or uid in lock_group_user:
                if rec.duplicate == True:
                    if rec.lock_end_date:
                        lock_end_date = datetime.strptime(rec.lock_end_date, "%Y-%m-%d %H:%M:%S")
                        if current_date >= lock_start_date and current_date <= lock_end_date:
                            raise osv.except_osv(('Warning'),('%s')%(warning,))
                    elif current_date >= lock_start_date:
                        raise osv.except_osv(('Warning'),('%s')%(warning,))
        return super(account_voucher,self).copy(cr, uid, id, default=default, context=context)
    
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: