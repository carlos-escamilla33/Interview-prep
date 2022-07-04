
# Creating Node class for linked list

class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

# node1 = Node("3")
# node2 = Node("5")
# node3 = Node("7")
# node4 = Node("10")

# node1.nextNode = node2
# node2.nextNode = node3
# node3.nextNode = node4

# # node1 -> node2 -> node3

# currentNode = node1

# while(currentNode != None):
#     print (currentNode.value, "-->", end=" ")
#     currentNode = currentNode.nextNode
# print("None")

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            return

        currentNode = self.head
        while currentNode != None:
            if currentNode.nextNode == None:
                currentNode.nextNode = node
                break
            else:
                currentNode = currentNode.nextNode

    def printList(self):
        currentNode = self.head
        
        while currentNode != None:
            print(currentNode.value, "-->", end=" ")
            currentNode = currentNode.nextNode
        print("None")
    
    def delete(self, value):
        currentNode = self.head

        while currentNode != None:
            if currentNode.nextNode.value == value:
                currentNode.nextNode = currentNode.nextNode.nextNode
                break
            else:
                currentNode = currentNode.nextNode



linkedList = LinkedList()

# linkedList.printList()
linkedList.insert("3")
linkedList.insert("5")
linkedList.insert("8")
linkedList.insert("12")
linkedList.printList()
linkedList.delete("5")
linkedList.printList()


            





















