"""Test naming patterns

Should-ExpectedBehavior-When-StateUnderTest

This is pattern has two parts:
1. Should and description of expected behavior
2. When and preconditions
"""
from production_code.code_under_test import personalize_menu

def test__should_return_dishes_without_allergens__when_user_has_allergies():
    user = {'username': 'test', 'has_allergies': True}
    menu = [
        {'name': 'dish without allergens', 'allergens': []},
        {'name': 'dish with allergens', 'allergens': ['eggs', 'milk']}
    ]
    personalized_menu = personalize_menu(menu, user)
    assert len(personalized_menu) == 1
