"""Styling tests

Separate test visually in three parts:

1. arrange statements
2. act statement
3. assert statements

Add blank line between each part to improve readability.
"""
from production_code.code_under_test import personalize_menu


def test__personalize_menu__when_user_has_allergies__return_dishes_without_allergens():
    # arrange statements:
    user = {'username': 'test', 'has_allergies': True}
    menu = [
        {'name': 'dish without allergens', 'allergens': []},
        {'name': 'dish with allergens', 'allergens': ['eggs', 'milk']}
    ]
    expected_menu_length = 1

    # act statement:
    personalized_menu = personalize_menu(menu, user)

    # assert statements:
    assert len(personalized_menu) == expected_menu_length
