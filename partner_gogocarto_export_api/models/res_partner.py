from odoo import models, fields, api
from ast import literal_eval
from datetime import date, datetime
import logging
_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    """ Inherits partner, adds Gogocarto fields in the partner form, and functions"""
    _inherit = 'res.partner'

    in_gogocarto = fields.Boolean('In gogocarto')
    
    def _get_gogocarto_domain(self): # To OVERRIDE in sub_modules to customize the partner selection
        return [('in_gogocarto','=',True)]

    ############################################
    #region Public method for JSON Serialization
    ############################################
    def gogocarto_serialization(self):
        element = {}

        # mandatory fields in the export
        self._add_simple_node(element, "name")
        self._add_simple_node(element, "partner_longitude")
        self._add_simple_node(element, "partner_latitude")
        # To detect the changes in the exported data compared to the previous ones, so that Gogocarto does not compute all the data for each synchronization:
        self._add_computed_node(element, "write_date", self.write_date.strftime("%d-%m-%Y, %H:%M:%S"))

        export_fields = self._get_export_fields()
        for field in export_fields:
            if field.name in ["name", "partner_longitude", "partner_latitude", "write_date"]:
                continue # fields already added above            
            #######################################################################################
            # # ADD HERE new conditions in override method to customized the fields' value exported
            # elif condition1:
            #    self._add_simple_node(element, field.name)
            # elif condition2:
            #    self._add_computed_node(element, field.name, self._newmethod(field)
            #######################################################################################
            elif field.ttype in ["boolean", "char", "integer", "monetary", "text", "selection", "float"]:
                self._add_simple_node(element, field.name)
            elif field.ttype == "many2one":
                self._add_computed_node(element, field.name, self._get_field_value_name(field))
            elif field.ttype in ["one2many", "many2many"]:
                self._add_computed_node(element, field.name, self._get_field_many_values(field))
            elif field.ttype == "datetime":
                self._add_computed_node(element, field.name, self._get_field_datetime_value(field))
            elif field.ttype == "date":
                self._add_computed_node(element, field.name, self._get_field_date_value(field)) 
            elif field.ttype == "binary":
                continue # Not developped so far
                # IMPROVMENT PROPOSED:  export a public URL toward the bynary
            elif field.ttype == "html":
                continue # Not developped so far
            else:
                continue
        
        return element
    #endregion
        

    ############################################
    #region Private method to JSON Serialization
    ############################################

    def _get_export_fields(self):
        ICPSudo = self.env['ir.config_parameter'].sudo()
        export_field_ids = literal_eval(ICPSudo.get_param('gogocarto_export_api.export_gogocarto_fields'))
        export_fields = self.env['ir.model.fields'].search([('model_id', '=', 'res.partner'),('id','in', export_field_ids)])
        return export_fields

    # Method to add simple fields, for which there is no process needed
    def _add_simple_node(self, element, fieldName): 
        if getattr(self, fieldName):
            element[fieldName] = self[fieldName]
    
    # Method to add complex fileds, for which we need a dedicated method to get the value
    def _add_computed_node(self, element, fieldLabel, fieldStrValue):
        element[fieldLabel] = fieldStrValue

    # Method to get the name of the value registered in a Many2one field
    def _get_field_value_name(self, field):
        if getattr(self, field.name):
            return self[field.name].name
        else:
            return ''

    # Method to get the name of the values registered in a One2many or Many2many field
    def _get_field_many_values(self, field):
        values_list = ''
        for item in self[field.name] :
            if values_list != '':
                values_list = values_list + ', '
            values_list = values_list + item.name
        return values_list 
    

    # Method to get a datetime value in a string
    def _get_field_datetime_value(self, field):
        if getattr(self, field.name):
            return fields.Datetime.to_datetime(self[field.name]).strftime("%d-%m-%Y, %H:%M:%S")
        else:
            return ""

    # Method to get a date value in a string
    def _get_field_date_value(self, field):
        if getattr(self, field.name):
            return fields.Date.to_date(self[field.name]).strftime("%d-%m-%Y")
        else:
            return ""
    #endregion


    #################################################
    #region Public method to debug JSON Serialization
    #################################################
    def debug_field_exported(self):
        _logger.debug("List of field exported for gogoCarto:")
        for field in self._get_export_fields():
            _logger.debug(field.name)
    #endregion
