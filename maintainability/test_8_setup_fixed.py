"""Avoid using setup method

Fixed setup method.
"""
import unittest

import pytest

from production_code.code_under_test import personalize_menu


class TestPersonalizeMenu(unittest.TestCase):
    def setUp(self):
        self.menu = [
            {'name': 'dish without allergens', 'allergens': []},
            {'name': 'dish with allergens', 'allergens': ['eggs', 'milk']}
        ]

    def test__when_user_has_allergies__return_dishes_without_allergens(self):
        user = {'username': 'test', 'has_allergies': True}
        expected_menu_length = 1

        personalized_menu = personalize_menu(self.menu, user)

        assert len(personalized_menu) == expected_menu_length

    def test__when_user_dont_have_allergies__return_all_dishes(self):
        user = {'username': 'test', 'has_allergies': False}
        expected_menu_length = 2

        personalized_menu = personalize_menu(self.menu, user)

        assert len(personalized_menu) == expected_menu_length

    def test__when_user_dont_have_allergies_flag__raise_exception(self):
        user = {'username': 'test'}

        with pytest.raises(KeyError):
            personalize_menu(self.menu, user)
