import random as r


def dataInput():
    length = r.randint(3, 5)
    array = r.sample(range(1, 100), length)
    return array


def freqFlag(array1, array2):
    for i in range(10):
        if array1[i] > 0 and array2[i] > 0:
            return True


def getFreq(number):
    freq = [0] * 10
    while number > 0:
        freq[number % 10] = 1
        number = number // 10
    return freq


def subsets(array):
    sets = []
    for i in range(2 ** len(array)):
        subset = []
        for j in range(len(array)):
            if i & (1 << j) > 0:
                subset.append(array[j])
        sets.append(subset)
    return sets


def dataOutput(array):
    print(*array, sep=',')


def problem(array):
    outputFlag = 0
    for g in range(1, len(array)):
        i = 0
        if len(array[g]) == 1:
            pass
        elif len(array[g]) == 2:
            freqA = getFreq(array[g][0])
            freqB = getFreq(array[g][1])
            if freqFlag(freqA, freqB):
                dataOutput(array[g])
                outputFlag = 1
        elif len(array[g]) > 2:
            flag = True
            while flag and i <= len(array[g]) - 2:
                freqA = getFreq(array[g][i])
                freqB = getFreq(array[g][i + 1])
                if freqFlag(freqA, freqB):
                    i += 1
                else:
                    flag = False
            if flag:
                dataOutput(array[g])
                outputFlag = 1
    if outputFlag == 0:
        return 0


def problemRecursive(array, index):
    i = 0
    if index <= len(array) - 1:
        if len(array[index]) == 1:
            pass
        elif len(array[index]) == 2:
            freqA = getFreq(array[index][0])
            freqB = getFreq(array[index][1])
            if freqFlag(freqA, freqB):
                dataOutput(array[index])
        elif len(array[index]) > 2:
            flag = True
            while flag and i <= len(array[index]) - 2:
                freqA = getFreq(array[index][i])
                freqB = getFreq(array[index][i + 1])
                if freqFlag(freqA, freqB):
                    i += 1
                else:
                    flag = False
            if flag:
                dataOutput(array[index])
        problemRecursive(array, index + 1)


def main():
    numbers = dataInput()
    numbers.sort()
    array = subsets(numbers)
    print(numbers)
    print(array)

    index = 0

    print("Iterative results:")
    problem(array)
    if problem(array) == 0:
        print("There are no possible solutions.")

    print("")

    print("Recursive results:")
    problemRecursive(array, index)
    if problem(array) == 0:
        print("There are no possible solutions.")


if __name__ == '__main__':
    main()
