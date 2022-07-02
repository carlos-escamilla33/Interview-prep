
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
    # Create a dummy node that just holds None
    node = ListNode()
    # Assign the tail to the node node
    tail = node

    # While list1 and list2 are not null
    while list1 != None and list2 != None:
        # if the value in list1 is greater than the value at list2
        if list1.val < list2.val:
            # Update next node in tail to the current node list1
            tail.next = list1
            # Update list1 head to the next node
            list1 = list1.next
        # if list2.val less than or equal to list1.val
        # Update next node in tail to be the current node at list2
        elif list2.val <= list1.val:
            tail.next = list2
            # Update list2 head to the next node
            list2 = list2.next
        
        # Update tail to move on to the next node
        tail = tail.next
    
    # if list1 is still not empty
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2
    
    # return the head of the next node in the node
    # first one is None
    return node.next

# ----------------Leetcode # 121 Best Time to Buy and Sell Stock ----------------

prices = [7,1,5,3,6,4]

def maxProfit(prices):
    # Initialize max profit
    maxProfit = 0
    # set the min, which is currently the first number
    currMin = prices[0]

    # Iterate through the indexes of array
    for i in range(len(prices)):
        # Initialize the current price index
        price = prices[i]
        # Initialize the current profit which is price - currMin
        currProfit = price - currMin
        # If the current profit is more than the max profit
        # assign the current profit to max profit
        if currProfit > maxProfit:
            maxProfit = currProfit
        # if price is less than the min than we assign the price to current min
        elif price < currMin:
            currMin = price
    
    return maxProfit

# ----------------Leetcode # 217 Contains Duplicate ----------------

# TIME - O(N)
# SPACE - O(N)

def containsDuplicate(nums):
    # Initialize object/dictionary data structure to hold numbers
    hashtable = {}

    # Iterate through nums array/list
    for idx in range(len(nums)):
        num = nums[idx]
        # if the num is already in the dictionary/object we know the list/arr doesnt hold distinct numbers
        if num in hashtable:
            # return true because the arr/list holds a duplicate
            return True
        # If we dont have it in the set we add it
        # There is no need to add an else because the last if statement will shortcircut the algorithm
        hashtable[num] = idx
    
    # return false if we didnt find a duplicate
    return False


# ----------------Leetcode # 242 Valid Anagram ----------------

# TIME - O(N)
# SPACE - O(N)

# Frequency counter

def frequencyCounter(string):
    # create a hashtable
    hashtable = {}
    # Iterate through string
    for letter in string:
        # If the letter is already in the hashtable increment the value by 1
        if letter in hashtable:
            hashtable[letter]+=1
        # If the letter is not in the hashtable add it and initialize the value to 1
        else:
            hashtable[letter] = 1
    # return the frequency count
    return hashtable

def isAnagram(word1, word2):

    # If they are not the same length they are not anagrams of each other
    if len(word1) != len(word2):
        return False

    # get the frequency count of the letters
    firstCount = frequencyCounter(word1)
    secondCount = frequencyCounter(word2)
    
    # Check to see if the letter count matches from both words
    for char in firstCount:
        if char not in secondCount or firstCount[char] != secondCount[char]:
            return False
    
    # If the counts match then we return True
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
    # remove non-alphanumeric characters
    nonAlphaNumWord = ""

    for letter in word:
        # if the letter is alphanumeric
        if letter.isalnum():
            # add to originalWord and lower
            nonAlphaNumWord+=letter.lower()

    # Initalize Left and Right pointers
    L = 0
    R = len(nonAlphaNumWord) - 1

    # While Left pointer is less than Right pointer
    while (L < R):
        # If the letters on each side are equal
        if nonAlphaNumWord[L] == nonAlphaNumWord[R]:
            # move up the left pointer by one
            L+=1
            # move down the right pointer by one
            R-=1
        # if they dont match we return false
        else:
            return False

    # If none of the last conditions are met we return true because its a palindome
    return True




# ----------------Leetcode # 155 MinStack ----------------

# TIME - 0(1)
#SPACE - O(N)

class MinStack:

    def __init__(self):
        # Initialize stack and minimum vals stack
        self.stack = []
        self.minValsStack = []

    def push(self, val: int) -> None:
        # add val to the end of the normal stack
        self.stack.append(val)

        # if our stack is not empty
        if self.minValsStack:
            # get the minimum value between val and the last number in our min values stack and reassign val
            val = min(val, self.minValsStack[-1])
            # add the lesser number to our minValsStack
            self.minValsStack.append(val)
        # if our stack is empty we just append the val coming in as a parameter
        else:
            self.minValsStack.append(val)

    def pop(self) -> None:
        # take out the last item of the stack of each
        self.stack.pop()
        self.minValsStack.pop()
    
    def top(self) -> int:
        # return the last item in the stack
        return self.stack[-1]
    
    def getMin(self) -> int:
        # return the last item in our minValsStack
        # we kept track of the lowest number by comparing the incoming val with
        # with the top of our min vals stack to stay up to date on the min val
        return self.minValsStack[-1]
    


# ----------------Leetcode #704 Binary Search Binary Search ----------------
# import the math module
import math
from xml.dom import minidom

def binarySearch(nums, target):
    # Initalize left and right pointers
    left = 0
    right = len(nums) - 1

    # while the left is not greater than the right
    while left <= right:
        mid = math.floor((right + left) / 2)
        # if the mid number we are at is the target return it
        if nums[mid] == target:
            return mid
        # if the current number we are at is less than the target
        elif nums[mid] < target:
            # assign the mid plus one to the left pointer
            left = mid + 1
        # if the current number we are at is greater than the target
        elif nums[mid] > target:
            # assign the mid minus one to the right pointer
            right = mid - 1
    
    # if we exit the while loop the number is not in our nums array
    # so we return negative one
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
    
    return firstBadVersion










