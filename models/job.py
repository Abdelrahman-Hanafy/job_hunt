# -*- coding: utf-8 -*-

from odoo import models, fields, api


class job_hunt(models.Model):
    _name = 'job_hunt.job'
    _description = 'A model that represents a job'

    name = fields.Char(string='Position',required=True)
    company = fields.Char(string='Company',required=True)

    apply_date = fields.Date(string='Apply Date', defualt=fields.Date.today())
    postion_type = fields.Selection([
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('contract', 'Contract'),
        ('internship', 'Internship'),
    ], default='full_time')

    applied_at = fields.Selection([
        ('website', 'Website'),
        ('linkedin', 'Linkedin'),
        ('referral', 'Referral'),
        ('other', 'Other'),
    ], default='website')    

    remote = fields.Selection([
        ('remote', 'Remote'),
        ('onsite', 'Onsite'),
        ('hybrid', 'Hybrid'),
    ], default='onsite')

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
    ], default='wishlisted')


    ### Actions ###
    def action_apply(self):
        self.state = 'applied'

    def register_assissment(self):
        self.state = 'assissment'

    def register_interview(self):
        self.state = 'interview'

    def register_offer(self):
        self.state = 'offer'

    def action_decline(self):
        self.state = 'declined'

    def action_hire(self):
        self.state = 'hired'

    def action_rejecte(self):
        self.state = 'rejected'

    def action_ghost(self):
        self.state = 'ghosted'