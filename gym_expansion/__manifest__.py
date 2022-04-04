# -*- coding: utf-8 -*-
{
    'name': "gym_expansion",

    'summary': """Gym manament expansion""",

    'description': """Gym manament expansion""",

    'author': "Guadaltech",
    'website': "http://www.guadaltech.es",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '14.0.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['gym'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/classes_views.xml',
        'views/users_views.xml',
        'views/materiales_views.xml',
        'views/menu.xml',
    ],
}
