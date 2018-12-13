"""Code under test example

This module contains simple function which is used to demonstrate how to write
good tests.

Function personalize_menu filters out dishes with allergens from given menu for user with allergies.

Function latest_offer_menu prints dishes that will be served today and in future.
"""
from datetime import datetime, timedelta


def personalize_menu(menu, user):
    if user['has_allergies']:
        return [dish for dish in menu if not dish.get('allergens')]

    return menu

def latest_offer_menu(menu):
    today = datetime.now().date()
    return [dish for dish in menu if dish.get('date') >= today]


# example call

today = datetime.now().date()
yesterday = today - timedelta(1)
tomorrow = today  + timedelta(1)

menu = [
    {'name': 'apple', 'allergens': [], 'date': yesterday},
    {'name': 'chocolate cake', 'allergens': ['eggs', 'gluten', 'milk'], 'date': today},
    {'name': 'tomato soup', 'allergens': [], 'date': today},
    {'name': 'lasagne', 'allergens': ['eggs', 'milk'], 'date': tomorrow}
]

users = [
    {'username': 'marvin', 'has_allergies': True},
    {'username': 'trillian', 'has_allergies': False}
]

filtered_menu = personalize_menu(menu, users[0])
print(filtered_menu)

filtered_menu = personalize_menu(menu, users[1])
print(filtered_menu)

print(latest_offer_menu(menu))
