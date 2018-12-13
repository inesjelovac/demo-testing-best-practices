"""Avoid using setup method

Setup method usually makes tests unreadable by introducing code that is not used by ALL tests.

In following example:
- some tests use self.user, and some custom user
- self.expected_menu_length is used by only one test
"""
import unittest

import pytest

from production_code.code_under_test import personalize_menu


class TestPersonalizeMenu(unittest.TestCase):
    def setUp(self):
        self.user = {'username': 'test', 'has_allergies': True}
        self.menu = [
            {'name': 'dish without allergens', 'allergens': []},
            {'name': 'dish with allergens', 'allergens': ['eggs', 'milk']}
        ]
        self.expected_menu_length = 1

    def test__when_user_has_allergies__return_dishes_without_allergens(self):
        personalized_menu = personalize_menu(self.menu, self.user)

        assert len(personalized_menu) == self.expected_menu_length

    def test__when_user_dont_have_allergies__return_all_dishes(self):
        user = {'username': 'test', 'has_allergies': False}
        personalized_menu = personalize_menu(self.menu, user)
        expected_menu_length = 2

        assert len(personalized_menu) == expected_menu_length

    def test__when_user_dont_have_allergies_flag__raise_exception(self):
        user = {'username': 'test'}

        with pytest.raises(KeyError):
            personalize_menu(self.menu, user)