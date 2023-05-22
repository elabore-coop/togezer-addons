# Copyright 2023 Stéphan Sainléger (Elabore)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "togezer_event",
    "version": "13.0.1.1.0",
    "author": "Elabore",
    "website": "https://elabore.coop",
    "maintainer": "Clément Thomas",
    "license": "AGPL-3",
    "category": "Tools",
    "summary": "Custom events in portal",
    # any module necessary for this one to work correctly
    "depends": [
        "base",
        "website_event",
    ],
    "qweb": [],
    "external_dependencies": {
        "python": [],
    },
    # always loaded
    "data": [
        "views/event_template.xml",
        "views/event_views.xml",
    ],
    # only loaded in demonstration mode
    "demo": [],
    "js": [],
    "css": [],
    "installable": True,
    # Install this module automatically if all dependency have been previously
    # and independently installed.  Used for synergetic or glue modules.
    "auto_install": False,
    "application": False,
}