# -*- coding: utf-8 -*-
{
    'name': "Database Auto-Backup to Amazon S3",
    'version': '12.0.1.0.0',
    "category": "Tools",
    "author": 'Andrii Semko | @andriisem',
    "website": "https://www.upwork.com/o/profiles/users/_~013175f63de76dd835/",
    'depends': ['base'],
    'data': [
        'data/ir_cron.xml',
        'security/ir.model.access.csv',
        'views/s3_backup_views.xml',
    ],
    'auto_install': False,
    'installable': True,
}
