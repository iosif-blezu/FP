#
# Write the implementation for A5 in this file
#
import random as r
import time as t

#
# Write below this comment 
# Functions to deal with complex numbers -- list representation
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#
"""--------------------------------------LIST--------------------------------------"""


def new_complex_number(real, imaginary: int):
    return [real, imaginary]


def get_real(complex_number):
    return complex_number[0]


def get_imaginary(complex_number):
    return complex_number[1]


def to_str(complex_number):
    """
    Return the complex number's representation as a string
    :param complex_number: The complex number
    :return: A string; for complex number  (1,2),
    return "z =  1 + 2i"
    """
    if get_real(complex_number) != 0 and get_imaginary(complex_number) != 0:
        if get_imaginary(complex_number) > 1:
            return "z = " + str(complex_number[0]) + " + " + str(complex_number[1]) + "i"
        elif get_imaginary(complex_number) < -1:
            negative_imaginary = str(complex_number[1])
            negative_imaginary = negative_imaginary[:0] + negative_imaginary[1:]
            return "z = " + str(complex_number[0]) + " - " + negative_imaginary + "i"
        elif get_imaginary(complex_number) == 1:
            return "z = " + str(complex_number[0]) + " + i"
        elif get_imaginary(complex_number) == -1:
            return "z = " + str(complex_number[0]) + " - i"
    elif get_real(complex_number) == 0:
        return "z = " + str(complex_number[1]) + "i"
    elif get_imaginary(complex_number) == 0:
        return "z = " + str(complex_number[0])


def make_random_complex_number(count: int):
    """
    Create count random complex numbers
    :param count: number of elements to be created
    :return: The list of newly created complex numbers
    """
    assert count < 40 ** 2

    complex_number_list = []

    while count > 0:
        real = r.randint(-100, 100)
        imaginary = r.randint(-100, 100)
        complex_number_list.append(new_complex_number(real, imaginary))
        count -= 1
    return complex_number_list


def add_complex_number(complex_number_list: list, complex_number):
    """
    Adds the new_complex number to the list of complex numbers
    :param complex_number_list: List of complex numbers maintained by the program
    :param complex_number: The new complex number to add
    :return: 0 on success, 1 if complex number with given center already exists
    """
    if complex_number in complex_number_list:
        return 1
    complex_number_list.append(complex_number)
    return 0


def delete_complex_number(complex_number_list: list, complex_number):
    """
    Deletes a complex number from the list of complex numbers
    :param complex_number_list: List of complex numbers maintained by the program
    :param complex_number: The complex number to delete
    :return: 0 on success, 1 if the complex number does not exist
    """
    if complex_number not in complex_number_list:
        return 1
    complex_number_list.remove(complex_number)
    return 0


def read_complex_number():
    """
    Reads a complex number from the console; Real and imaginary parts must
    be integers (keep reading until true)
    :return: The new complex number.
    """
    while True:
        print()

        real = input("Enter the real part: ")
        if not real.lstrip('-').isdigit():
            print("The real part must be an integer.")
            continue
        real = int(real)

        imaginary = input("Enter the imaginary part: ")
        if not imaginary.lstrip('-').isdigit():
            print("The imaginary part must be an integer:")
            continue
        imaginary = int(imaginary)

        return new_complex_number(real, imaginary)


def show_complex_number_list(complex_number_list):
    """
    Displays the complex numbers
    :param complex_number_list:
    :return:
    """
    sorted_list = sorted(complex_number_list, key=lambda c: get_real(c), reverse=True)
    return "Current list of complex numbers:\n" + "\n".join(map(to_str, sorted_list))


#
# Write below this comment
# Functions to deal with complex numbers -- dict representation
# -> There should be no print or input statements in this section
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#
"""--------------------------------------DICTIONARY--------------------------------------"""


def make_random_complex_number_dict(count: int):
    """
    Create count random complex numbers
    :param count: number of elements to be created
    :return: The dictionary of newly created complex numbers
    """
    assert count < 40 ** 2

    complex_number_dict = {"Real": [], "Imaginary": []}

    while count > 0:
        real = r.randint(-100, 100)
        imaginary = r.randint(-100, 100)
        complex_number_dict["Real"].append(real)
        complex_number_dict["Imaginary"].append(imaginary)
        count -= 1
    return complex_number_dict


