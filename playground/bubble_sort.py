from sorting_data import data_set, smaller_set

data = data_set
data2 = smaller_set

def swap(elem1, elem2):
    temp = elem1
    elem1 = elem2
    elem2 = temp
    return 3

def bubbleSort(arr):
    n = len(arr)
    swapped = False
    swapCount = 0
    comparisonCount = 0

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisonCount += 1
            if arr[j] > arr[j + 1]:
                swapCount += swap(arr[j], arr[j + 1])
                swapped = True
        if not swapped:
            break
    
    print("Moves: ", swapCount)
    print("Comparisons:", comparisonCount)

bubbleSort(data2)

# DATA_SET
# Moves: 737,169
# Comparisons: 498,498

# Alg 4

# SMALLER_SET
# Moves: 
# Comparisons: 