class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#               a
#             /   \
#           b       c
#         /  \        \
#        d    e        f


# Depth first traversal
# use a stack
# check if stack is empty
# check if the node has been visited

def depthFirstValues(root):
    stack = [root]
    while len(stack) > 0:
        current = stack.pop()
        print(current.val)
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

depthFirstValues(a)
        
