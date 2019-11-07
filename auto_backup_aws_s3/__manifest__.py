# -*- coding: utf-8 -*-
{
    'name': "Database Auto-Backup to S3",
    'version': '12.0.1.0.0',
    "category": "Tools",
    "description": """
Database Auto-Backup to S3
==========================
Documentation: https://andriisem.github.io/odoo-database-backup-to-s3/
    """,
    "author": 'Andrii Semko | @andriisem',
    "website": "https://andriisem.github.io/",
    'support': 'semko.andrey.i@gmail.com',
    'depends': ['base'],
    'data': [
        'data/ir_cron.xml',
        'security/ir.model.access.csv',
        'views/s3_backup_views.xml',
    ],
    'auto_install': False,
    'installable': True,
}
