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
    street = fields.Char(string="Street")
    city = fields.Char(string="City")
    state = fields.Char(string="State")
    country = fields.Char(string="Country")
    postcode = fields.Char(string="Postcode")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    picture = fields.Image()

    API_LINK = 'https://randomuser.me/api'

    def create_user(self):
        print('---hello world ONE')
        json_data = requests.get(self.API_LINK).json()

        print('+++', json_data)
        print('---', json_data['results'][0])

        self.email = json_data['results'][0]['email']
        self.gender = json_data['results'][0]['gender']
        self.name = json_data['results'][0]['name']['first'] + ' ' + json_data['results'][0]['name']['last']
        self.phone = json_data['results'][0]['phone']
        self.picture = json_data['results'][0]['picture']['large']

    def create_few_user(self):
        print('---hello world FEW')
