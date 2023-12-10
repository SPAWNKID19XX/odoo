# -*- coding: utf-8 -*-
import base64
import json

import requests
from odoo import models, fields, api, _


class MailingList(models.Model):
    _name = 'mailing.mailing'
    _description = 'mailing.mailing'

    gender = fields.Selection(
        [
            ('male', 'Male'),
            ('female', 'Female'),
        ],
        string="Gender"
    )
    name = fields.Char(string="Name")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    picture = fields.Image("Image")
    country = fields.Many2one(comodel_name='res.country', string='Country')
    state = fields.Many2one(comodel_name='res.country.state', string='State', domain="[('country_id', '=?', country)]")
    city = fields.Char(string="City")
    street = fields.Char(string="Street")
    postcode = fields.Char(string="Postcode")

    API_LINK = 'https://randomuser.me/api'

    def create_user(self):
        json_data = requests.get(self.API_LINK).json()
        picture_url = json_data['results'][0]['picture']['large']
        decoded_img = base64.b64encode(requests.get(picture_url).content)
        state = self.env['res.country.state'].search([('name', '=', json_data['results'][0]['location']['state'])])
        country = self.env['res.country'].search([('name', '=', json_data['results'][0]['location']['country'])])
        context = {
            'gender': json_data['results'][0]['gender'],
            'name': json_data['results'][0]['name']['first'] + ' ' + json_data['results'][0]['name']['last'],
            'email': json_data['results'][0]['email'],
            'phone': json_data['results'][0]['phone'],
            'picture': decoded_img,
            'street': json_data['results'][0]['location']['street']['name'] + ' ' + str(
                json_data['results'][0]['location']['street']['number']),
            'city': json_data['results'][0]['location']['city'],
            'state': state.id,
            'country': country.id,
            'postcode': json_data['results'][0]['location']['postcode']
        }
        return context

    def create_one_user(self):
        user = self.create_user()
        if user['name']:
            self.write(user)
        else:
            self.create(user)
        return user

    def call_wizard_quantity(self):
        print('CALL WIZARD')
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'create.users.wizard',
            'view_mode': 'form',
            'views': [(False, 'form')],
            'target': 'new',
            'context': {'default_mailing_mailing_id': self.id}
        }

    def open_last_user(self, user):
        return {
            'type': 'ir.actions.act_window',
            'res_id': user.id,
            'res_model': 'mailing.mailing',
            "views": [[False, "form"]],
        }
