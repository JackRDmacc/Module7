"""Jack Reser
This program searches and sorts a list
10/12/20"""


def sort_list():
    pass


def search_list(x):
    my_list = make_list()
    try:
        return my_list.index(x)
    except ValueError:
        return -1


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
