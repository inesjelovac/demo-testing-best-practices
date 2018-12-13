"""Isolation

Time isolation: solution that will work at any moment in future.
But what are disadvantages of this approach?
"""
import unittest
from datetime import datetime, timedelta

from production_code.code_under_test import latest_offer_menu


class TestLatestOfferMenuWithoutTimeIsolationUsingRelativeTime(unittest.TestCase):
    """Imagine this code was written on June 21st 2015.
    In this example time is relative to time of running test.
    Tests will pass in 2018, but this is hard to maintain and read
    """
    def test__nothing_to_offer__returns_empty_list(self):
        today = datetime.now().date()
        menu = [
            {'name': 'dish without allergens', 'allergens': [], 'date': today - timedelta(1)},
            {'name': 'dish with allergens', 'allergens': ['eggs', 'milk'], 'date': today - timedelta(1)}
        ]
        expected_menu_length = 0

        resulting_menu = latest_offer_menu(menu)

        assert len(resulting_menu) == expected_menu_length

    def test__one_dish_to_offer_today__returns_filtered_list(self):
        today = datetime.now().date()
        menu = [
            {'name': 'dish without allergens', 'allergens': [], 'date': today - timedelta(1)},
            {'name': 'dish with allergens', 'allergens': ['eggs', 'milk'], 'date': today}
        ]
        expected_menu_length = 1

        resulting_menu = latest_offer_menu(menu)

        assert len(resulting_menu) == expected_menu_length

    def test__one_dish_to_offer_tomorrow__returns_filtered_list(self):
        today = datetime.now().date()
        menu = [
            {'name': 'dish without allergens', 'allergens': [], 'date': today - timedelta(1)},
            {'name': 'dish with allergens', 'allergens': ['eggs', 'milk'], 'date': today + timedelta(1)}
        ]
        expected_menu_length = 1

        resulting_menu = latest_offer_menu(menu)

        assert len(resulting_menu) == expected_menu_length

    def test__all_dishes_to_offer__returns_unchanged_list(self):
        today = datetime.now().date()
        menu = [
            {'name': 'dish without allergens', 'allergens': [], 'date': today},
            {'name': 'dish with allergens', 'allergens': ['eggs', 'milk'], 'date': today + timedelta(1)}
        ]
        expected_menu_length = 2

        resulting_menu = latest_offer_menu(menu)

        assert len(resulting_menu) == expected_menu_length
