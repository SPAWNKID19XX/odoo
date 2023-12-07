# -*- coding: utf-8 -*-
import base64
import json

import requests
from odoo import models, fields, api


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

    street = fields.Char(string="Street")
    city = fields.Char(string="City")
    state = fields.Char(string="State")
    country = fields.Char(string="Country")
    postcode = fields.Char(string="Postcode")

    API_LINK = 'https://randomuser.me/api'

    def create_user(self):
        json_data = requests.get(self.API_LINK).json()
        picture_url = json_data['results'][0]['picture']['large']
        decoded_img = base64.b64encode(requests.get(picture_url).content)
        context = {
            'gender': json_data['results'][0]['gender'],
            'name': json_data['results'][0]['name']['first'] + ' ' + json_data['results'][0]['name']['last'],
            'email': json_data['results'][0]['email'],
            'phone': json_data['results'][0]['phone'],
            'picture': decoded_img,
            'street': json_data['results'][0]['location']['street']['name'] + ' ' + str(
                json_data['results'][0]['location']['street']['number']),
            'city': json_data['results'][0]['location']['city'],
            'state': json_data['results'][0]['location']['state'],
            'country': json_data['results'][0]['location']['country'],
            'postcode': json_data['results'][0]['location']['postcode']
        }

        return context

    def create_one_user(self):
        print('---hello world ONE')
        user = self.create_user()
        if user['name']:
            self.write(user)
        else:
            self.create(user)

    def create_few_user(self):
        print('---hello world FEW')
