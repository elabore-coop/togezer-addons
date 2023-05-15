# -*- coding: utf-8 -*-
from odoo import fields, models

class Partner(models.Model):
    _inherit = 'res.partner'

    def _get_gogocarto_parser(self, company_id):
        parser = []
        for field in self._get_export_fields(company_id):
            if field.ttype in [
                    "boolean",
                    "char",
                    "integer",
                    "monetary",
                    "text",
                    "selection",
                    "float",
                    "date_time",
                    "date"]:
                parser.append(field.name)
            elif field.name == 'child_ids':
                parser.append((field.name, ['id', 'name','website_short_description','biography']))
            elif field.name == 'x_pictures':
                parser.append((field.name, ['id', 'x_url']))
            elif field.name == 'x_touristic_tours':
                parser.append((field.name, ['id', 'x_name', 'x_url']))
            elif field.ttype in ["many2one", "one2many", "many2many"]:
                parser.append((field.name, ['id', 'name']))
            elif field.ttype == "binary":
                continue
            elif field.ttype == "html":
                continue  # Not developped so far
            else:
                continue
        return parser
