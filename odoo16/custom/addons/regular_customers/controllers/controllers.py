# -*- coding: utf-8 -*-
# from odoo import http


# class RegularCustomers(http.Controller):
#     @http.route('/regular_customers/regular_customers', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/regular_customers/regular_customers/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('regular_customers.listing', {
#             'root': '/regular_customers/regular_customers',
#             'objects': http.request.env['regular_customers.regular_customers'].search([]),
#         })

#     @http.route('/regular_customers/regular_customers/objects/<model("regular_customers.regular_customers"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('regular_customers.object', {
#             'object': obj
#         })
