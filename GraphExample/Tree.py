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
        pass
    def print_post(self):
        pass

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
    
    def print_in(self):
        self.root.print_in()

test = Tree(8)
values = [3, 9, 10, 3, 8, 15, 12, 13]

for i in values:
    test.add(i)

test.print_in()
