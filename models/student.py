# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Student(models.Model):

    _name = 'xh.student'
    #name = fields.Char(string='学生姓名', required=True)
    name = fields.Many2one('res.users', string='学生姓名')



class StudentResUsers(models.Model):
    _inherit = 'res.users'
    #stype = fields.Char(string='类型', required=True)
    @api.model
    def create(self, vals):

        record = super(StudentResUsers, self).create(vals)
        #if record['stype'] == '学生':
        self.env['xh.student'].create({
            'name': int(record['id'])
        })
        return record

