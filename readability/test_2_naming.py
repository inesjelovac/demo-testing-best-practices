"""Test naming patterns

Given-When-Then

There are three parts in test name:

1. starting state description
2. behaviour description
3. expected result description

As in previous pattern, each part is usually separated by underscore.

More about pattern: https://martinfowler.com/bliki/GivenWhenThen.html
"""
from production_code.code_under_test import personalize_menu


def test__given_menu_contains_dishes_with_allergens__when_user_has_alergies__then_resulting_menu_should_contain_only_dishes_without_allergens():
    user = {'username': 'test', 'has_allergies': True}
    menu = [
        {'name': 'dish without allergens', 'allergens': []},
        {'name': 'dish with allergens', 'allergens': ['eggs', 'milk']}
    ]
    personalized_menu = personalize_menu(menu, user)
    assert len(personalized_menu) == 1
