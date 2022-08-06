# LIFO = LAST IN FIRST OUT
class Stack:
    def __init__(self):
        self.stack = []
    
    def isEmpty(self):
        if len(self.stack) <= 0:
            return True
        return False
    
    def top(self):
        return self.stack[-1]
    
    def push(self, val):
        self.stack.append(val)
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty. Underflow!"
        return self.stack.pop()

stack = Stack()

stack.push(1)
stack.push(2)

print(stack.top())