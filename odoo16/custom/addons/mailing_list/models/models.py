# -*- coding: utf-8 -*-
import base64
import json, requests
from odoo import models, fields, api

URL_API = 'https://randomuser.me/api'


class MailingList(models.Model):
    _name = 'mailing_list.mailing_list'
    _description = 'mailing_list.mailing_list'

    name = fields.Char()
    gender = fields.Selection(
        [
            ('male', 'MALE'),
            ('female', 'FEMALE')
        ]
    )
    street = fields.Char()
    city = fields.Char()
    state = fields.Many2one('res.country.state', string="State")
    country = fields.Many2one('res.country', string="Country")
    zip = fields.Char()
    email = fields.Char()
    phone = fields.Char()
    image_1920 = fields.Image("Image")

    def convert_to_base64_image(self, img_url):
        response = requests.get(img_url)
        return base64.b64encode(response.content).decode('utf-8')

    @api.model
    def delete_empty_records(self):
        empty_records = self.search([('name', '=', False)])
        empty_records.unlink()
        return True

    def create_a_user(self):
        new_user = self.get_new_user_from_API()
        self.delete_empty_records()
        return super(MailingList, self).create(new_user)

    def create_a_multiple_users(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'mailing_list.model_create.multiple.users.wizard',
            'view_mode': 'form',
            'views': [(False, 'form')],
            'target': 'new',
            'context': {'default_mailing_mailing_id': self.id}
        }


    def clean_all_recs(self):
        all_users_list = self.search([])
        for i, obj in enumerate(all_users_list):
            obj.unlink()


    def get_new_user_from_API(self):
        '''
        get a json from api and save it into dict
        :return: Dict
        '''
        new_user_data = requests.get(URL_API).json()
        country_id = self.env['res.country'].search([('name', '=', new_user_data['results'][0]['location']['country'])]).id
        state_id = self.env['res.country.state'].search(
            [('name', '=', new_user_data['results'][0]['location']['state'])]).id
        picture_url = new_user_data['results'][0]['picture']['large']
        street = []
        picture_base64 = self.convert_to_base64_image(picture_url)

        for k, v in new_user_data['results'][0]['location']['street'].items():
            street.append(str(v))

        return {
            'gender': new_user_data['results'][0]['gender'],
            'name': '{} {} {}'.format(
                new_user_data['results'][0]['name']['title'],
                new_user_data['results'][0]['name']['first'],
                new_user_data['results'][0]['name']['last']
            ),
            'country': country_id,
            'state': state_id,
            'city': new_user_data['results'][0]['location']['city'],
            'street': ' '.join(street),
            'zip': new_user_data['results'][0]['location']['postcode'],
            'email': new_user_data['results'][0]['email'],
            'phone': new_user_data['results'][0]['phone'],
            'image_1920': picture_base64
        }
