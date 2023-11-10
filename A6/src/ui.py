#
# This is the program's UI module. The user interface and all interaction with the user (print and input statements)
# are found here
#
import copy

import functions as f


def start_application():
    apartment_list = f.make_random_apartment_list(10)
    all_apartment_list = []
    f.memorise_move(all_apartment_list, apartment_list)
    print(f.Style.CYAN + "WELCOME TO A6" + f.Style.RESET)
    print("To view command type help.")

    while True:
        print("\nPlease introduce your command: \n")
        user_input = input()
        user_input_array = user_input.split()
        user_input_verify = ""
        first_choice = user_input_array[0]
        if len(all_apartment_list) > 0:
            special_index = len(all_apartment_list) - 1
            apartment_list = copy.deepcopy(all_apartment_list[special_index])
        else:
            apartment_list = copy.deepcopy(all_apartment_list[0])
        for i in range(len(user_input_array)):
            if i == len(user_input_array) - 1:
                user_input_verify = user_input_verify + user_input_array[i]
            else:
                user_input_verify = user_input_verify + user_input_array[i] + " "
        if user_input_verify == user_input:
            if first_choice == 'add' and len(user_input_array) == 4:
                try:
                    f.add_expenses(apartment_list, int(user_input_array[1]), f.get_expense_number(user_input_array[2]),
                                   int(user_input_array[3]))
                    print(f.Style.BLUE + "\nTransaction added." + f.Style.RESET)
                    f.memorise_move(all_apartment_list, apartment_list)
                except ValueError as error:
                    print("\n" + str(error))
            elif user_input_array[0] == 'remove':
                if len(user_input_array) == 2 and user_input_array[1].isnumeric():
                    try:
                        f.remove_all_apartment_expenses(apartment_list, int(user_input_array[1]))
                        print(f.Style.BLUE + "\nApartment expenses removed." + f.Style.RESET)
                        f.memorise_move(all_apartment_list, apartment_list)
                    except ValueError as error:
                        print("\n" + str(error))
                elif len(user_input_array) == 4 and user_input_array[2] == 'to' and user_input_array[1].isnumeric() \
                        and user_input_array[3].isnumeric():
                    try:
                        f.remove_all_apartment_expenses_interval(apartment_list, int(user_input_array[1]),
                                                                 int(user_input_array[3]))
                        print(f.Style.BLUE + "\nApartment expenses removed." + f.Style.RESET)
                        f.memorise_move(all_apartment_list, apartment_list)
                    except ValueError as error:
                        print("\n" + str(error))
                elif len(user_input_array) == 2 and user_input_array[1].isnumeric() is False and \
                        user_input_array[1] != 'apartment':
                    try:
                        f.remove_expense(apartment_list, f.get_expense_number(user_input_array[1]))
                        print(f.Style.BLUE + "\nExpenses removed." + f.Style.RESET)
                        f.memorise_move(all_apartment_list, apartment_list)
                    except ValueError as error:
                        print("\n" + str(error))
                elif user_input_array[1] == 'apartment' and len(user_input_array) == 3:
                    try:
                        f.remove_apartment(apartment_list, int(user_input_array[2]))
                        print(f.Style.BLUE + "\nApartment removed." + f.Style.RESET)
                        f.memorise_move(all_apartment_list, apartment_list)
                    except ValueError as error:
                        print("\n" + str(error))
            elif user_input_array[0] == 'replace' and len(user_input_array) == 5 and user_input_array[3] == 'with':
                try:
                    f.replace_apartment_expenses(apartment_list, int(user_input_array[1]),
                                                 f.get_expense_number(user_input_array[2]), int(user_input_array[4]))
                    print(f.Style.BLUE + "\nApartment expenses modified." + f.Style.RESET)
                    f.memorise_move(all_apartment_list, apartment_list)
                except ValueError as error:
                    print("\n" + str(error))
            elif first_choice == 'list':
                if user_input_array[1] == 'all' and len(user_input_array) == 2:
                    print(f.show_apartment_list(apartment_list))
                elif user_input_array[1].isnumeric():
                    try:
                        print(f.to_str(f.find_apartment(apartment_list, int(user_input_array[1]))))
                    except ValueError as error:
                        print("\n" + str(error))
                elif user_input_array[1] == '<' and len(user_input_array) == 3:
                    try:
                        print(
                            f.show_apartment_list(
                                f.show_apartments_condition(apartment_list, 1, int(user_input_array[2]))))
                    except ValueError as error:
                        print("\n" + str(error))
                elif user_input_array[1] == '>' and len(user_input_array) == 3:
                    try:
                        print(
                            f.show_apartment_list(
                                f.show_apartments_condition(apartment_list, 2, int(user_input_array[2]))))
                    except ValueError as error:
                        print("\n" + str(error))
                elif user_input_array[1] == '=' and len(user_input_array) == 3:
                    try:
                        print(
                            f.show_apartment_list(
                                f.show_apartments_condition(apartment_list, 3, int(user_input_array[2]))))
                    except ValueError as error:
                        print("\n" + str(error))
                else:
                    print("Input not valid")
            elif first_choice == 'filter':
                if user_input_array[1].isnumeric() is False and len(user_input_array) == 2:
                    try:
                        f.filter_expenses_type(apartment_list, f.get_expense_number(user_input_array[1]))
                        print(f.Style.BLUE + "\nFilter applied." + f.Style.RESET)
                        f.memorise_move(all_apartment_list, apartment_list)
                    except ValueError as error:
                        print("\n" + str(error))
                elif user_input_array[1].isnumeric() and len(user_input_array) == 2:
                    try:
                        f.filter_expenses_amount(apartment_list, int(user_input_array[1]))
                        print(f.Style.BLUE + "\nFilter applied." + f.Style.RESET)
                        f.memorise_move(all_apartment_list, apartment_list)
                    except ValueError as error:
                        print("\n" + str(error))
                else:
                    print("Input not valid")
            elif first_choice == 'help' and len(user_input_array) == 1:
                print("\nadd <apartment> <type> <amount>\n")
                print("remove <apartment>")
                print("remove <start apartment> to <end apartment>")
                print("remove <type>")
                print("remove apartment <apartment>")
                print("replace <apartment> <type> with <amount>\n")
                print("list all")
                print("list <apartment>")
                print("list [ < | = | > ] <amount>\n")
                print("filter <type>")
                print("filter <value>")
                print("undo")
            elif first_choice == 'undo' and len(user_input_array) == 1:
                try:
                    f.undo_move(all_apartment_list)
                    print(f.Style.BLUE + "\nUndo function executed." + f.Style.RESET)
                except ValueError as error:
                    print("\n" + str(error))
            elif first_choice == 'quit' and len(user_input_array) == 1:
                print("Quitting...")
                return
            else:
                print("Input not valid.")
        else:
            print("Input is not valid")
