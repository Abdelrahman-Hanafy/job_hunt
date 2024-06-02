from odoo import models, fields

class Assissment(models.Model):
    _name = 'job_hunt.assissment'
    _description = 'A model that represents an assissment'

    name = fields.Char(string='Name')
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

    job_id = fields.Many2one('job_hunt.job', string='Job')
