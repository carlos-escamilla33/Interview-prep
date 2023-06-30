
class Node:
    def __init__(self, val = 0):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, val):
        new_node = Node(val)
        self.head = new_node
    
    def append(self, val):
        node = Node(val)

        if self.head is None:
            self.head = node
        
        curr = self.head

        while curr:
            if curr.next == None:
                curr.next = node
                return True
            curr = curr.next
    
    def printLL(self):
        curr = self.head

        while curr:
            print(curr.val)
            curr = curr.next

    def find_middle_node(self):
        slow = self.head
        fast = self.head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        print(slow.val)
    

ll = LinkedList(1)
ll.append(2)
# ll.append(3)
ll.append(4)
ll.append(5)
ll.find_middle_node()