# -*- coding: utf-8 -*-
# from servers import http


# class MailingList(http.Controller):
#     @http.route('/mailing_list/mailing_list', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mailing_list/mailing_list/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mailing_list.listing', {
#             'root': '/mailing_list/mailing_list',
#             'objects': http.request.env['mailing_list.mailing_list'].search([]),
#         })

#     @http.route('/mailing_list/mailing_list/objects/<model("mailing_list.mailing_list"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mailing_list.object', {
#             'object': obj
#         })
