{
    'name': "Togezer_partner_gogocarto_export_api",
    'summary': """ HTTP JSON api to send data for Gogocarto import """,
    'license': 'AGPL-3'
    'description': """
================================
Togezer_partner_gogocarto_export_api
================================

Togezer Gogocarto connection module, to communicate the Odoo partner data needed for a Togezer' Gogocarto map

This module allow the users to decide:

* the partner to be exported
* the fields exported for each partner (*name*, *partner_longitude*, *partner_lattitude* and *write_date* automatically exported)

Installation
============

Just install partner_gogocarto_export_api, all dependencies will be installed by default.

To export partners data:

#. Set the fields you want to export in Settings / Gogocarto.
#. Check the field *"In Gogocarto"* in the partner form view.

And use the link *https://yourodoo.com/web/get_http_gogocarto_elements* in Gogocarto server import configuration (*https://video.colibris-outilslibres.org/videos/watch/c74fc469-c822-4ab8-82a7-a2555e49e576*)

Known issues / Roadmap
======================

Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/elabore-coop/Togezer-Special-Module/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smashing it by providing a detailed and welcomed feedback.

Credits
=======

Images
------

* Elabore: `Icon <https://elabore.coop/web/image/res.company/1/logo?unique=de95b2e>`_.

Contributors
------------

* Stéphan SAINLEGER <https://github.com/stephansainleger>
* Elabore Teams

Funders
-------

The development of this module has been financially supported by:

* Elabore (https://elabore.coop)
* Togezer (https://togezer.travel)

Maintainer
----------

This module is maintained by ELABORE.

This module is maintained by ELABORE.
Elabore is a cooperative corporation whose mission is to support the collaborative development of Odoo features and ecosystem for social and solidarity-based economy Organizations.

""",

    'author': "Elabore",
    'website': "https://elabore.coop",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Localization',
    'version': '13.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'partner_gogocarto_export_api',
                'Togezer_partners_and_subscription_process'
            ],

    # always loaded
    'data': [],
    # only loaded in demonstration mode
    'demo': [],
}
