
# Example of what nodes look like under the hood
# They look like dictionaries that point to other dictionaries
# Think of it like a set of nested dictionaries
head = {
    "value": 11,
    "next": {
        "value": 3,
        "next": {
            "value": 23,
            "next": {
                "value": 7,
                "next": None

            }
        }
    }
}

# Creating Node class

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Creating Linked List Class

class LinkedList:
    def __init__(self, value = 0):
        # create a new node
        new_node = Node(value)
        # assigning head/tail/length
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        tempPtr = self.head
        
        while tempPtr:
            print(tempPtr.value)
            tempPtr = tempPtr.next

    def append(self, value):
        node = Node(value) # create a new node

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.length+=1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        
        headPtr = self.head
        tempPtr = self.head

        while tempPtr.next: # wont run if the next node is None
            headPtr = tempPtr # moves the headPtr to the place of the tempPtr/ saves current tmp
            tempPtr = tempPtr.next # moves tempPtr to the next node

        self.tail = headPtr # assigns the tail to the node bofore the last tail node
        self.tail.next = None # deletes the next node by setting it to None
        self.length -=1

        if self.length == 0:
            self.head = None
            self.tail = None

        return tempPtr
             
    def prepend(self, value):
        node = Node(value) # create new node
        
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

        self.length+=1
        return True
    
    def pop(self):
        tempPtr = self.head

        if self.length == 0:
            return None
        
        self.head = self.head.next
        tempPtr.next = None
        self.length-=1
            
        if self.length == 0:
            self.tail = None

        return tempPtr

    # def insert(self, index, value):
    #     # create new node
    #     # insert node

ll = LinkedList(9)
ll.append(3)
ll.append(2)
ll.prepend(4)
ll.pop()
ll.print_list()

