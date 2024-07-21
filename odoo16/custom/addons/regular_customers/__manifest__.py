# -*- coding: utf-8 -*-
{
    'name': "regular_customers",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
    For the articles, have a listing for the "regular customers" where we can place the reference and name 
    that the customer uses for that article.

    Each article can have multiple "regular customers."

    Each customer can be associated with multiple articles.

    Each customer can have a different reference and name for each article, for example: The article [ABC] Article, 
    for customer Jorge, can be [001] Product and for customer Armando, it can be [QWERTY] sardine.

    In sales and invoices, when adding a new article, if the sale/invoice is for a regular customer of that article, 
    it should use those values instead of the "normal" ones.

    Both in sales and invoices, these values should be loaded when editing/adding articles 
    to the document or when changing the partner of that document.

EXTRA:

    Add a new field to the articles to specify the countries where the article is sold. For now, this field should be informative only, 
    not affecting the normal functionality of Odoo.

    This field should be visible in both the templates and the variants.

    If a template has multiple variants, it should display all the countries present in its variants.

    When adding a new country to the template, it should be added to all the variants as well, 
    and the same should happen when it is removed.

    When adding a new country to the variant, it should only be added to the variant being edited, not to the others.

    Tip: Computed fields can have the "inverse" parameter.
    """,

    'author': "Boris Isac(ODOO DEVELOPER)",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales/CRM',
    'version': '16.0.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'crm'],

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
