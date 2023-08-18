# -*- coding: utf-8 -*-
from odoo import fields, models, api
import pdb;

class IrAttachment(models.Model):
    _inherit = 'ir.attachment'

    @api.model_create_multi
    def create(self, vals_list):        
        for val_list in vals_list:
            if val_list['res_model'] == 'res.partner':
                val_list['public'] = True
        return super().create(vals_list)