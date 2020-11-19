# -*- coding: utf-8 -*-
from odoo import fields, models

class Partner(models.Model):
    _inherit = 'res.partner'

    biography = fields.Text(
        string="My biography",
        required=False,
        translate=False,
        readonly=False
    )

    whatsapp = fields.Char(
        string="Whatsapp",
        required=False,
        translate=False,
        readonly=False
    )

    skype = fields.Char(
        string="Skype",
        required=False,
        translate=False,
        readonly=False
    )

    spoken_languages = fields.Many2many(
        'res.lang',
        string="Spoken languages",
        readonly=False
    )

    company_category = fields.Many2many(
        'togezer.company_category',
        string="Company categories",
        required=False,
        readonly=False
    )

    company_speciality = fields.Many2many(
        'togezer.company_speciality',
        string="Company specialities",
        required=False,
        readonly=False
    )

    continent = fields.Many2many(
        'togezer.continent',
        string="Continents",
        required=False,
        readonly=False
    )

    opening_hours = fields.Text(
        string="Opening hours",
        required=False,
        translate=False,
        readonly=False
    )

    historic = fields.Text(
        string="Compagny historic",
        required=False,
        translate=False,
        readonly=False
    )

    my_company = fields.Char(
        string="My company",
        required=False,
        translate=False,
        readonly=False 
    )

    tourism_licence = fields.Char(
        string="Tourism licence",
        required=False,
        translate=False,
        readonly=False
    )

    terms_of_use_agreed = fields.Boolean(
        string="Terms of use agreed",
        required=True,
        readonly=True
    )

    