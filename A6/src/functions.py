#
# The program's functions are implemented here. There is no user interaction in this file,
# therefore no input/print statements.
# Functions here communicate via function parameters, the return statement and raising of exceptions.
#

import random as r
import os
import copy

os.system("")


class Style:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


def new_apartment(apartment_number, water_amount, heating_amount, electricity_amount, gas_amount, other_amount):
    return [apartment_number, water_amount, heating_amount, electricity_amount, gas_amount, other_amount]


def find_apartment(apartment_list: list, apartment_number: int):
    for index in range(len(apartment_list)):
        if apartment_number == apartment_list[index][0]:
            return apartment_list[index]
    raise ValueError("Apartment " + Style.MAGENTA + str(apartment_number) + Style.RESET + " was not found.")


def find_apartment_index(apartment_list: list, apartment_number: int):
    """
    Finds the index of an apartment in the apartment_list
    :param apartment_list:
    :param apartment_number:
    :return: index
    """
    for index in range(len(apartment_list)):
        if apartment_number == apartment_list[index][0]:
            return index
    raise ValueError("Apartment " + Style.MAGENTA + str(apartment_number) + Style.RESET + " was not found.")


def get_apartment_number_list(apartment_list: list):
    """
    for the function remove x to y, gets a list with the apartment numbers
    :param apartment_list:
    :return: list with apartment numbers
    """
    apartment_number_list = []
    for i in range(len(apartment_list)):
        apartment_number_list.append(apartment_list[i][0])
    return apartment_number_list


def to_str(apartment: list):
    """
    to string function
    :param apartment:
    :return: a string :)
    """
    to_string = " "
    if apartment[0] != 0:
        to_string = to_string + Style.MAGENTA + "\n Apartment number: " + str(apartment[0]) + Style.RESET
    if apartment[1] != 0:
        to_string = to_string + "\n Water expenses: " + str(apartment[1])
    if apartment[2] != 0:
        to_string = to_string + "\n Heating expenses: " + str(apartment[2])
    if apartment[3] != 0:
        to_string = to_string + "\n Electricity expenses: " + str(apartment[3])
    if apartment[4] != 0:
        to_string = to_string + "\n Gas expenses: " + str(apartment[4])
    if apartment[5] != 0:
        to_string = to_string + "\n Other expenses: " + str(apartment[5])
    return to_string


def show_apartment_list(apartment_list: list):
    """
    displays the apartments
    :param apartment_list:
    :return:
    """
    print(apartment_list)
    sorted_list = apartment_list[:]
    sorted_list.sort()
    return "CURRENT APARTMENTS:\n" + Style.RESET + "\n".join(map(to_str, sorted_list))


def make_random_apartment_list(count: int):
    """
    makes random apartments, is accessed at the beginning of the program
    :param count:
    :return:
    """
    assert count < 40 ** 2

    apartment_list = []
    apartment_number_list = r.sample(range(1, 100), count)
    while count > 0:
        apartment_number = apartment_number_list[count - 1]
        water_amount = r.randint(0, 100)
        heating_amount = r.randint(0, 100)
        electricity_amount = r.randint(0, 100)
        gas_amount = r.randint(0, 100)
        other_amount = r.randint(0, 100)
        apartment_list.append(new_apartment(apartment_number, water_amount, heating_amount,
                                            electricity_amount, gas_amount, other_amount))
        count -= 1
    return apartment_list


def add_apartment(apartment_list: list, apartment: list):
    """
    not used
    :param apartment_list:
    :param apartment:
    :return:
    """
    apartment_list.append(apartment)


