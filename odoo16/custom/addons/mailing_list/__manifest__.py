# -*- coding: utf-8 -*-
{
    'name': "mailing_list",
    'license': 'LGPL-3',

    'summary': """
        App witch will receve rendom users from api""",

    'description': """
        app can create 1 user, multiple users and remove all users in 1 click
    """,

    'author': "Boris Isac(ODOO DEVELOPER)",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Human Resources/Employees',
    'version': '16.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        #data views

        #wizard views
        'wizard/mailing_list_quantity_wizard.xml',

        'views/views.xml',
        'views/templates.xml',
        #my views
        'views/mailing_list.xml'

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
