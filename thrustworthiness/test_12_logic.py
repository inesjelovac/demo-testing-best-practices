"""Logic in test code

If there is logic in test, sooner or later, there will be bug too.
It is also extremely hard to read and to maintain.

Another problems with logic in tests:
- naming
- styling

"""
from production_code.code_under_test import personalize_menu


def test__personalize_menu__with_logic():
    users = [
        {'username': 'test', 'has_allergies': True},
        {'username': 'test', 'has_allergies': False}
    ]
    menu = [
        {'name': 'dish without allergens', 'allergens': []},
        {'name': 'dish with allergens', 'allergens': ['eggs', 'milk']}
    ]

    for user in users:
        personalized_menu = personalize_menu(menu, user)
        if user['has_allergies']:
            expected_menu_length = 1
        else:
            expected_menu_length = 2

        assert len(personalized_menu) == expected_menu_length
