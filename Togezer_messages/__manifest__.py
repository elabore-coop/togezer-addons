# Copyright 2020 Elabore ()
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'togezer_messages',
    'version': '13.0.1.0.10',
    'author': 'Elabore',
    'maintainer': 'False',
    'website': 'https://elabore.coop',
    'license': '',
    'category': 'False',
    'summary': 'Customization of togezer.travel mail modules - https://togezer.travel',
    'description': """
.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3
================
Togezer Messages
================
The module's goal is to customize Togezer message functionnalities.

Installation
============
Just install togezer_messages, all dependencies will be installed by default.

Known issues / Roadmap
======================

Bug Tracker
===========
Bugs are tracked on `GitHub Issues
<https://github.com/stephansainleger/Togezer-Special-Module/issues>`_. In case of trouble, please
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
* TogeZer (https://togezer.travel)

Maintainer
----------
This module is maintained by ELABORE.
Elabore is a cooperative corporation whose mission is to support the collaborative development of Odoo features and ecosystem for social and solidarity-based economy Organizations.
""",

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'mail'
    ],
    'external_dependencies': {
        'python': [],
    },

    # always loaded
    'data': [
       'views/website_navbar_template.xml',
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