from odoo import models, fields

class ProjectProject(models.Model):
    _inherit = 'project.project'

    contracting_company_id = fields.Many2one('res.partner', string='Contracting Company')