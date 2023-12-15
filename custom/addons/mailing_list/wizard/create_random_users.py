from odoo import models, fields, api


class CreateUsersWizard(models.TransientModel):
    _name = 'create.users.wizard'
    _description = 'create few users wizard'

    quantity = fields.Integer('Quantity', default=2)
    mailing_mailing_id = fields.Many2one('mailing.mailing')

    def confirm_button(self):
        user_number = 1
        list_users = self.env['mailing.mailing'].search([])
        mailing_mailing = self.env['mailing.mailing']
        print('Button has been confirmed. Quantity introduced is:', self.quantity)
        while user_number <= self.quantity:
            mailing_mailing = self.env['mailing.mailing']
            user = mailing_mailing.create_one_user()
            if user['name'] not in list_users:
                self.mailing_mailing_id = mailing_mailing.create(user)
                user_number += 1
        self.del_empty_recs()
        return mailing_mailing.open_last_user(self.mailing_mailing_id)

    def del_empty_recs(self):
        all_recs = self.env['mailing.mailing'].search([])
        for rec in all_recs:
            if not rec.name:
                rec.unlink()

