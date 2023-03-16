# Copyright 2023 Elabore ()
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields

class res_partner(models.Model):
    _inherit = "res.partner"

    search_partner = fields.Boolean('Search Partner')
    banner_image = fields.Binary('Banner Image')