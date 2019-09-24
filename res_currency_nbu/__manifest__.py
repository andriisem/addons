# -*- coding: utf-8 -*-
{
    'name': "NBU rates parser",
    'description': """
Parse NBU rates and updated Odoo active currencies rates accordingly
=====================================================================
- API: https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json
    """,
    'category': 'Accounting',
    "author": 'Andrii Semko | @andriisem',
    "website": "https://www.upwork.com/o/profiles/users/_~013175f63de76dd835/",
    'version': '1.0',
    'depends': [
        'base',
        'account',
    ],

    'data': [
        'data/ir_cron.xml',
        'views/res_currency_view.xml'
    ],
}
