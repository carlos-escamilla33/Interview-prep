# FIFO = FIRST IN FIRST OUT
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        if len(self.items) <= 0:
            return True
        return False
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

q = Queue()

q.enqueue("1")
q.enqueue("2")

print(q.items)

q.dequeue()

print(q.items)