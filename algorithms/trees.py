from queue import Queue

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value):
        if self.left_child == None:
            self.left_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left_child = self.left_child
            self.left_child = new_node
    
    def insert_right(self, value):
        if self.right_child == None:
            self.right_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value) #create a new node
            new_node.right_child = self.right_child #assign none
            self.right_child = new_node #assign the 
    
    def pre_order_dfs(self):
        print(self.value)
        if self.left_child:
            self.left_child.pre_order_dfs()
        if self.right_child:
            self.right_child.pre_order_dfs()

    def in_order_dfs(self):
        if self.left_child:
            self.left_child.in_order_dfs()
        print(self.value)
        if self.right_child:
            self.right_child.in_order_dfs()

    def post_order(self):
        if self.left_child:
            self.left_child.post_order()
        if self.right_child:
            self.right_child.post_order()
        print(self.value)

    def bfs(self):
        queue = Queue()
        queue.put(self)

        while not queue.empty():
            current_node = queue.get()
            print(current_node.value)
            if current_node.left_child:
                queue.put(current_node.left_child)
            if current_node.right_child:
                queue.put(current_node.right_child)




one_node = BinaryTree("1")
one_node.insert_left("2")

one_copy_node = BinaryTree("1")
one_copy_node.insert_right("2")


def isSameTree(p, q):
    if p.value != q.value:
        return False
    elif not(p.left_child) or not(q.left_child):
        return False
    if p.left_child.value != q.left_child.value:
        return False
    else:
        isSameTree(p.left_child, q.left_child)

    if p.right_child.value != q.right_child.value:
        return False
    else:
        isSameTree(p.right_child, q.right_child)
    return True

print(isSameTree(one_node, one_copy_node))