
# def findAverages(arr, k):
#     res = []
#     for i in range(len(arr) - k + 1):
#         _sum = 0.0
#         for j in range(i, i + k):
#             _sum += arr[j]
#         res.append(_sum / k)
#     return res

def findAverages(arr, k):
    res = []
    windowStart = 0
    currSum = 0.0
    for windowEnd in range(len(arr)):
        currSum += arr[windowEnd]
        if (windowEnd - windowStart) + 1 == k:
            res.append(currSum / k)
            currSum -= arr[windowStart]
            windowStart += 1
    return res

arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]

# print(findAverages(arr, 5))

def findMaxSumSubArray(arr, k):
    maxSum = -1
    currMax = 0
    windowStart = 0

    for windowEnd in range(len(arr)):
        currMax += arr[windowEnd]
        if windowEnd >= k - 1:
            maxSum = max(maxSum, currMax)
            currMax -= arr[windowStart]
            windowStart += 1
    
    return maxSum


print(findMaxSumSubArray([2, 3, 4, 1, 5], 2))