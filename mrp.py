# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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


from openerp.osv import fields, osv
from openerp.tools.translate import _
from openerp import pooler, tools
from openerp import netsvc
from openerp import release
import datetime
from pytz import timezone
import pytz
from dateutil.relativedelta import relativedelta

from datetime import date, datetime, timedelta
import time
import pytz

import os
from openerp import SUPERUSER_ID

class mrp_production(osv.osv):
    _name = 'mrp.production'
    _inherit ='mrp.production'
    _columns = {
        }

    _defaults = {
        'location_src_id': False,
        'location_dest_id': False,
        }

class stock_production_lot(osv.osv):
    _name = 'stock.production.lot'
    _inherit ='stock.production.lot'
    _columns = {
    'user_id': fields.many2one('res.users','Creado por'),
    'name': fields.char('No. de Serie', size=128, required=False),
    'name_required': fields.boolean('Nombre Requerido'),
        }

    def _get_uid(self, cr, uid, context=None):
        return uid

    _defaults = {  
        'user_id': _get_uid,
        'name': False,
        'name_required': False,
        }

    def restart_serie_actual(self, cr, SUPERUSER_ID, automatic=False, use_new_cursor=False, context=None):
        # print "############# REINICIANDO LAS SECUENCIAS  >>>>> "
        ########### REINICIANDO LAS SECUENCIAS A 1 #########
        ############## USANDO EL TZ DEL USUARIO ###############
        # date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # start = datetime.strptime(date_now, "%Y-%m-%d %H:%M:%S")
        # user = self.pool.get('res.users').browse(cr, SUPERUSER_ID, SUPERUSER_ID)
        # print "###################### TZ USER >>>>>>>>> ",  user.tz
        # tz = pytz.timezone(user.tz) if user.tz else pytz.utc
        # start = pytz.utc.localize(start).astimezone(tz)     # convert start in user's timezone
        # tz_date = start.strftime("%Y-%m-%d %H:%M:%S")
        # print "########################## DATE FINAL TZ >>> ", tz_date

        date_prefix = datetime.now().strftime('%Y%m%d')
        sequence_obj = self.pool.get('ir.sequence')
        sequence_id = sequence_obj.search(cr, SUPERUSER_ID, [('code','=','stock.production.lot')])
        sequence_obj.write(cr, SUPERUSER_ID, sequence_id, 
            {'number_next_actual': 1, 'prefix': str(date_prefix) })

        return True

    # def _check_lot(self, cr, uid, ids, context=None):
    #     for rec in self.browse(cr, uid, ids, context=None):
    #         lot_ids = self.search(cr, uid, [('name','=',rec.name),('id','!=',ids[0])])
    #         if lot_ids:
    #             return False
    #     return True
    # _constraints = [(_check_lot, 'Error: El Numero de Serie debe ser unico.\n Consulta al Administrador.', ['name']), ] 

    # _sql_constraints = [     ('name_uniq', 'unique (name)', 'El nombre del No. de Serie debe ser Unico !'),      ]

    def copy(self, cr, uid, id, default=None, 
        context=None):
        # default = {} Diccionario con valores a poner
        # por defecto!!!
        self_br = self.browse(cr, uid, id, context)
        nuevo_name = self_br.name + " (Copia)"
        default.update({
            'name': nuevo_name,
            })

        res = super(stock_production_lot, self).copy(
            cr, uid, id, default, context)
        return res

    def add_numbers(self, numero):
        if numero < 10:
            numero = '0000'+str(numero)
        elif numero >= 10 and numero < 100:
            numero = '000'+str(numero)
        elif numero >= 100 and numero <1000:
            numero = '00'+str(numero)
        elif numero >= 1000 and numero <10000:
            numero = '0'+str(numero)
        else:
            numero = str(numero)
        return numero

    def create(self, cr, uid, vals, context=None):
        # vals.update({'name':name_lot})
        if 'name' in vals:
            name = vals['name']
            if name == False or name == '':
                seq_id = self.pool.get('ir.sequence').search(cr, uid, [('code','=','stock.production.lot')])
                name_lot = self.pool.get('ir.sequence').get_id(cr, uid, seq_id[0])
                vals.update({'name':name_lot})
        else:
            seq_id = self.pool.get('ir.sequence').search(cr, uid, [('code','=','stock.production.lot')])
            name_lot = self.pool.get('ir.sequence').get_id(cr, uid, seq_id[0])
            vals.update({'name':name_lot})
        return super(stock_production_lot, self).create(cr, uid, vals, context=context)
