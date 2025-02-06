from odoo import models, fields

class Task(models.Model):
    _inherit = 'project.task'

    subtask_ids = fields.One2many('project.subtask', 'task_id', string='Subtareas')