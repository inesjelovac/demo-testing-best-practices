"""Test naming patterns

UnitOfWorkName-Scenario-ExpectedBehavior

There are three parts in test name:

1. function under test name
2. case description
3. result description

Each part is usually separated by underscore.
Since Python already uses underscore, for this purpose double underscore is used.

Mora about pattern: http://osherove.com/blog/2005/4/3/naming-standards-for-unit-tests.html
"""
from production_code.code_under_test import personalize_menu

def test__personalize_menu__when_user_has_allergies__return_dishes_without_allergens():
    user = {'username': 'test', 'has_allergies': True}
    menu = [
        {'name': 'dish without allergens', 'allergens': []},
        {'name': 'dish with allergens', 'allergens': ['eggs', 'milk']}
    ]
    personalized_menu = personalize_menu(menu, user)
    assert len(personalized_menu) == 1
