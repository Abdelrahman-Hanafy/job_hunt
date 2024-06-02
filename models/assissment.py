from odoo import models, fields, api

class Assissment(models.Model):
    _name = 'job_hunt.assissment'
    _description = 'A model that represents an assissment'

    name = fields.Char(string='Name', compute='_compute_name', store=True)
    description = fields.Text(string='Description')
    
    recived_date = fields.Date(string='Recived Date')
    deadline = fields.Date(string='Deadline')

    assissment_type = fields.Selection([
        ('task', 'Task'),
        ('problem_solving', 'Problem Solving'),
        ('test', 'Test'),
        ('competition', 'Competition'),
        ('other', 'Other'),
    ], string='Type')

    is_done = fields.Boolean(string='Is Done', default=False)
    job_id = fields.Many2one('job_hunt.job', string='Job')

    ### compute ###
    @api.depends('assissment_type', 'job_id')
    def _compute_name(self):
        for rec in self:
            rec.name = f'{rec.assissment_type} for {rec.job_id.name}'
