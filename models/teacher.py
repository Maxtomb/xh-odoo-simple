# -*- coding: utf-8 -*-
from odoo import fields, models


class Teacher(models.Model):

    _name = 'xh.teacher'
    name = fields.Many2one('res.users', string='老师姓名')