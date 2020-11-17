# -*- coding: utf-8 -*-
import logging

from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo.http import request

_logger = logging.getLogger(__name__)

class AuthSignupHome(AuthSignupHome):

    def do_signup(self, qcontext):
        _logger.info('Local currency = {}'.format(qcontext.get('lcc')))
        if qcontext.get('lcc'):        
            """ Shared helper that creates a res.partner out of a token """
            # The only change compared to the parent function is the addition of the key "lcc"
            values = { key: qcontext.get(key) for key in ('login', 'name', 'password', 'lcc') } 
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