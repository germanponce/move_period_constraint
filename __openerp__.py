# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2010 moylop260 - http://www.hesatecnica.com.com/
#    All Rights Reserved.
#    info skype: german_442 email: (german.ponce@hesatecnica.com)
############################################################################
#    Coded by: german_442 email: (german.ponce@hesatecnica.com)
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
{
    'name': 'Addons Fixes',
    'version': '1',
    "author" : "German Ponce Dominguez",
    "category" : "Nishikawa",
    'description': """

Este modulo soluciona pequeños Bugs como:
    - Eliminacion de la Restriccion de Fechas en Facturas para Proveedores.
    - Agrega el Codigo del Proveedor al Crear Cotizacion desde Solicitud.
    - Lotes, agrega una Restriccion que no permite crear No. Serie que ya existen en el Sistema. Solo Aplica para Series iguales con el mismo Producto.
    - Agrega un campo llamado  Creado Por, en la ficha de Series, para saber quien creo el No. de Serie.
    - Agrega una Validacion Extra a Polizas, en donde no puedes Cancelar un Asiento si el periodo esta Cerrado y si el Diario no Permite Cancelacion.

Configuracion Autmatica de Series:

    - Existe una Secuencia llamada Secuencia Series NCM, es la encargada de asignar la secuencia a
    - los Numeros de Serie.\n
    - Existe Una funcion Automatizada llamada Reinicio de Serie al Dia Actual, esta funcion permite que cada dia la serie se reinicie a 1, para poder continuar desde 1 con cada serie nueva.

Nota: Revisar que la serie siempre se reasigne a 1 para evitar continuar en el numero anterior.

    """,
    "website" : "http://poncesoft.blogspot.com",
    "license" : "AGPL-3",
    "depends" : ["account","sale","account_cancel"],
    "init_xml" : [],
    "demo_xml" : [],
    "update_xml" : [
#                    'mrp_view.xml',
#                    'data.xml',
#                    'account_view.xml',

                    ],
    "installable" : True,
    "active" : False,
}
