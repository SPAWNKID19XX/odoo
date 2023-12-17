from odoo import models, fields, api, _


class InheritSaleOrder(models.Model):
    _inherit = 'crm.lead'

    acquisition_agent = fields.Many2one('res.partner', string="Acquisition Agent")