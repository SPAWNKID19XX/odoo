# -*- coding: utf-8 -*-
# from servers import http


# class AcquisitionAgent(http.Controller):
#     @http.route('/acquisition_agent/acquisition_agent', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/acquisition_agent/acquisition_agent/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('acquisition_agent.listing', {
#             'root': '/acquisition_agent/acquisition_agent',
#             'objects': http.request.env['acquisition_agent.acquisition_agent'].search([]),
#         })

#     @http.route('/acquisition_agent/acquisition_agent/objects/<model("acquisition_agent.acquisition_agent"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('acquisition_agent.object', {
#             'object': obj
#         })
