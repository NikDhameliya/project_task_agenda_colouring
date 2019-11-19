# -*- coding: utf-8 -*-


from odoo import api, fields, models



class ProjectTask(models.Model):
    _inherit = 'project.task'

    agenda_status = fields.Many2one(
        'agenda.status',
        'Agenda status'
    )
    hex_value = fields.Char(
        string="Hex Value",
        related="agenda_status.color",
        store=False,
        size=7
    )