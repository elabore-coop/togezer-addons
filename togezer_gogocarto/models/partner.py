# -*- coding: utf-8 -*-
from odoo import fields, models

class Partner(models.Model):
    _inherit = 'res.partner'

    def _get_gogocarto_parser(self, company_id):
        parser = super(Partner,self)._get_gogocarto_parser(company_id)
        for field in parser:
            if type(field) is tuple and field[0] == 'child_ids':
                field[1].append('website_short_description')
        return parser