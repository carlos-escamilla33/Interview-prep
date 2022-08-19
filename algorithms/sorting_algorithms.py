def bubbleSort(arr):
    length = len(arr) - 1
    for _ in range(length):
        for j in range(length):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

    print(arr)


bubbleSort([32,1,9,6])