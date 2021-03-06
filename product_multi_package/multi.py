# -*- coding: utf-8 -*-
###############################################################################
#
#    Copyright (C) 2001-2014 Micronaet SRL (<http://www.micronaet.it>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
import os
import sys
import logging
import openerp
import openerp.netsvc as netsvc
import openerp.addons.decimal_precision as dp
from openerp.osv import fields, osv, expression, orm
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from openerp import SUPERUSER_ID, api
from openerp import tools
from openerp.tools.translate import _
from openerp.tools.float_utils import float_round as round
from openerp.tools import (DEFAULT_SERVER_DATE_FORMAT, 
    DEFAULT_SERVER_DATETIME_FORMAT, 
    DATETIME_FORMATS_MAP, 
    float_compare)


_logger = logging.getLogger(__name__)

class ProductMultiPackaging(orm.Model):
    ''' Object for manage multi pack in product
    '''
    _name = 'product.multi.packaging'
    _description = 'Multi packaging'
    _rec_name = 'sequence'
    _order = 'sequence'
    
    _columns = {
        'sequence': fields.integer('Seq.', 
            help='Sequence order when displaying a list of packaging.'),
        'name': fields.char('Description', size=80),
        'number': fields.integer('Tot.',
            help='The total number of this package.'),
        'ul_id': fields.many2one('product.ul', 'Package', 
            required=True),
        #'product_tmpl_id': fields.many2one('product.template', 
        #    'Product', select=1, ondelete='cascade'),
        'product_id': fields.many2one('product.product', 
            'Product', select=1, ondelete='cascade'),
        #'ean': fields.char('EAN', size=14, 
        #    help='The EAN code of the package unit.'),
        'code': fields.char('Code', 
            help='The code of the transport unit.'),

        'height': fields.float('Height', help='Height of the pack'),
        'width': fields.float('Width', help='Width of the pack'),
        'length': fields.float('Length', help='Length of the pack'),

        'weight': fields.float('Weight',
            help='The weight of a full package, pallet or box.'),
        }
        
    _defaults = {
        'number': lambda *x: 1,
        }    

class ProductProduct(orm.Model):
    ''' Add relation fields
    '''
    _inherit = 'product.product'
    
    _columns = {
        'multi_pack_ids': fields.one2many(
            'product.multi.packaging', 'product_id', 'Multipack',
            help='Multipack for package one item'),

        # TODO colls in product? > campo function
        }
        
        
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
