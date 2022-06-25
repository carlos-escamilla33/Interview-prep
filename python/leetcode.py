
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
    # Create a dummy node
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
        # if list2.val < list1.val
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
    



