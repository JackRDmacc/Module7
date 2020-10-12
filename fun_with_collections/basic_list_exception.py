"""Jack Reser
This program accepts input into a list and then returns the list
10/12/20"""


def make_list():
    my_list = []
    for x in range(3):
        my_list.insert(x, int(get_input()))
    return my_list


def get_input():
    x = input("Please enter a number:")
    if not x.isdigit():
        raise Exception("Non-numeric input")
    else:
        return x


if __name__ == '__main__':
    print(get_input())
