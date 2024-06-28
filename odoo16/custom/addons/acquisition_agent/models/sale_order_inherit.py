from odoo import models, fields, api

class Sales(models.Model):
    _inherit = 'sale.order'
    _description = 'sale order inherit add acquisition_agent field'

    acquisition_agent = fields.Many2one('res.partner',  string="Acquisition agent")

    @api.model
    def default_get(self, fields_list):
        res = super(Sales, self).default_get(fields_list)
        if self.env.context.get('default_acquisition_agent'):
            res['acquisition_agent'] = self.env.context['default_acquisition_agent']
            self.acquisition_agent = res['acquisition_agent']
        return res