# -*- coding: utf-8 -*-
{
    'name': "acquisition_agent",
    'license': 'LGPL-3',

    'summary': """
        crm.lead, invoices and sailes wil contain a field acquisition_agent""",

    'description': """
        Both sales already have a field for the salesperson; however, none of them have a field to identify the "acquisition agent," that is, the person who referred the opportunity.

You are asked to create a contact field in opportunities, sales, and invoices.

The value of this field should be passed from the opportunity to the sale, and from the sale to the invoice.

(In other words, if you create a sale from the opportunity, the sale should inherit the same acquisition agent as the lead, and when creating an invoice from the sale, the invoice should inherit the same value as the sale.)

This field should appear in the form view below the salesperson field.

In sales and invoices, the field should only be editable if the document is in the "draft" state (see examples from Odoo, using the "states" parameter on fields).

This field should also appear in the print of the quotations near the salesperson field.
    """,

    'author': "BorisIsac(OdooDeveloper)",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales/CRM',
    'version': '16.0.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'crm', 'account', 'sale_management'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/sale_order_inherit.xml',
        'views/crm_inherit.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
