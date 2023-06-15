
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
    def __init__(self, value=0):
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
        node = Node(value)  # create a new node

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None

        headPtr = self.head
        tempPtr = self.head

        while tempPtr.next:  # wont run if the next node is None
            headPtr = tempPtr  # moves the headPtr to the place of the tempPtr/ saves current tmp
            tempPtr = tempPtr.next  # moves tempPtr to the next node

        self.tail = headPtr  # assigns the tail to the node bofore the last tail node
        self.tail.next = None  # deletes the next node by setting it to None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return tempPtr

    def prepend(self, value):
        node = Node(value)  # create new node

        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

        self.length += 1
        return True

    def pop_first(self):
        tempPtr = self.head

        if self.length == 0:
            return None

        self.head = self.head.next
        tempPtr.next = None
        self.length -= 1

        if self.length == 0:
            self.tail = None

        return tempPtr

    def get(self, index):
        i = 0
        temp = self.head

        while temp:
            if i == index:
                return temp
            temp = temp.next
            i += 1

        return None

    def set_value(self, index, value):
        temp = self.get(index)

        if temp:
            temp.value = value
            return True

        return False
    
    def insert(self, index, value):
        # create new node value
        if index < 0 or index > self.length:
            return False

        if index == 0:
            return self.prepend(value)
        elif index > self.length:
            return self.append(value)
        else:
            node = Node(value)
            pre = self.get(index - 1)
            post = self.get(index)
            pre.next = node
            node.next = post
            self.length+=1

        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length-=1

        return temp
    
    def reverse(self):
        # switch head and tail
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.reverse()
ll.print_list()
