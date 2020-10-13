"""Jack Reser
This program deals with text file i/o
10/12/20"""


def write_to_file(my_tuple):
    f = open('student_info.txt', 'a')
    f.write(str(my_tuple))
    f.write('\n')
    f.close()


def get_student_info(student):
    my_list = [student]

    stop_loop = False
    print(student + ":")

    while not stop_loop:
        my_input = int(input("(-1 to stop) Enter a test score: "))

        if my_input == -1:
            print()
            stop_loop = True
        else:
            my_list.append(my_input)

    my_tuple = tuple(my_list)

    write_to_file(my_tuple)


def read_from_file():
    f = open('student_info.txt', 'r')
    file_lines = f.readlines()

    for x in file_lines:
        print(x)


if __name__ == '__main__':
    f = open('student_info.txt', 'w')
    f.close()

    get_student_info("Jack")
    get_student_info("Avery")
    get_student_info("Ryan")
    get_student_info("Rick")

    read_from_file()

    input("Press any key to end: ")
