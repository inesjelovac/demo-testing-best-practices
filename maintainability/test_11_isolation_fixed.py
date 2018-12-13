"""Isolation

Time isolation: the most readable and maintainable solution is
to fix now and then "hardcode" other moments.
"""
import unittest
from datetime import date

from freezegun import freeze_time

from production_code.code_under_test import latest_offer_menu


@freeze_time("2015-06-21")
class TestLatestOfferMenuWithTimeIsolation(unittest.TestCase):
    """Imagine this code was written on June 21st 2015. Real system time is not used any more"""

    def test__nothing_to_offer_today__returns_empty_list(self):
        menu = [
            {'name': 'dish without allergens', 'allergens': [], 'date': date(2015, 1, 1)},
            {'name': 'dish with allergens', 'allergens': ['eggs', 'milk'], 'date': date(2015, 1, 2)}
        ]
        expected_menu_length = 0

        resulting_menu = latest_offer_menu(menu)

        assert len(resulting_menu) == expected_menu_length

    def test__one_dish_to_offer_today__returns_filtered_list(self):
        menu = [
            {'name': 'dish without allergens', 'allergens': [], 'date': date(2017, 12, 31)},
            {'name': 'dish with allergens', 'allergens': ['eggs', 'milk'], 'date': date(2015, 1, 1)}
        ]
        expected_menu_length = 1

        resulting_menu = latest_offer_menu(menu)

        assert len(resulting_menu) == expected_menu_length

    def test__all_dishes_to_offer_today__returns_unchanged_list(self):
        menu = [
            {'name': 'dish without allergens', 'allergens': [], 'date': date(2017, 12, 31)},
            {'name': 'dish with allergens', 'allergens': ['eggs', 'milk'], 'date': date(2017, 12, 31)}
        ]
        expected_menu_length = 2

        resulting_menu = latest_offer_menu(menu)

        assert len(resulting_menu) == expected_menu_length
