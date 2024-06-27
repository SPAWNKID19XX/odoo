from odoo import models, fields, api

class CrmLead(models.Model):
    _inherit = 'crm.lead'
    _description = 'crm inherit add acquisition_agent field'

    acquisition_agent = fields.Many2one('res.partner',  string="Acquisition agent")