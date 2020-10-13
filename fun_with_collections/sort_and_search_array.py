"""Jack Reser
This program searches and sorts an array
10/12/20"""

import array as arr


def sort_array():
    pass


def search_array(x):
    pass


def make_list():
    my_list = []
    for x in range(3):
        my_input = get_input()

        if not my_input.isdigit():
            raise ValueError
        elif int(my_input) < 1:
            raise ValueError
        elif int(my_input) > 50:
            raise ValueError
        else:
            my_list.insert(x, int(my_input))

    return my_list


def get_input():
    x = input("Please enter a number:")
    return x
