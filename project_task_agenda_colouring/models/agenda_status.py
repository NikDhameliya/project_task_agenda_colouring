# -*- coding: utf-8 -*-


from odoo import api, fields, models


class AgendaStatus(models.Model):
    _name = 'agenda.status'
 
    name = fields.Char(
        String='Description'
    )
    color = fields.Char(
        string="Color",
        help="Choose your color",
        size=7
    )