"""Code under test example

This module contains modified version of example production code with bug
used to demonstrate failing tests.
"""


def buggy_personalize_menu(menu, user):
    if user.get('has_allergies'):
        return [dish for dish in menu if dish.get('allergens')] # 'not' omitted

    return menu


# example call

menu = [
    {'name': 'apple', 'allergens': []},
    {'name': 'chocolate cake', 'allergens': ['eggs', 'gluten', 'milk']},
    {'name': 'tomato soup', 'allergens': []},
    {'name': 'lasagne', 'allergens': ['eggs', 'milk']}
]

users = [
    {'username': 'marvin', 'has_allergies': True},
    {'username': 'trillian', 'has_allergies': False}
]

filtered_menu = buggy_personalize_menu(menu, users[0])
print(filtered_menu)

filtered_menu = buggy_personalize_menu(menu, users[1])
print(filtered_menu)
