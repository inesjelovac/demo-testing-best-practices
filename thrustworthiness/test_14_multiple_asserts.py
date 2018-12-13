"""Multiple asserts

Multiple assert are often sign that test is checking more than one thing.

Again, naming and styling becomes problem.

How should asserts fail? All together or it is important to know for each if it failed?
"""
from production_code.code_under_test import personalize_menu


def test__personalize_menu():
    menu = [
        {'name': 'dish without allergens', 'allergens': []},
        {'name': 'dish with allergens', 'allergens': ['eggs', 'milk']}
    ]

    personalized_menu = personalize_menu(menu, {'username': 'test', 'has_allergies': True})
    assert len(personalized_menu) == 1

    personalized_menu = personalize_menu(menu, {'username': 'test', 'has_allergies': False})
    assert len(personalized_menu) == 2
