from odoo import models, fields, api


class QuantityUsersWizard(models.TransientModel):
    _name = 'create.few.users.wizard'
    _description = 'create.few.users.wizard'

    quantity = fields.Integer('Quantity', default=2)


    def confirm_button(self):
        print('---hello world FEW', self.quantity)
