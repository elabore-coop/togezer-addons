# -*- coding: utf-8 -*-
from werkzeug import urls
from odoo import fields, models, api
from odoo.addons.http_routing.models.ir_http import slug

class SaleOrderTemplate(models.Model):
    _inherit = "sale.order.template"

    website_url = fields.Char(
        'Website URL', compute='_compute_website_url')

    @api.depends('name')
    def _compute_website_url(self):
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')      
        for record in self:
            package_path = '/package/details/%s' % slug(record)
            record.website_url = urls.url_join(base_url, package_path)