def add_complex_number_dict(complex_number_dict: dict, complex_number):
    """
    Adds the new_complex number to the list of complex numbers
    :param complex_number_dict: List of complex numbers maintained by the program
    :param complex_number: The new complex number to add
    :return: 0 on success, 1 if complex number with given center already exists
    """
    for i in range(len(complex_number_dict["Real"])):
        if get_real(complex_number) == complex_number_dict["Real"][i] and get_imaginary(complex_number) == \
                complex_number_dict["Imaginary"][i]:
            return 1
    complex_number_dict["Real"].append(get_real(complex_number))
    complex_number_dict["Imaginary"].append(get_imaginary(complex_number))
    return 0


def delete_complex_number_dict(complex_number_dict: dict, complex_number):
    """
    Deletes a complex number from the list of complex numbers
    :param complex_number_dict: List of complex numbers maintained by the program
    :param complex_number: The complex number to delete
    :return: 0 on success, 1 if the complex number does not exist
    """
    flag = 0
    length = len(complex_number_dict["Real"])
    for i in range(length):
        if get_real(complex_number) == complex_number_dict["Real"][i] and get_imaginary(complex_number) == \
                complex_number_dict["Imaginary"][i]:
            flag += 1
            complex_number_dict["Real"].pop(i)
            complex_number_dict["Imaginary"].pop(i)
            return 0
    if flag == 0:
        return 1


def show_complex_number_dict(complex_number_dict: dict):
    """
    Displays the complex numbers
    :param complex_number_dict:
    :return:
    """
    complex_number_list_dict = []
    length = len(complex_number_dict["Imaginary"])
    for i in range(length):
        complex_number_list_dict.append(new_complex_number(complex_number_dict["Real"][i],
                                                           complex_number_dict["Imaginary"][i]))
    sorted_list = sorted(complex_number_list_dict, key=lambda c: get_real(c), reverse=True)
    return "Current dictionary of complex numbers:\n" + "\n".join(map(to_str, sorted_list))


def dict_to_list(complex_number_dict: dict):
    """
    Pair the real part with the imaginary part in lists and returns the list with all the numbers
    :param complex_number_dict:
    :return: list containing the dictionary elements
    """
    complex_number_list = []
    length = len(complex_number_dict["Real"])
    for i in range(length):
        real = complex_number_dict["Real"][i]
        imaginary = complex_number_dict["Imaginary"][i]
        complex_number_list.append(new_complex_number(real, imaginary))
    return complex_number_list


#
# Write below this comment
# Functions that deal with subarray/subsequence properties
# -> There should be no print or input statements in this section
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#
def getFreq(number1, number2):
    """
    Sticks the numbers on to each other and does the frequency array  of it.
    :param number1:
    :param number2:
    :return: frequency array
    """
    number1 = abs(number1)
    number2 = abs(number2)
    if number2 != 0:
        digits = len(str(number2))
    else:
        digits = 0
    number = number1 * (10 ** digits) + number2
    freq = [0] * 10
    while number > 0:
        freq[number % 10] = 1
        number = number // 10
    return freq


def subsets(complex_list):
    """
    Gets the subsets of the list
    :param complex_list:
    :return: the subsets
    """
    sets = []
    for i in range(2 ** len(complex_list)):
        subset = []
        for j in range(len(complex_list)):
            if i & (1 << j) > 0:
                subset.append(complex_list[j])
        sets.append(subset)
    return sets


def freqFlag(freq1, freq2):
    """
    Checks if the frequency arrays are equal.
    :param freq1:
    :param freq2:
    :return: True if equal, False otherwise
    """
    for i in range(10):
        if freq1 == freq2:
            return True
    return False


