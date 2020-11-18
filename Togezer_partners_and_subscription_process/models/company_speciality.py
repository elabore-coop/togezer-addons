from odoo import models, fields, api
from odoo.tools.translate import _

class company_speciality(models.Model):
    _name = 'togezer.company_speciality'
    _description = "Company speciality"

    id = fields.Integer(
        string=_("ID"),
        required=False,
        translate=False,
        readonly=True
    )
    create_date = fields.Datetime(
        string=_("Created on"),
        required=False,
        translate=False,
        readonly=True
    )
    create_uid = fields.Many2one(
        string=_("Created by"),
        required=False,
        translate=False,
        readonly=True
    )
    write_date = fields.Datetime(
        string=_("Last Updated on"),
        required=False,
        translate=False,
        readonly=True
    )
    write_uid = fields.Many2one(
        string=_("Last Updated by"),
        required=False,
        translate=False,
        readonly=True
    )

    name = fields.Char(
        string=_("Name"),
        required=True,
        translate=False,
        readonly=False
    )