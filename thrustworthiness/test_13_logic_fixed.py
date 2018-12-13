"""Logic in test code

Very good way to avoid logic in tests but also to avoid code duplication
is to use parametrized tests.
"""
import pytest

from production_code.code_under_test import personalize_menu


@pytest.mark.parametrize("user,expected_menu_length", [
    ({'username': 'test', 'has_allergies': True}, 1),
    ({'username': 'test', 'has_allergies': False}, 2),
])
def test__personalize_menu__parametrized(user, expected_menu_length):
    menu = [
        {'name': 'dish without allergens', 'allergens': []},
        {'name': 'dish with allergens', 'allergens': ['eggs', 'milk']}
    ]

    personalized_menu = personalize_menu(menu, user)

    assert len(personalized_menu) == expected_menu_length
