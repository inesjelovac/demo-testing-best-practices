"""Code under test example

This module contains slightly modified version of example production code used to demonstrate
writing test when requirements change.
"""


def modified_personalize_menu(menu, user):
    if user['is_allergic']: # key name changed
        return [dish for dish in menu if not dish.get('allergens')]

    return menu


# example call

menu = [
    {'name': 'apple', 'allergens': []},
    {'name': 'chocolate cake', 'allergens': ['eggs', 'gluten', 'milk']},
    {'name': 'tomato soup', 'allergens': []},
    {'name': 'lasagne', 'allergens': ['eggs', 'milk']}
]

users = [
    {'username': 'marvin', 'is_allergic': True},
    {'username': 'trillian', 'is_allergic': False}
]

filtered_menu = modified_personalize_menu(menu, users[0])
print(filtered_menu)

filtered_menu = modified_personalize_menu(menu, users[1])
print(filtered_menu)
