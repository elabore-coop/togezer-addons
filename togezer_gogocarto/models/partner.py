# -*- coding: utf-8 -*-
from odoo import fields, models
import pdb;

class Partner(models.Model):
    _inherit = 'res.partner'

    image_url = fields.Char('Image URL', compute='get_image_url')

    def get_image_url(self):        
        for partner in self:                
            attachment = self.env['ir.attachment'].search([('res_model','=','res.partner'), ('res_field','=', 'image_1920'), ('res_id','=',partner.id)])
            if attachment:
                base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
                partner.image_url = base_url + '/web/image/ir.attachment/%s/datas'%(attachment.id)
            else:
                partner.image_url = ''


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
                parser.append((field.name, ['id', 'name','website_short_description','biography','image_url']))
            elif field.name == 'x_pictures':
                parser.append((field.name, ['id', 'x_url']))
            elif field.name == 'x_touristic_tours':
                parser.append((field.name, ['id', 'x_name', 'x_url']))
            elif field.name == 'x_videos':
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
