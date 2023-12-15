# -*- coding: utf-8 -*-
# from odoo import http


# class SalesAndInvoices(http.Controller):
#     @http.route('/sales_and_invoices/sales_and_invoices', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sales_and_invoices/sales_and_invoices/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sales_and_invoices.listing', {
#             'root': '/sales_and_invoices/sales_and_invoices',
#             'objects': http.request.env['sales_and_invoices.sales_and_invoices'].search([]),
#         })

#     @http.route('/sales_and_invoices/sales_and_invoices/objects/<model("sales_and_invoices.sales_and_invoices"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sales_and_invoices.object', {
#             'object': obj
#         })
