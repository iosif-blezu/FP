#A2 assignment
import copy
import random as r
import time

maxInt = 9223372036854775807

def cocktailSort(array, step):  #cocktail sort algorithm
    starttime = time.time()
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
    endtime = time.time()
    duration = endtime - starttime
    return duration


def combSort(array, step): #combsort algorithm
    starttime = time.time()
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
    endtime = time.time()
    duration = endtime - starttime
    return duration

def worstCase(alg):
    length = 500
    time = 0
    while length <= 8000:
        list = dataInput(length)
        list.sort(reverse=True)
        #print(*list, sep=", ")
        if alg == 1:
            sortTime = cocktailSort(list, maxInt)
            time = time + sortTime
            timeOutput(length, sortTime)
        else:
            sortTime = combSort(list, maxInt)
            time = time + sortTime
            timeOutput(length, sortTime)

        length *= 2
    return time / 5

def averageCase(alg):
    length = 500
    time = 0
    while length <= 8000:
        list = dataInput(length)
        #print(*list, sep=", ")
        if alg == 1:
            sortTime = cocktailSort(list, maxInt)
            time = time + sortTime
            timeOutput(length, sortTime)
        else:
            sortTime = combSort(list, maxInt)
            time = time + sortTime
            timeOutput(length, sortTime)
        length *= 2
    return time / 5

def bestCase(alg):
    length = 500
    time = 0
    while length <= 8000:
        list = dataInput(length)
        list.sort()
        # print(*list, sep=", ")
        if alg == 1:
            sortTime = cocktailSort(list, maxInt)
            time = time + sortTime
            timeOutput(length, sortTime)
        else:
            sortTime = combSort(list, maxInt)
            time = time + sortTime
            timeOutput(length, sortTime)
        length *= 2
    return time / 5

def dataInput(n): #data input function

    list = []
    for i in range(n):
        element = r.randint(0, 100)
        list.append(element)
    return list

def timeOutput(length, sortTime):
    print("For length =", length, "it takes:", sortTime, "seconds")
def dataOutput(array):
    print(*array, sep=", ")


def main():
    list = []

    while True:
        print("1. Generate a list of random natural numbers.")
        print("2. Sort the list using the Cocktail Sort algorithm.")
        print("3. Sort the list using the Comb Sort algorithm.")
        print("4. Get the average runtime of CocktailSort.")
        print("5. Get the average runtime of CombSort.")
        print("6. Exit the program.")
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
            cocktailSort(list, step)
        elif choice == 3:
            print("Which step do you want to proceed to?")
            step = int(input())
            combSort(list, step)
        elif choice == 4:
            print("Which case do you want to be tested?")
            print("")
            print("1. The Worst Case")
            print("2. The Average Case")
            print("3. The Best Case")

            secondchoice = int(input())

            if secondchoice == 1:
                print("The average time is:", worstCase(1), "seconds")
            elif secondchoice == 2:
                print("The average time is:", averageCase(1), "seconds")
            elif secondchoice == 3:
                print("The average time is:", bestCase(1), "seconds")
        elif choice == 5:
            print("Which case do you want to be tested?")
            print("")
            print("1. The Worst Case")
            print("2. The Average Case")
            print("3. The Best Case")

            secondchoice = int(input())

            if secondchoice == 1:
                print("The average time is:", worstCase(2), "seconds")
            elif secondchoice == 2:
                print("The average time is:", averageCase(2), "seconds")
            elif secondchoice == 3:
                print("The average time is:", bestCase(2), "seconds")

        elif choice == 6:
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