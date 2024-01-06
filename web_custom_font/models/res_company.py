from odoo import fields, models

class ResCompany(models.Model):
    _inherit = 'res.company'

    font = fields.Selection(selection_add=[('Lemon', 'Lemon')])
