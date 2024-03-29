# -*- coding: utf-8 -*-

from odoo import models, fields, api


class GymExpansion(models.Model):
    _name = 'gym_expansion.materiales'
    _description = 'Materiales Gym Alquiler'

    name = fields.Char(string='Nombre', required=True, help='Nombre del material')
    quantity = fields.Integer(string='unidades disponibles')
    
    material_type = fields.Selection(
        string='Tipo de Material',
        selection=[('clothes', 'Ropa'), ('instrument', 'Instrumentos'), ('space', 'Sala'), ],
        default='clothes'
    )
    
    user_ids = fields.Many2many(
        string='Usuarios confirmados',
        comodel_name='gym.users'
    )
    
    classe_ids = fields.Many2many(
        string='Clases confirmadas',
        comodel_name='gym.classes'
    )