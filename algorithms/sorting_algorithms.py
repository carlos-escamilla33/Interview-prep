def bubbleSort(arr):
    length = len(arr) - 1
    for i in range(length):
        noSwaps = True
        for j in range(length - i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                noSwaps = False

        if noSwaps:
            return arr

    return arr



print(bubbleSort([32,1,9,6]))