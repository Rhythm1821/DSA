class BinarySearchTree:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None
        self.data=None

    def insert(self,value,data=None):
        if self.value>value:
            if self.left is None:
                self.left= BinarySearchTree(value)
                self.left.data = data
            else:
                self.left.insert(value,data)
        else:
            if self.right is None:
                self.right=BinarySearchTree(value)
                self.right.data = data
            else:
                self.right.insert(value,data)

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.value)
        if self.right:
            self.right.inorder_traversal()

    def preorder_traversal(self):
        print(self.value)
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()

    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.value)
    
    def find(self,value):
        if value < self.value:
            if self.left is None:
                return None
            else:
                return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return None
            else:
                return self.right.find(value)
        else:
            return self

tree = BinarySearchTree(6)
tree.insert(5)
tree.insert(2)
tree.insert(4)
tree.insert(1,{"data":45})
tree.insert(2)
tree.insert(4)
tree.insert(19)
tree.insert(29)
tree.insert(11)
tree.insert(4)
tree.insert(2)

# tree.inorder_traversal()
# tree.preorder_traversal()
# tree.postorder_traversal()

print(tree.find(1).data["data"])