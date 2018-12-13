"""Naming

Naming in test code is as important as naming in production code.

In example: magic number is replaced by variable with verbose name
"""
from production_code.code_under_test import personalize_menu

def test__personalize_menu__when_user_has_allergies__return_dishes_without_allergens__fixed_naming():
    user = {'username': 'test', 'has_allergies': True}
    menu = [
        {'name': 'dish without allergens', 'allergens': []},
        {'name': 'dish with allergens', 'allergens': ['eggs', 'milk']}
    ]
    expected_menu_length = 1
    personalized_menu = personalize_menu(menu, user)
    assert len(personalized_menu) == expected_menu_length
