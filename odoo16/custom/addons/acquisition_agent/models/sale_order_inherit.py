from odoo import models, fields, api

class Sales(models.Model):
    _inherit = 'sale.order'
    _description = 'sale order inherit add acquisition_agent field'

    acquisition_agent = fields.Many2one('res.partner',  string="Acquisition agent")