def longest_subarray(complex_subsets):
    """
    Determines the longest subarray satisfying the problem statement
    :param complex_subsets: subsets of the list of complex numbers
    :return: the longest subset satisfying the problem statement
    """
    index = 0
    length_max = 1
    flag = 1
    for i in range(1, len(complex_subsets)):
        if len(complex_subsets[i]) > length_max:
            for j in range(len(complex_subsets[i]) - 1):
                freq_a = getFreq(get_real(complex_subsets[i][j]), get_imaginary(complex_subsets[i][j]))
                freq_b = getFreq(get_real(complex_subsets[i][j + 1]), get_imaginary(complex_subsets[i][j + 1]))
                if not freqFlag(freq_a, freq_b):
                    flag = 0
                    break
            if flag == 1:
                index = i
                length_max = len(complex_subsets[i])
            flag = 1
    return complex_subsets[index]


def longest_alternating_list(complex_number_list):
    """
    Does the length of the longest subarray
    inc = length of the longest alternative subsequence so far with current value being GREATER than its previous value
    dec = length of the longest alternative subsequence so far with current value being SMALLER than its previous value
    "inc" increased if the last element in the alternative sequence was SMALLER than its previous element
    “dec” increased if the last element in the alternative sequence was GREATER than its 1previous element
    :param complex_number_list:
    :return: max between inc and dec
    """
    modulus_list = []
    for i in range(len(complex_number_list)):
        modulus_list.append(get_real(complex_number_list[i]) ** 2 + get_imaginary(complex_number_list[i]) ** 2)
    inc = 1
    dec = 1
    # print(modulus_list)
    for i in range(1, len(modulus_list)):
        if modulus_list[i] > modulus_list[i - 1]:
            inc = dec + 1
        elif modulus_list[i] < modulus_list[i - 1]:
            dec = inc + 1
    return max(inc, dec)


def longest_alternating_dict(complex_number_dict):
    """
    Does the length of the longest subarray
    inc = length of the longest alternative subsequence so far with current value being GREATER than its previous value
    dec = length of the longest alternative subsequence so far with current value being SMALLER than its previous value
    "inc" increased if the last element in the alternative sequence was SMALLER than its previous element
    “dec” increased if the last element in the alternative sequence was GREATER than its 1previous element
    :param complex_number_dict:
    :return: max between inc and dec
    """
    modulus_list = []
    for i in range(len(complex_number_dict["Real"])):
        modulus_list.append(complex_number_dict["Real"][i] ** 2 + complex_number_dict["Imaginary"][i] ** 2)
    # print(modulus_list)
    inc = 1
    dec = 1
    for i in range(1, len(modulus_list)):
        if modulus_list[i] > modulus_list[i - 1]:
            inc = dec + 1
        elif modulus_list[i] < modulus_list[i - 1]:
            dec = inc + 1
    return max(inc, dec)


#
# Write below this comment
# UI section
# Write all functions that have input or print statements here
# Ideally, this section should not contain any calculations relevant to program functionalities
#


