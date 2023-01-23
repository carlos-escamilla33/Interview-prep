class Node:
   def __init__(self, data = 0, next = None):
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
    def printList(self):
        if not self.head:
            return
        current = self.head
        while current is not None:
            print(current.data, "-->", end=" ")
            current = current.next
        print("None")

    def search(self, target):
        current = self.head
        while current.next:
            if current.data == target:
                return True
            current = current.next
        return False
    
    def remove(self, target):
        if self.head == target: #if the head of the linked list is the target
            self.head = self.head.next #set the head to the next node after that to remove it
            return
        current = self.head #assign the current head to the variable current
        previous = None
        while current:
            if current.data == target:
                previous.next = current.next
            previous = current
            current = current.next

list1 = LinkedList()
list1.append(1)
list1.append(2)
list1.append(4)
list2 = LinkedList()
list2.append(1)
list2.append(3)
list2.append(4)

def mergeTwoLists(list1, list2):
    head = Node()
    current1 = list1
    current2 = list2
    while current1 and current2:
        if current1.data > current2.data:
            head.next = Node(current1.data)
        elif current1.data < current2.data:
            head.next = Node(current2.val)
        current1 = current1.next
        current2 = current2.next
        head = head.next
    
    if not current1:
        head.next = current1
    elif not current2:
        head.next = current2
    
    return head.next

# print(mergeTwoLists(list1, list2))

