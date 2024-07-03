from odoo import models, fields, api

class CrmLead(models.Model):
    _inherit = 'crm.lead'
    _description = 'crm inherit add acquisition_agent field'

    acquisition_agent = fields.Many2one(
        'res.partner',
        string="Acquisition agent"
    )

    def action_new_quotation(self):
        res = super(CrmLead, self).action_new_quotation()
        if isinstance(res, dict) and res.get('context'):
            res['context']['default_acquisition_agent'] = self.acquisition_agent.id
        return res