# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Exam(models.Model):

    _name = 'xh.exam'
    stu_name = fields.Many2one('res.users', string='学生姓名', ondelete='cascade')
    subject = fields.Char(string="科目", required=True)
    score = fields.Integer(string="分数", required=False)
    t_name = fields.Many2one('xh.teacher', string='老师姓名')