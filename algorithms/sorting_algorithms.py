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



# print(bubbleSort([32,1,9,6]))

def insertionSort(arr):
    for i in range(1, len(arr)):
        value = arr[i]
        while i > 0 and arr[i-1] > value:
            arr[i] = arr[i-1]
            i-=1
        arr[i] = value
    return arr

# print(insertionSort([6,5,8,2]))




