from odoo import models, fields


class CreateMultipleUsersWizard(models.TransientModel):
    _name = 'mailing_list.model_create.multiple.users.wizard'
    _description = 'Description of the model'

    quantety = fields.Integer('Quantety', default=2)
    mailing_mailing_id = fields.Many2one('mailing_list.mailing_list')

    def btn_confirm_wizard(self):
        mailing_list = self.env['mailing_list.mailing_list']
        new_users_list = []
        counter = 0
        while counter < self.quantety:
            new_user = mailing_list.get_new_user_from_API()
            if not new_user in new_users_list:
                new_users_list.append(new_user)
                counter += 1
        mailing_list.create(new_users_list)
        mailing_list.delete_empty_records()