
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
    



