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

{
    'name' : 'Period Lock',
    'version': '1.0',
    'author': 'Mattobell',
    "website" : "http://www.mattobell.com",
    'description':"Lock on some forms for given users and groups on create, write, delete, copy.",
    'data':[
            'security/ir.model.access.csv',
            'period_lock_view.xml'
            ],
    'depends':['sale','purchase','account',
               'account_voucher','hr_attendance',
               'hr_holidays','stock','hr_evaluation',
               'ng_internal_requisition','ng_hr_payroll',
                'ng_account_asset',
               'account_transfer',
               'account_cash_advance',
               'hr_expense','hr_payroll','mrp','account_asset',
               ],
    'installable':True,
    'auto_install':False
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: