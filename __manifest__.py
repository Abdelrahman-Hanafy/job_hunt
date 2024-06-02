# -*- coding: utf-8 -*-
{
    'name': "Job Hunt",

    'summary': "Personal App to keep track of jobs",

    'author': "Abdelrahman M Hanafy",
    'website': "https://www.linkedin.com/in/abdelrahman-hanafy/",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',

        'views/job_views.xml',
        'views/menu.xml',

    ],

    'application': True,
    'installable': True,
}

