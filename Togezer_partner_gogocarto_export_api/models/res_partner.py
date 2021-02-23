from odoo import models, fields, api
from ast import literal_eval


class ResPartner(models.Model):
    """ Inherits partner and adds Tasks information in the partner form """
    _inherit = 'res.partner'
    
    def _get_gogocarto_domain(self):
        return [('in_gogocarto','=',True),('is_company','=', True)
                ,('membership_state','in',['paid', 'free'])
                ,('partner_longitude', '!=', float())
                ,('partner_latitude', '!=', float())
                ]

    def _get_team_id_label(self):
        if self.team_id:
            return self.team_id.name
        else:
            return ''

    def _get_company_category(self):
        categories_list = ''
        for category in self.company_category :
            if categories_list != '':
                categories_list = categories_list + ', '
            categories_list = categories_list + category.name
        return categories_list 

    def _get_company_speciality(self):
        specialities_list = ''
        for speciality in self.company_speciality :
            if specialities_list != '':
                specialities_list = specialities_list + ', '
            specialities_list = specialities_list + speciality.name
        return specialities_list 

    def _get_spoken_languages(self):
        languages_list = ''
        for language in self.spoken_languages :
            if languages_list != '':
                languages_list = languages_list + ', '
            languages_list = languages_list + language.name
        return languages_list 


    #region Public method for JSON Serialization
    def add_fields(self, element, export_fields):
        for field in export_fields:
            if field.name == "team_id":
                self.__add_computed_node(element, "team_id", self._get_team_id_label)
            elif field.name == "company_category":
                self.__add_computed_node(element,"company_category", self._get_itinerant_label)
            elif field.name == "company_speciality":
                self.__add_computed_node(element,"company_speciality", self._get_exchange_counter_label)
            elif field.name == "spoken_languages":
                self.__add_computed_node(element, "spoken_languages", self._get_team_id_label)
            elif field.name == "industry_id":
                self.__add_computed_node(element, "industry_id", self._get_industry_id_label)
            elif field.name == "category_id":
                self._add_computed_node(element, "category_id", self._get_category_id)
            else:
                self.__add_simple_node(element, field.name)
        return element
    #endregion