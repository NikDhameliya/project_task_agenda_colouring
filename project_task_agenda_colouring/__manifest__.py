# -*- coding: utf-8 -*-

{
    'name' : 'Kanban Background Color',
    'version': '12.0.0.1.0',
    'summary': 'Kanban Background Color',
    'category': 'Project',
    'description': """
        Set Background color of task kanbanview from color picker,
        Followed : https://www.odoo.yenthevg.com/adding-custom-colors-to-agenda-and-kanban-views/
    """,
    'author': 'Nikunj Dhameliya',
    'website': 'https://www.upwork.com/o/profiles/users/_~01cc28161571ffd1bd/',
    'depends': ['project', 'calendar', 'web_widget_color'],
    'data': [
        'security/ir.model.access.csv',
        'views/agenda_status_view.xml',
        'views/assets.xml',
        'views/project_task.xml',
    ],
    'qweb': []
}


