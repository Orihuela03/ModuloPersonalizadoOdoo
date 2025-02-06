from odoo import models, fields, api

class Project(models.Model):
    _inherit = 'project.project'

    contracting_company_id = fields.Many2one('contracting.company', string='Empresa Contratadora')
    project_manager_id = fields.Many2one('res.users', string='Jefe de Proyecto')

    @api.model
    def create(self, vals):
        if self.env.user.has_group('custom_project_management.group_project_manager') or self.env.user.has_group('base.group_system'):
            return super(Project, self).create(vals)
        else:
            raise models.ValidationError("No tienes permisos para crear proyectos.")

    def write(self, vals):
        if self.env.user.has_group('custom_project_management.group_project_manager') or self.env.user.has_group('base.group_system'):
            return super(Project, self).write(vals)
        else:
            raise models.ValidationError("No tienes permisos para modificar este proyecto.")
