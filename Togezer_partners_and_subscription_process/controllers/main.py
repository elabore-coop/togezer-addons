# -*- coding: utf-8 -*-
import logging

from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo.http import request

_logger = logging.getLogger(__name__)

class AuthSignupHome(AuthSignupHome):

    def do_signup(self, qcontext):
        _logger.info('Firstname = {}'.format(qcontext.get('firstname')))
        _logger.info('Phone = {}'.format(qcontext.get('phone')))
        _logger.info('Whatsapp = {}'.format(qcontext.get('whatsapp')))
        _logger.info('Skype = {}'.format(qcontext.get('skype')))
        _logger.info('My company = {}'.format(qcontext.get('my_company')))
        _logger.info('Function = {}'.format(qcontext.get('function')))
        _logger.info('Website = {}'.format(qcontext.get('website')))
        _logger.info('Street = {}'.format(qcontext.get('street')))
        _logger.info('Zip = {}'.format(qcontext.get('zip')))
        _logger.info('City = {}'.format(qcontext.get('city')))        
        _logger.info('Country ID = {}'.format(qcontext.get('country_id')))
        _logger.info('Biography = {}'.format(qcontext.get('biography')))
        _logger.info('Terms of use agreed = {}'.format(qcontext.get('terms_of_use_agreed')))
        if qcontext.get('phone') or qcontext.get('whatsapp') or qcontext.get('skype') or qcontext.get('my_company') or qcontext.get('website') or qcontext.get('biography') or qcontext.get('terms_of_use_agreed') or qcontext.get('firstname') or qcontext.get('street') or qcontext.get('zip') or qcontext.get('city') or qcontext.get('function') or qcontext.get('country_id') :
            """ Shared helper that creates a res.partner out of a token """
            # The only change compared to the parent function is the addition of the keys of thenew fields
            values = { key: qcontext.get(key) for key in ('login', 'name', 'password', 'phone', 'whatsapp', 'skype', 'my_company',
                                                          'website', 'biography', 'terms_of_use_agreed', 'street', 'zip', 'city', 'country_id',
                                                          'firstname', 'function') } 
            if not values:
                raise UserError(_("The form was not properly filled in."))
            if values.get('password') != qcontext.get('confirm_password'):
                raise UserError(_("Passwords do not match; please retype them."))
            supported_lang_codes = [code for code, _ in request.env['res.lang'].get_installed()]
            lang = request.context.get('lang', '').split('_')[0]
            if lang in supported_lang_codes:
                values['lang'] = lang
            self._signup_with_values(qcontext.get('token'), values)
            request.env.cr.commit()
        else:
            super(AuthSignupHome, self).do_signup(qcontext)