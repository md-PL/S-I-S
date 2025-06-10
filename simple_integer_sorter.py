"""
Python 3.13.3
Simple Integer Sorter
"""


def str_to_int(a_list: list):
    """ Summary:
    Description:
        Converts the strings in the list elements into integers
    Input:
        a_list: list
    """
    list_length = len(a_list)
    for x in range(list_length):
        y_str: str = a_list[x]
        y_int: int = int(y_str)
        a_list.pop(x)
        a_list.insert(x, y_int)
    return a_list


def get_input():
    """ Summary:
    Description:
        #
    """
    user_input: str = input("\n\tInput:\n> ")
    sort_list_f: list = user_input.split(" ")
    sort_list_f = str_to_int(sort_list_f)
    return sort_list_f


def swap_elements(the_list: list, x_f: int):
    """ Summary:
    Description:
        Swaps the places of 2 elements of the list
    Input:
        the_list: list
        x_f: int
    """
    a: int = the_list[x_f]
    b: int = the_list[x_f + 1]
    the_list.pop(x_f + 1)
    the_list.pop(x_f)
    the_list.insert(x_f, b)
    the_list.insert(x_f + 1, a)
    return the_list


def int_to_str(the_a_list: list):
    """ Summary:
    Description:
        Converts the integers in the list elements into strings
    Input:
        a_list: list
    """
    list_length = len(the_a_list)
    for x in range(list_length):
        y_str: int = the_a_list[x]
        y_int: str = str(y_str)
        the_a_list.pop(x)
        the_a_list.insert(x, y_int)
    return the_a_list


def list_to_string(the_list: list):
    """ Summary:
    Description:
        Sorts the values of the list
    Input:
        the_list: list
    """
    the_list = int_to_str(the_list)
    output_f = " ".join(the_list)
    return output_f


def sort_values(a_list: list):
    """ Summary:
    Description:
        Sorts the values of the list
    Input:
        a_list: list
    """
    sort: bool = True
    score: int = 0
    list_length = len(a_list)
    while sort:
        for x in range(list_length - 1):
            a: int = a_list[x]
            b: int = a_list[x + 1]
            if a > b:
                swap_elements(a_list, x)
                score -= 1
            else:
                score += 1
        # TODO it needs a better exit condition
        if score >= (list_length * 5):
            sort = False
    a_list = list_to_string(a_list)
    return a_list


def main():
    """ Summary:
    Description:
        Runs the app
    """
    again: bool = True
    print("\nSeparate the integers with space\n")
    while again:
        again = False
        sort_list: list = get_input()
        output = sort_values(sort_list)
        print(f"\n\tOutput:\n{output}\n")
        again_question = input("\nContinue? y/n\n> ")
        print()
        if again_question == "y":
            again = True


if __name__ == "__main__":
    main()

# Examples:
# 1 45 7 2732587 4 69 2 347 6 46732
# 5 2 89 3 4538 12476 67 23 7 0 3 0 2
