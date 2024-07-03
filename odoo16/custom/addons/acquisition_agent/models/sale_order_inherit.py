from odoo import models, fields, api

class Sales(models.Model):
    _inherit = 'sale.order'
    _description = 'sale order inherit add acquisition_agent field'

    acquisition_agent = fields.Many2one(
        'res.partner',
        string="Acquisition Agent",
        states={
            'draft': [('readonly', False)],
            'sent': [('readonly', False)],
            'sale': [('readonly', True)],
            'done': [('readonly', True)],
            'cancel': [('readonly', True)]
        }
    )

    @api.model
    def default_get(self, fields_list):
        res = super(Sales, self).default_get(fields_list)
        if self.env.context.get('default_acquisition_agent'):
            res['acquisition_agent'] = self.env.context['default_acquisition_agent']
        return res

    def create_invoices(self, grouped=False, final=False, date=None):
        res = super(Sales, self)._create_invoices(grouped=grouped, final=final, date=date)
        for invoice in res:
            invoice.acquisition_agent = self.acquisition_agent
        return invoice

    def _prepare_invoice(self):
        invoice_vals = super(Sales, self)._prepare_invoice()
        invoice_vals['acquisition_agent'] = self.acquisition_agent.id
        return invoice_vals