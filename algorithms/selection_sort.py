from sorting_data import data_set

def selectionSort(arr):
    comparisonCount = 0
    movesCount = 0

    for i in range(len(arr) - 1):
        minIdx = i
        for j in range(i + 1, len(arr)):
            comparisonCount += 1
            if arr[minIdx] > arr[j]:
                minIdx = j
        arr[i], arr[minIdx] = arr[minIdx], arr[i]
        movesCount += 3
    
    print("Comparisons", comparisonCount)
    print("Moves", movesCount)

selectionSort(data_set)

# Moves: 737,169
# Comparisons: 498,498