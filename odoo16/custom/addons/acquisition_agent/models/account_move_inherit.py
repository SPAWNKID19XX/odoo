from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'
    _description = 'account.move.inherit'

    acquisition_agent = fields.Many2one(
        'res.users',
        string="Acquisition Agent",
        states={
            'draft': [('readonly', False)],
            'cancel': [('readonly', True)]
        }
    )


