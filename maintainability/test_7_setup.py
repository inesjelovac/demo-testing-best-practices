"""Avoid using setup method

Setup method usually makes tests unmaintainable by introducing code that is not used by ALL tests.

In following example, what happens if user's 'has_allergies' flag changed name to 'is_allergic':
1. developer sees user in setup and changes flag name
2. then she runs tests, but one test is still failing
3. after looking at test method she sees there is one more user to update
"""
import unittest

import pytest

from production_code.code_under_test_with_change_in_logic import modified_personalize_menu


class TestModifiedPersonalizeMenu(unittest.TestCase):
    def setUp(self):
        self.user = {'username': 'test', 'is_allergic': True} # flag name updated ...
        self.menu = [
            {'name': 'dish without allergens', 'allergens': []},
            {'name': 'dish with allergens', 'allergens': ['eggs', 'milk']}
        ]
        self.expected_menu_length = 1

    def test__when_user_has_allergies__return_dishes_without_allergens(self):
        personalized_menu = modified_personalize_menu(self.menu, self.user)

        assert len(personalized_menu) == self.expected_menu_length

    def test__when_user_dont_have_allergies__return_all_dishes(self):
        user = {'username': 'test', 'is_allergic': False} # ... and another flag name updated
        personalized_menu = modified_personalize_menu(self.menu, user)
        expected_menu_length = 2

        assert len(personalized_menu) == expected_menu_length

    def test__when_user_dont_have_allergies_flag__raise_exception(self):
        user = {'username': 'test'}

        with pytest.raises(KeyError):
            modified_personalize_menu(self.menu, user)