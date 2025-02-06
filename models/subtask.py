from odoo import models, fields

class Subtask(models.Model):
    _name = 'project.subtask'
    _description = 'Subtarea'

    name = fields.Char(string='Nombre', required=True)
    description = fields.Text(string='Descripción')
    task_id = fields.Many2one('project.task', string='Tarea Relacionada')