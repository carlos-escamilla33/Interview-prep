class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next


a = Node(4)
b = Node(10)
c = Node(3)
d = Node(40)

a.next = b
b.next = c
c.next = d

def printLL(head):
    current = head
    while current:
        print(current.val)
        current = current.next

def printRecursively(head):
    if not head:
        return
    print(head.val)
    printRecursively(head.next)

# printRecursively(a)
# printLL(a)

# Linked List Values
# Write a function, linkedlistValues, that takes in the head of a linked list as an argument.
# The function should return an array containing all values of the nodes in the linked list

def linkedListValues(head):
    nodeArr = []
    current = head
    while current:
        nodeArr.append(current.val)
        current = current.next
    print(nodeArr)

def fillValues(head, nodeArr):
    if not head:
        return nodeArr
    nodeArr.append(head.val)
    fillValues(head.next, nodeArr)

def linkedListValuesRecurr(head):
    nodeArr = []
    fillValues(head, nodeArr)
    print(nodeArr)


# linkedListValues(a)

# linkedListValuesRecurr(a)

# Add up the nodes in the linked list and return them

def sumLinkedListVals(head):
    total = 0
    current = head
    while current:
        total+=current.val
        current = current.next
    return total

def sumLinkedListValsRecurr(head):
    if not head:
        return 0
    return head.val + sumLinkedListValsRecurr(head.next)

# print(sumLinkedListVals(a))
# print(sumLinkedListValsRecurr(a))

# Find target value in linked list

# O(N) runtime
# O(1) memory

def findTarget(head, target):
    current = head
    while current:
        if current.val == target:
            return True
        current = current.next
    return False

def findTargetRecurr(head, target):
    if not head:
        return False
    elif head.val == target:
        return True
    return findTargetRecurr(head.next, target)
    

# print(findTarget(a, 90))

# print(findTargetRecurr(a, 3))

# Find the node by index in the linked list

def findByIdx(head, idx):
    count = 0
    current = head
    while current:
        if count == idx:
            return current.val
        count+=1
        current = current.next
    return f"Index {idx} is out of range"

def findByIdxRecurr(head, idx):
    if not head:
        return "Idx not in range"
    elif idx == 0:
        return head.val
    idx-=1
    return findByIdx(head.next, idx)

# print(findByIdx(a, 2))
# print(findByIdxRecurr(a, 9))


