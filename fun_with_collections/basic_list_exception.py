"""Jack Reser
This program accepts input into a list and then returns the list
10/12/20"""


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


if __name__ == '__main__':
    print(get_input())
