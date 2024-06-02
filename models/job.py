# -*- coding: utf-8 -*-

from odoo import models, fields, api


class job_hunt(models.Model):
    _name = 'job_hunt.job'
    _description = 'A model that represents a job'

    name = fields.Char(string='Position',required=True)
    company = fields.Char(string='Company',required=True)

    apply_date = fields.Date(string='Apply Date')
    postion_type = fields.Selection([
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('contract', 'Contract'),
        ('internship', 'Internship'),
    ])

    applied_at = fields.Selection([
        ('website', 'Website'),
        ('linkedin', 'Linkedin'),
        ('referral', 'Referral'),
        ('other', 'Other'),
    ])    

    remote = fields.Selection([
        ('remote', 'Remote'),
        ('onsite', 'Onsite'),
        ('hybrid', 'Hybrid'),
    ])

    state = fields.Selection([
        ('wishlisted', 'Wishlisted'),
        ('applied', 'Applied'),
        ('assissment', 'Assessment'),
        ('interview', 'Interview'),
        ('offer', 'Offer'),
        ('rejected', 'Rejected'),
        ('hired', 'Hired'),
        ('declined', 'Declined'),
        ('ghosted', 'Ghosted'),
    ])
