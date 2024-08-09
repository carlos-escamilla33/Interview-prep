from algorithms.sorting_data import data_set, smaller_set

def insertionSort(arr):
    n = len(arr)
    comparisonCount = 0
    movesCount = 0

    for i in range(1, n):
        curr = arr[i]

        j = i - 1
        while j >= 0 and curr < arr[j]:
            arr[j + 1] = arr[j]
            comparisonCount += 1
            movesCount += 3
            j -= 1
        arr[j + 1] = curr
        movesCount += 3

    print("Moves:", movesCount)
    print("Comparisons:", comparisonCount)


insertionSort(data_set)



# Moves: 760659
# Comparisons: 252555

# Alg 5