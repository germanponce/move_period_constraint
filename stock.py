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

import time
import os


class stock_move(osv.osv):
    _name = 'stock.move'
    _inherit ='stock.move'
    _columns = {
        }

    _defaults = {
        }
    _order = 'id desc'

# class split_in_production_lot(osv.osv_memory):
#     _name = 'stock.move.split'
#     _inherit ='stock.move.split'
#     _columns = {
        
#             }
#     _defaults = {  

#         }
