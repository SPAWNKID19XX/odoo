# -*- coding: utf-8 -*-
{
    'name': "mailing_list",
    'license': 'LGPL-3',

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
A aplicação deve cumprir os seguintes pontos:

1.1 Deve criar uma Mailing List própria de nome “NOVOS CONTATOS 2023”

1.2 Devem criar contatos que fiquem associados a esta lista de contatos.

1.3 O form de contatos deve conter os seguintes dados (usar campos existentes e criar os necessários):

    gender,name,street,city,state,country,postcode,email,phone,picture (deve mostrar a imagem)

  1.4 os dados são retirados da seguinte API - https://randomuser.me/api 

  1.5 deve existir um botão wizard que define o número de contactos que quero importar (ex. carrego no botão, indico o número de contactos que quero, faço um pedido à API e crio esse número de contatos) (usar multiple request ver docs api)

  1.6 Não pode haver contactos duplicados

  1.7 Criar um botão para eliminar os contactos todos dessa lista 
""",

    'author': "Boris Isac",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Contacts',
    'version': '16.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/create_random_users_view.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/mailing.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