def UI():
    complex_number_list = make_random_complex_number(10)
    complex_number_dict = make_random_complex_number_dict(10)
    while True:
        print("Please make your choice.")
        print()
        print("1. List representation of complex numbers.")
        print("2. Dictionary representation of complex numbers.")
        print()
        print("3. Exit.")
        print()
        repr_choice = input()
        if repr_choice == '1':
            while True:
                print("Please make your choice.")
                print()
                print("1. Add complex numbers.")
                print("2. Delete a complex number.")
                print("3. Display the list of complex numbers")
                print("4. Length and elements of a longest subarray of numbers"
                      "where both their real and imaginary parts can be written using the same base 10 digits.")
                print("5. The length of a longest alternating subsequence, when considering each number's modulus.")
                print()
                print("6. Choose another representation")
                print("7. Exit")
                print()

                choice = input()

                if choice == '1':
                    while True:
                        complex_number = read_complex_number()
                        exists = add_complex_number(complex_number_list, complex_number)
                        if exists:
                            print("The complex number is already in the list.")
                            print()
                        else:
                            print("Complex number added.")
                            print()
                        print("Do you want to add another number? y/n")
                        continue_choice = input()
                        if continue_choice == 'y':
                            pass
                        elif continue_choice == 'n':
                            print("You will be returned to the menu.")
                            print()
                            print()
                            t.sleep(0.5)
                            break
                        else:
                            print("Entrance", continue_choice, "not valid. You will be returned to the menu.")
                            print()
                            print()
                            t.sleep(0.5)
                            break
                elif choice == '2':
                    complex_number = read_complex_number()
                    exists = delete_complex_number(complex_number_list, complex_number)
                    if exists:
                        print("The complex number isn't in the list.")
                        print()
                    else:
                        print("Complex number deleted.")
                        print()
                elif choice == '3':
                    print(show_complex_number_list(complex_number_list))
                elif choice == '4':
                    complex_subsets = subsets(complex_number_list)
                    longest_subset = longest_subarray(complex_subsets)
                    if len(longest_subset) == 0:
                        print("There is no such subarray.")
                        print()
                    else:
                        print("The length of the longest subarray satisfying the condition is: ", len(longest_subset))
                        print("The elements of the  longest subarray satisfying the condition are: ")
                        print(show_complex_number_list(longest_subset))
                        print()
                elif choice == '5':
                    print("The longest alternating sequence has the length of:", longest_alternating_list(complex_number_list))
                    print()
                elif choice == '6':
                    break
                elif choice == '7':
                    print("Quitting...")
                    return
                else:
                    print("Entrance", choice, "not valid. Try again")
        elif repr_choice == '2':
            while True:
                while True:
                    print("Please make your choice.")
                    print()
                    print("1. Add complex numbers.")
                    print("2. Delete a complex number.")
                    print("3. Display the dictionary of complex numbers")
                    print("4. Length and elements of a longest subarray of numbers"
                          "where both their real and imaginary parts can be written using the same base 10 digits.")
                    print("5. The length of a longest alternating subsequence, when considering each number's modulus.")
                    print()
                    print("6. Choose another representation")
                    print("7. Exit")
                    print()

                    choice = input()

                    if choice == '1':
                        while True:
                            complex_number = read_complex_number()
                            exists = add_complex_number_dict(complex_number_dict, complex_number)
                            if exists:
                                print("The complex number is already in the dictionary.")
                                print()
                            else:
                                print("Complex number added.")
                                print()
                            print("Do you want to add another number? y/n")
                            continue_choice = input()
                            if continue_choice == 'y':
                                pass
                            elif continue_choice == 'n':
                                print("You will be returned to the menu.")
                                print()
                                print()
                                t.sleep(0.5)
                                break
                            else:
                                print("Entrance", continue_choice, "not valid. You will be returned to the menu.")
                                print()
                                print()
                                t.sleep(0.5)
                                break
                    elif choice == '2':
                        complex_number = read_complex_number()
                        exists = delete_complex_number_dict(complex_number_dict, complex_number)
                        if exists:
                            print("The complex number isn't in the dictionary.")
                            print()
                        else:
                            print("Complex number deleted.")
                            print()
                    elif choice == '3':
                        print(show_complex_number_dict(complex_number_dict))
                    elif choice == '4':
                        complex_subsets = subsets(dict_to_list(complex_number_dict))
                        longest_subset = longest_subarray(complex_subsets)
                        if len(longest_subset) == 0:
                            print("There is no such subarray.")
                            print()
                        else:
                            print("The length of the longest subarray satisfying the condition is: ",
                                  len(longest_subset))
                            print("The elements of the  longest subarray satisfying the condition are: ")
                            print(show_complex_number_list(longest_subset))
                            print()
                    elif choice == '5':
                        print("The longest alternating sequence has the length of:", longest_alternating_dict(complex_number_dict))
                        print()
                    elif choice == '6':
                        break
                    elif choice == '7':
                        print("Quitting...")
                        return
                    else:
                        print("Entrance", choice, "not valid. Try again")
        elif repr_choice == '3':
            print("Quitting...")
            return
        else:
            print("Entrance", repr_choice, "not valid. Try again")


if __name__ == "__main__":
    UI()
