# -*- coding: utf-8 -*-
import logging

from odoo.addons.account.controllers.portal import PortalAccount

_logger = logging.getLogger(__name__)

class PortalAccount(PortalAccount):

    def details_form_validate(self, data):
        self.OPTIONAL_BILLING_FIELDS.append("lcc")
        _logger.info('data = {}'.format(data))
        _logger.info('OPTIONAL_BILLING_FIELDS = {}'.format(self.OPTIONAL_BILLING_FIELDS))
        return super(PortalAccount, self).details_form_validate(data)