def add_expenses(apartment_list: list, apartment_number: int, expense_type: int, amount: int):
    """
    add expenses function, adds to current value
    :param apartment_list:
    :param apartment_number:
    :param expense_type:
    :param amount:
    :return:
    """
    if expense_type > 5 or expense_type < 1:
        raise ValueError("The expense type " + Style.MAGENTA + str(expense_type) + Style.RESET + " is not valid.")
    try:
        index = find_apartment_index(apartment_list, apartment_number)
        if expense_type == 1:
            apartment_list[index][1] = apartment_list[index][1] + amount
        elif expense_type == 2:
            apartment_list[index][2] = apartment_list[index][2] + amount
        elif expense_type == 3:
            apartment_list[index][3] = apartment_list[index][3] + amount
        elif expense_type == 4:
            apartment_list[index][4] = apartment_list[index][4] + amount
        elif expense_type == 5:
            apartment_list[index][5] = apartment_list[index][5] + amount
        return apartment_list
    except ValueError as error:
        print(str(error))
        print("We'll add a new apartment.\n")
        add_apartment(apartment_list, new_apartment(apartment_number, 0, 0, 0, 0, 0))
        index = len(apartment_list) - 1
        if expense_type == 1:
            apartment_list[index][1] = apartment_list[index][1] + amount
        elif expense_type == 2:
            apartment_list[index][2] = apartment_list[index][2] + amount
        elif expense_type == 3:
            apartment_list[index][3] = apartment_list[index][3] + amount
        elif expense_type == 4:
            apartment_list[index][4] = apartment_list[index][4] + amount
        elif expense_type == 5:
            apartment_list[index][5] = apartment_list[index][5] + amount
        return apartment_list


def remove_apartment(apartment_list: list, apartment_number: int):
    """
    removes an apartment
    :param apartment_list:
    :param apartment_number:
    :return:
    """
    for index in range(len(apartment_list)):
        if find_apartment_index(apartment_list, apartment_number) != -1:
            apartment_list.pop(find_apartment_index(apartment_list, apartment_number))
            return apartment_list
    raise ValueError("Apartment " + Style.MAGENTA + str(apartment_number) + Style.RESET + " was not found.")


def remove_all_apartment_expenses_interval(apartment_list: list, first_apartment: int, last_apartment: int):
    """
    for remove x to y
    :param apartment_list:
    :param first_apartment:
    :param last_apartment:
    :return:
    """
    apartment_number_list = get_apartment_number_list(apartment_list)
    flag = 0
    for i in range(len(apartment_number_list)):
        index = find_apartment_index(apartment_list, apartment_number_list[i])
        if first_apartment <= apartment_number_list[i] <= last_apartment and index != -1:
            apartment_list[index][1] = 0
            apartment_list[index][2] = 0
            apartment_list[index][3] = 0
            apartment_list[index][4] = 0
            apartment_list[index][5] = 0
            flag = 1
    if flag == 1:
        return apartment_list
    else:
        raise ValueError("Apartments were not found.")


def remove_all_apartment_expenses(apartment_list: list, apartment_number: int):
    """
    sets all apartment expenses to 0
    :param apartment_list:
    :param apartment_number:
    :return:
    """
    index = find_apartment_index(apartment_list, apartment_number)
    if index != -1:
        apartment_list[index][1] = 0
        apartment_list[index][2] = 0
        apartment_list[index][3] = 0
        apartment_list[index][4] = 0
        apartment_list[index][5] = 0
    else:
        raise ValueError("Apartments were not found.")


def remove_expense(apartment_list: list, expense_type: int):
    """
    sets apartment expenses to 0 (only 1)
    :param apartment_list:
    :param expense_type:
    :return:
    """
    if expense_type > 5 or expense_type < 0:
        raise ValueError("The expense type " + Style.MAGENTA + str(expense_type) + Style.RESET + " is not valid.")
    for index in range(len(apartment_list)):
        if expense_type == 1:
            apartment_list[index][1] = 0
        elif expense_type == 2:
            apartment_list[index][2] = 0
        elif expense_type == 3:
            apartment_list[index][3] = 0
        elif expense_type == 4:
            apartment_list[index][4] = 0
        elif expense_type == 5:
            apartment_list[index][5] = 0
    return apartment_list


def replace_apartment_expenses(apartment_list: list, apartment_number: int, expense_type: int, amount: int):
    """
    replaces the value of an expense
    :param apartment_list:
    :param apartment_number:
    :param expense_type:
    :param amount:
    :return:
    """
    index = find_apartment_index(apartment_list, apartment_number)
    apartment_list[index][expense_type] = amount
    return apartment_list


def show_apartment(apartment_list: list, apartment_number: int):
    return "All expenses for the requested apartment:" + to_str(find_apartment(apartment_list, apartment_number))


def total_expenses(apartment_list: list):
    """
    calculates the total value of the expenses
    :param apartment_list:
    :return:
    """
    total_expenses_list = []
    for index in range(len(apartment_list)):
        total_expenses_list.append(apartment_list[index][1] + apartment_list[index][2] +
                                   apartment_list[index][3] + apartment_list[index][4] + apartment_list[index][5])
    return total_expenses_list


