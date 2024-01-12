
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


# print(findMaxSumSubArray([2, 3, 4, 1, 5], 2))

def findMinSubArray(arr, s):
    minLen = float("inf")
    currSum = 0
    windowStart = 0

    for windowEnd in range(len(arr)):
        currSum += arr[windowEnd]
        while currSum >= s:
            minLen = min(windowEnd - windowStart + 1, minLen)
            currSum -= arr[windowStart]
            windowStart += 1
    if minLen == float("inf"):
        return 0
    return minLen

# print(findMinSubArray([1, 1, 1, 1, 1, 1], 7))

def findLength(str1, k):
    windowStart = 0
    maxLength = 0
    charFrequency = {}

    for windowEnd in range(len(str1)):
        rightChar = str1[windowEnd]
        if rightChar not in charFrequency:
            charFrequency[rightChar] = 0
        charFrequency[rightChar] += 1

        while len(charFrequency) > k:
            leftChar = str1[windowStart]
            charFrequency[leftChar] -= 1
            if charFrequency[leftChar] == 0:
                del charFrequency[leftChar]
            windowStart += 1

        maxLength = max(maxLength, windowEnd - windowStart + 1)
    
    return maxLength

string="araaci"
K=1
# print(findLength(string, K))

def strStr(haystack, needle):
    firstOccuranceIdx = -1
    i = 0
    while i < len(haystack):
        j = 0
        idx = i
        while j < len(needle) and idx < len(haystack) and haystack[idx] == needle[j]:
            idx += 1
            j += 1
        if j == len(needle):
            firstOccuranceIdx = idx - j
            return idx - j
        i += 1

    return firstOccuranceIdx

def longestSubstring(s, k):
    maxLength = 0
    
    # for 
    return maxLength

s = "ababacb"
k = 3

print(longestSubstring(s, k))

def decrypt(code, k):
    n = len(code)
    result = [0] * n

    if k == 0:
        return result

    for i in range(n):
        window_sum = 0
        if k > 0:
            for j in range(1, k + 1):
                window_sum += code[(i + j) % n]
        else:
            for j in range(1, abs(k) + 1):
                window_sum += code[(i - j) % n]

        result[i] = window_sum

    return result

code = [5,7,1,4]
k = 3
# print(decrypt(code, k))
            