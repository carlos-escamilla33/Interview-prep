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

printRecursively(a)
# printLL(a)
