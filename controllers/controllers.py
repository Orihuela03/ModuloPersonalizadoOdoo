# -*- coding: utf-8 -*-
# from odoo import http


# class CustomProjectManagement(http.Controller):
#     @http.route('/custom_project_management/custom_project_management/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_project_management/custom_project_management/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_project_management.listing', {
#             'root': '/custom_project_management/custom_project_management',
#             'objects': http.request.env['custom_project_management.custom_project_management'].search([]),
#         })

#     @http.route('/custom_project_management/custom_project_management/objects/<model("custom_project_management.custom_project_management"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_project_management.object', {
#             'object': obj
#         })
