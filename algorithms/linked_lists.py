class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next


a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

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

linkedListValuesRecurr(a)


