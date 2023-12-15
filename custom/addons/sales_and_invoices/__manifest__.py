# -*- coding: utf-8 -*-
{
    'name': "sales_and_invoices",
    'license': 'LGPL-3',

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        I request the creation of a contact field in opportunities, sales, and invoices.

        The value of this field should be passed from the opportunity to the sale and from the sale to the invoice.

        (In other words, if a sale is created from the opportunity, the sale should assume the same contact as the lead, and when creating an invoice from the sale, the invoice should assume the same contact as the sale.)

        This field should appear in the form view below the salesperson field.

        In sales and invoices, the field should only be editable if the document is in the "draft" state (similar to Odoo's examples when using the "states" parameter in fields).

        This field should also appear in the quotation printout next to the salesperson field.
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management', 'account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
