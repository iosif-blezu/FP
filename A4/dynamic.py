
def subsetSum(array, sum):
    length = len(array)
    subset = ([[False for i in range(sum + 1)] for i in range(length + 1)])

    for i in range(length + 1):
        subset[i][0] = True


    for i in range(1, length + 1):
        for j in range(1, sum + 1):
            if j < array[i - 1]:
                subset[i][j] = subset[i - 1][j]
            else:
                if subset[i-1][j]:
                    subset[i][j] = subset[i - 1][j]
                else:
                    subset[i][j] = subset[i-1][j - array[i-1]]

    j = sum
    i = length
    vector = []
    while j > 0 and i > 0:
        if subset[i][j] == subset[i-1][j]:
            i -= 1
        else:
            vector.append(array[i-1])
            j = j - array[i-1]

    return vector


def dataInput():
    print("Introduce the length of the list:")
    length = int(input())
    list = []
    print("Introduce the list: ")
    for i in range(length):
        element = int(input())
        list.append(element)
    return list





def main():
    array = dataInput()
    print("Introduce the sum:")
    sum = int(input())
    print("A subset with the sum equal to", sum, "is:")
    vector = subsetSum(array, sum)
    if vector == []:
        print("No such subset.")
    else:
        print(*subsetSum(array, sum), sep=', ')

if __name__ == '__main__':
    main()
