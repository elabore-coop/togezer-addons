# Copyright 2020 Elabore ()
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'togezer_gogocarto',
    'version': '13.0.1.0.10',
    'author': 'Elabore',
    'maintainer': 'False',
    'website': 'https://elabore.coop',
    'license': '',
    'category': 'False',
    'summary': 'Customization of gogocarto API for Togezer - https://togezer.travel',
    'description': """
.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3
=========================================
Togezer Gogocarto
=========================================
Customization of gogocarto API for Togezer

Installation
============
Just install togezer_gogocarto, all dependencies will be installed by default.

Known issues / Roadmap
======================


Credits
=======

Images
------
* Elabore: `Icon <https://elabore.coop/web/image/res.company/1/logo?unique=de95b2e>`_.

Contributors
------------
* Clément Thomas
* Elabore Teams

Funders
-------
The development of this module has been financially supported by:
* Elabore (https://elabore.coop)
* TogeZer (https://togezer.travel)

Maintainer
----------
This module is maintained by ELABORE.
Elabore is a cooperative corporation whose mission is to support the collaborative development of Odoo features and ecosystem for social and solidarity-based economy Organizations.
""",

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'partner_gogocarto_export_api'
    ],
    'external_dependencies': {
        'python': [],
    },

    # always loaded
    'data': [
    ],

    # only loaded in demonstration mode
    'demo': [
    ],

    'js': [],
    'css': [],
    'qweb': [],

    'installable': True,
    # Install this module automatically if all dependency have been previously
    # and independently installed.  Used for synergetic or glue modules.
    'auto_install': False,
    'application': False,
}