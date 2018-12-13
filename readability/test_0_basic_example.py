"""Common test example

This function is staring point for applying and demonstrating good practices in testing.
"""
from production_code.code_under_test import personalize_menu


def test_personalize_menu():
    user = {'username': 'test', 'has_allergies': True}
    menu = [
        {'name': 'dish without allergens', 'allergens': []},
        {'name': 'dish with allergens', 'allergens': ['eggs', 'milk']}
    ]
    personalized_menu = personalize_menu(menu, user)
    assert len(personalized_menu) == 1
