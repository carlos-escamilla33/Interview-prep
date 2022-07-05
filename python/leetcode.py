
# ----------------Leetcode #20 Valid Parentheses ---------------- #

def isValid(string):
    bracePairs = {
        "]": "[", 
        ")": "(",
        "}": "{",
    }
    stack = []

    for char in string:
        if char in bracePairs and stack:
            if bracePairs[char] != stack[-1]:
                return False
            else:
                stack.pop()
        else:
            stack.append(char)

    return True if not stack else False

# ----------------Leetcode #21 Merge Two Sorted Lists ---------------- #

# Create list node
class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None

def mergeTwoSortedLists(list1, list2):

    node = ListNode()
    head = node

    while list1 != None and list2 != None:
        if list1.val < list2.val:
            head.next = list1
            list1 = list1.next
        else:
            head.next = list2
            list2 = list2.next

        head = head.next
    

    if list1:
        head.next = list1
    elif list2:
        head.next = list2
        
    return node.next

# ----------------Leetcode # 121 Best Time to Buy and Sell Stock ----------------

prices = [7,1,5,3,6,4]

def maxProfit(prices):

    maxProfit = 0
 
    currMin = prices[0]


    for i in range(len(prices)):
        price = prices[i]
        currProfit = price - currMin
        
        if currProfit > maxProfit:
            maxProfit = currProfit
    
        elif price < currMin:
            currMin = price
    
    return maxProfit

# ----------------Leetcode # 217 Contains Duplicate ----------------

# TIME - O(N)
# SPACE - O(N)

def containsDuplicate(nums):

    hashtable = {}


    for idx in range(len(nums)):
        num = nums[idx]

        if num in hashtable:
            return True

        hashtable[num] = idx
    

    return False


# ----------------Leetcode # 242 Valid Anagram ----------------

# TIME - O(N)
# SPACE - O(N)

# Frequency counter

def frequencyCounter(string):

    hashtable = {}

    for letter in string:
        if letter in hashtable:
            hashtable[letter]+=1
        else:
            hashtable[letter] = 1

    return hashtable

def isAnagram(word1, word2):


    if len(word1) != len(word2):
        return False

    firstCount = frequencyCounter(word1)
    secondCount = frequencyCounter(word2)
    
    for char in firstCount:
        if char not in secondCount or firstCount[char] != secondCount[char]:
            return False
    

    return True
    
# ----------------Leetcode # 125 Valid Palindrome ----------------

# TIME - O(N)
# SPACE = O(N)

# a palindrome is a word that reads the same backward and forward

# BRUTE FORCE SOLUTION

# def isPalindrome(word):
#     # remove non-alphanumeric characters
#     originalWord = ""
#     reversedWord = ""

#       # Iterate through letter in word
#     for letter in word:
#         # if the letter is alphanumeric
#         if letter.isalnum():
#             # add to originalWord and lower
#             originalWord+=letter.lower()

#     # Iterate through letters in word in reverse order
#     for letter in reversed(word):
#         # if the letter is alphanumeric
#         if letter.isalnum():
#             # add it to the reversedWord and lower
#             reversedWord+=letter.lower()

#     # Compare the reversed word to the original word without nonalphanumeric characters
#     return reversedWord == originalWord


def isPalindrome(word):

    nonAlphaNumWord = ""

    for letter in word:
        if letter.isalnum():
            nonAlphaNumWord+=letter.lower()

    L = 0
    R = len(nonAlphaNumWord) - 1

    while (L < R):
        if nonAlphaNumWord[L] == nonAlphaNumWord[R]:
            L+=1
            R-=1
        else:
            return False

   
    return True




# ----------------Leetcode # 155 MinStack ----------------

# TIME - 0(1)
#SPACE - O(N)

class MinStack:

    def __init__(self):

        self.stack = []
        self.minValsStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minValsStack:
            val = min(val, self.minValsStack[-1])
            self.minValsStack.append(val)
        else:
            self.minValsStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minValsStack.pop()
    
    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.minValsStack[-1]
    


# ----------------Leetcode #704 Binary Search Binary Search ----------------
# import the math module
import math
from xml.dom import minidom

def binarySearch(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = math.floor((right + left) / 2)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    
    return -1

# ----------------Leetcode #278 First Bad Version ----------------

# TIME - O(LOGN)
# SPACE - O(1)

# PLACE HOLDER API
def isBadVersion(version): 
    return True

def firstBadVersion(n):
    l = 1
    r = n
    firstBadVersion = 0

    while l <= r:
        currentVersion = math.floor((r + l) / 2)

        if isBadVersion(currentVersion):
            r = currentVersion - 1
            firstBadVersion = currentVersion
        else:
            l = currentVersion + 1
    
    return l

# ----------------Leetcode #Search Insert Position ----------------


# TIME - O(LOGN)
#SPACE - O(1)

def searchInsert(nums, target):

    leftPointer = 0
    rightPointer = len(nums) - 1

    while leftPointer <= rightPointer:
        mid = math.floor((rightPointer + leftPointer) / 2)

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            leftPointer = mid + 1
        elif nums[mid] > target:
            rightPointer = mid - 1
    
    return leftPointer




