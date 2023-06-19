# -*- coding: utf-8 -*-
{
    "name": "report_example",
    "author": "My Company",
    "website": "https://www.yourcompany.com",
    "category": "Uncategorized",
    "version": "0.1",
    "depends": ["base"],
    "data": [
        "wizard/report_view.xml",
        "security/ir.model.access.csv",
    ],
    "assets": {
        "web.assets_backend": ["report_example/static/src/js/action_manager.js"],
    },
    "installable": True,
    "application": True,
    "auto_install": True,
    "license": "LGPL-3",
}
