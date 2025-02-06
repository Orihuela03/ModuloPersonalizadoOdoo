from odoo import models, fields

class ContractingCompany(models.Model):
    _name = 'contracting.company'
    _description = 'Empresa Contratadora'

    name = fields.Char(string='Nombre', required=True)
    address = fields.Char(string='Dirección')
    contact = fields.Char(string='Contacto')
    project_ids = fields.One2many('project.project', 'contracting_company_id', string='Proyectos')
