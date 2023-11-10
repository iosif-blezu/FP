#A2 assignment
import copy
import random as r

def cocktailSort(array, step):  #cocktail sort algorithm
    length = len(array)
    swap = True
    start = 0 #first
    end = length - 1 #last
    flag = 0
    increment = step
    if step == 0:
        return array

    while swap == True:
        swap = False
        for a in range(start, end):
            if array[a] > array[a+1]:
                array[a], array[a+1] = array[a+1], array[a]
                swap = True
                flag += 1
                if flag == step:
                    dataOutput(array)
                    step = step + increment
        if swap == False:
            end = end-1
        for a in range(end-1, start-1, -1):
            if array[a] > array[a+1]:
                array[a], array[a+1] = array[a+1], array[a]
                swap = True
                flag += 1
                if flag == step:
                    dataOutput(array)
                    step = step + increment
        start = start + 1

    #return array


def combSort(array, step): #combsort algorithm
    gap = len(array)
    swaps = True
    flag = 0
    increment = step
    if step == 0:
        return array

    while gap > 1 or swaps:
        gap = max(1, int(gap / 1.25))  # minimum gap is 1
        swaps = False
        for i in range(len(array) - gap):
            j = i+gap
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                swaps = True
                flag += 1
                if flag == step:
                    dataOutput(array)
                    step = step + increment
    #return array

def dataInput(n): #data input function

    list = []
    for i in range(n):
        element = r.randint(0, 100)
        list.append(element)
    return list

def dataOutput(array):
    print(*array, sep=', ')


def main():
    list = []

    while True:
        print("1. Generate a list of random natural numbers.")
        print("2. Sort the list using the Cocktail Sort algorithm.")
        print("3. Sort the list using the Comb Sort algorithm.")
        print("4. Exit the program.")
        choice = int(input())         #menu choices

        if choice == 1:
            print("Introduce the length of your array:")
            n = int(input())
            list = dataInput(n)
            print("Your generated list is:")
            print(*list, sep=', ')
        elif choice == 2:
            print("Which step do you want to proceed to?")
            step = int(input())
            #copyList = copy.deepcopy(list)
            #print(cocktailSort(list, step), sep=', ')
            cocktailSort(list, step)
        elif choice == 3:
            print("Which step do you want to proceed to?")
            step = int(input())
            #copyList = copy.deepcopy(list) #deepcopy of the list, if we change the list, the copylist won't be changed
            #print(combSort(list, step), sep=', ')
            combSort(list, step)
        elif choice == 4:
            break
        else:
            print("You are not my friend anymore :((")

        print("")
        print("Do you want to continue? y/n")
        yesorno = input()
        if yesorno == 'y':
            pass
        else:
            break

main()
