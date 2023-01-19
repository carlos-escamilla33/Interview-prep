class Node:
   def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head: #if there is no head to the LL
            self.head = Node(data) #add the data param as the head
            return #stop running the method
        current = self.head # set the head of the linked list to the variable current
        while current.next: #while the next node of the linked list is not None / Null keep iterating
            current = current.next #set the next node as the new head of the LL
        current.next = Node(data) #once we reach the end of the loop, we are at the end of the LL
                                  #set the last nodes next to be the new Node holding the data
                                  #the next of the last node will automatically be None