def show_apartments_condition(apartment_list: list, condition: int, amount: int):
    """
    for < = > function
    :param apartment_list:
    :param condition:
    :param amount:
    :return:
    """
    show_apartments_condition_list = []
    total_expenses_list = total_expenses(apartment_list)
    flag = 0
    if condition > 3 or condition < 1:
        raise ValueError("The condition " + Style.MAGENTA + str(condition) + Style.RESET + " is not valid.")
    if condition == 1:
        for i in range(len(total_expenses_list)):
            if total_expenses_list[i] < amount:
                show_apartments_condition_list.append(apartment_list[i])
                flag = 1
    if condition == 2:
        for i in range(len(total_expenses_list)):
            if total_expenses_list[i] > amount:
                show_apartments_condition_list.append(apartment_list[i])
                flag = 1
    if condition == 3:
        for i in range(len(total_expenses_list)):
            if total_expenses_list[i] == amount:
                show_apartments_condition_list.append(apartment_list[i])
                flag = 1
    if flag == 0:
        raise ValueError("No apartments match the condition")
    else:
        return show_apartments_condition_list


def filter_expenses_type(apartment_list: list, expense_type: int):
    """
    sets the other expenses other than the given input to 0
    :param apartment_list:
    :param expense_type:
    :return:
    """
    if expense_type > 5 or expense_type < 1:
        raise ValueError("The expense type " + Style.MAGENTA + str(expense_type) + Style.RESET + " is not valid.")
    if expense_type == 1:
        for i in range(len(apartment_list)):
            apartment_list[i][2] = 0
            apartment_list[i][3] = 0
            apartment_list[i][4] = 0
            apartment_list[i][5] = 0
    elif expense_type == 2:
        for i in range(len(apartment_list)):
            apartment_list[i][1] = 0
            apartment_list[i][3] = 0
            apartment_list[i][4] = 0
            apartment_list[i][5] = 0
    elif expense_type == 3:
        for i in range(len(apartment_list)):
            apartment_list[i][1] = 0
            apartment_list[i][2] = 0
            apartment_list[i][4] = 0
            apartment_list[i][5] = 0
    elif expense_type == 4:
        for i in range(len(apartment_list)):
            apartment_list[i][1] = 0
            apartment_list[i][2] = 0
            apartment_list[i][3] = 0
            apartment_list[i][5] = 0
    elif expense_type == 5:
        for i in range(len(apartment_list)):
            apartment_list[i][1] = 0
            apartment_list[i][2] = 0
            apartment_list[i][3] = 0
            apartment_list[i][4] = 0
    return apartment_list


def filter_expenses_amount(apartment_list: list, amount: int):
    """
    filters >= amount
    :param apartment_list:
    :param amount:
    :return:
    """
    if amount != int(amount):
        raise ValueError("The amount " + Style.MAGENTA + str(amount) + Style.RESET + " is not an integer.")
    for i in range(len(apartment_list)):
        for j in range(1, len(apartment_list[i])):
            if apartment_list[i][j] >= amount:
                apartment_list[i][j] = 0


def get_expense_number(user_input):
    """
    gets the number associated to the user input. e.g. gas = 4
    :param user_input:
    :return:
    """
    expense_type = 0
    if user_input == 'water':
        expense_type = 1
    elif user_input == 'heating':
        expense_type = 2
    elif user_input == 'electricity':
        expense_type = 3
    elif user_input == 'gas':
        expense_type = 4
    elif user_input == 'other':
        expense_type = 5
    if expense_type == 0:
        raise ValueError("The input " + user_input + " was not correct.")
    else:
        return expense_type


def memorise_move(all_apartment_list: list, apartment_list: list):
    """
    memorises every variant of a list
    :param all_apartment_list:
    :param apartment_list:
    :return:
    """
    temp_list = copy.deepcopy(apartment_list)
    all_apartment_list.append(temp_list)


def undo_move(all_apartment_list: list):
    """
    undo
    :param all_apartment_list:
    :return:
    """
    index = len(all_apartment_list) - 1
    if index > 0:
        all_apartment_list.pop(index)
    else:
        raise ValueError("Can't undo.")
