# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloPersonalizadoOdoo(http.Controller):
#     @http.route('/modulo_personalizado_odoo/modulo_personalizado_odoo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_personalizado_odoo/modulo_personalizado_odoo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_personalizado_odoo.listing', {
#             'root': '/modulo_personalizado_odoo/modulo_personalizado_odoo',
#             'objects': http.request.env['modulo_personalizado_odoo.modulo_personalizado_odoo'].search([]),
#         })

#     @http.route('/modulo_personalizado_odoo/modulo_personalizado_odoo/objects/<model("modulo_personalizado_odoo.modulo_personalizado_odoo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_personalizado_odoo.object', {
#             'object': obj
#         })
