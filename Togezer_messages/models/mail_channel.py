# -*- coding: utf-8 -*-
from odoo import fields, models, api

class Channel(models.Model):
    _name = 'mail.channel'
    _inherit = ['mail.channel']

    channel_partner_ids = fields.Many2many( 'res.partner', 
                                            'mail_channel_partner', 
                                            'channel_id', 'partner_id', 
                                            string='Listeners', 
                                            depends=['channel_last_seen_partner_ids'],
                                            domain=[('is_company','=',False),('user_ids','!=',False)])