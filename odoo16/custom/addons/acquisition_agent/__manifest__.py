# -*- coding: utf-8 -*-
{
    'name': "acquisition_agent",
    'license': 'LGPL-3',

    'summary': """
        crm.lead, invoices and sailes wil contain a field acquisition_agent""",

    'description': """
        Both sales already have a field for the salesperson; however, none of them have a field to identify 
        the "acquisition agent," that is, the person who referred the opportunity.
        You are asked to create a contact field in opportunities, sales, and invoices.
        The value of this field should be passed from the opportunity to the sale, and from the sale to the invoice.
        (In other words, if you create a sale from the opportunity, the sale should inherit the same acquisition agent 
        as the lead, and when creating an invoice from the sale, the invoice should inherit the same value as the sale.)
        This field should appear in the form view below the salesperson field.
        In sales and invoices, the field should only be editable if the document is in the "draft" state 
        (see examples from Odoo, using the "states" parameter on fields).
        This field should also appear in the print of the quotations near the salesperson field.
        
        Tanto as vendas já têm um campo para o vendedor, no entanto nenhum deles tem um campo para identificar o 
        "angariador"(acquisition agent) ou seja a pessoa que referenciou a oportunidade.
        É então pedido que seja criado um campo de contacto nas oportunidades, vendas e faturas.
        O valor deste campo deve ser passado da oportunidade para a venda, e de venda para a fatura
        (Ou seja se criar uma venda apartir da oportunidade, a venda deve assumir o mesmo angariador que a lead, 
        e ao criar uma fatura a partir da venda, a fatura deve assumir o mesmo valor que a venda)
        Este campo deve aparecer na vista de formulário a baixo do campo do vendedor
        Nas vendas e faturas o campo só deve poder ser editado se o documento estiver no estado "draft" 
        (verem exemplos da odoo, quando usam o parâmetro "states" nos campos)
        Este campo deve também aparecer no print dos orçamentos perto do campo do vendedor
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
        'views/crm_inherit.xml',
        'views/account_move_inherit.xml',
        'views/report_invoice_document_inherit.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
