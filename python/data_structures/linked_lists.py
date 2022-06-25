
# Creating Node class for linked list
class Node:
    def __init__(self, val=None):
        self.val = val #Assigning data
        self.next = None # Initalize next as null

#passing in value to Node class
node1 = Node(1)
# Giving node1 a next value
node1.next = 2

# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, node):
        if self.head is None:
            self.head = Node(self.head)
        else:
            current = node.val
            while current.next != None:
                current = current.next
            current.next = Node(node.val)

    def print_list(self):
        current = self.head
        while current != None:
            print(current.val)
            current = current.next
        print("None")


linkedList = LinkedList()
linkedList.append(node1)

# linkedList.print_list()

        
        
            





















