class Node:
    def __init__(self, value, parent, left, right):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
    def print_in(self):
        if self.left != None:
            self.left.print_in()
        print(self.value)
        if self.right != None:
            self.right.print_in()
    def print_pre(self):
        print(self.value)
        if self.left != None:
            self.left.print_pre()
        if self.right != None:
            self.right.print_pre()
    def print_post(self):
        if self.left != None:
            self.left.print_post()
        if self.right != None:
            self.right.print_post()
        print(self.value)
    def find_lowest_value_node(self):
        current = self.right
        while current.left != None:
            current = current.left 
        return current

    def remove(self):
        if self.right == None and self.left == None:
            if self.parent.value >= self.value:
                self.parent.left = None
                self.parent = None
            else:
                self.parent.right = None
                self.parent = None
            return
        if self.right == None or self.left == None:
            child = self.right
            if self.right == None:
                child = self.left
            self.right = None
            self.left = None 
            child.parent = self.parent               
            if self.parent.value >= self.value: 
                self.parent.left = child
            else:
                self.parent.right = child
            self.parent = None
            return
        target_node = self.find_lowest_value_node()
        if target_node.right != None:
            if target_node.parent.value >= target_node.value:
                target_node.parent.left = target_node.right
            else:
                target_node.parent.right = target_node.right
            target_node.right.parent = target_node.parent
            target_node.right = None
            target_node.parent = None
        else:
            if target_node.parent.value >= target_node.value:
                target_node.parent.left = None
            else:
                target_node.parent.right = None
            target_node.parent = None
        self.value = target_node.value 
             

class Tree:
    # Root is a node
    def __init__(self, value):
        self.root = Node(value, None, None, None)

    def add(self, value):
        toAdd = Node(value, None, None, None)
        parent = None
        current = self.root
        isLeft = True

        while current != None:
            parent = current
            if toAdd.value <= current.value:
                isLeft = True
                current = current.left
            else:
                isLeft = False
                current = current.right

        toAdd.parent = parent
        if isLeft:
            parent.left = toAdd
        else:
            parent.right = toAdd
    
    def remove(self, value):
        current = self.root
        while current.value != value and current != None:
            if value <= current.value:
                current = current.left
            else:
                current = current.right

        if current != None:
            current.remove()
        else:
            print("Value is not in the tree")
    



    def print_in(self):
        self.root.print_in()
    def print_pre(self):
        self.root.print_pre()
    def print_post(self):
        self.root.print_post()

test = Tree(5)
values = [4,10,2,6,11]

for i in values:
    test.add(i)
test.print_in()
test.remove(4)
test.print_in()


