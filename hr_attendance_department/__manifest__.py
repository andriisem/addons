{
    "name": "Hr Attendance Department",
    "version": "1.0",
    "category": "HR",
    "author": 'Andrii Semko | @andriisem',
    "website": "https://www.upwork.com/o/profiles/users/_~013175f63de76dd835/",
    "description": """
        The employee chooses the department where works
    """,
    "depends": ['hr_attendance'],
    "data": [
        'security/ir.model.access.csv',
        'views/assets.xml',
        'views/hr_attendance_view.xml',
        'views/hr_department_view.xml',
        'views/hr_employee_view.xml',
        'views/hr_department_restaurant_view.xml',
    ],
    'qweb': [
        'static/src/xml/attendance.xml',
    ],
    "application": False,
    "installable": True,
}