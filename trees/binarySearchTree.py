class BinarySearchTree:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

    def insert(self,value):
        if self.value>value:
            if self.left is None:
                self.left= BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right=BinarySearchTree(value)
            else:
                self.right.insert(value)

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

tree = BinarySearchTree(6)
tree.insert(5)
tree.insert(2)
tree.insert(4)
tree.insert(1)
tree.insert(2)
tree.insert(4)
tree.insert(19)
tree.insert(29)
tree.insert(11)
tree.insert(4)
tree.insert(2)

# tree.inorder_traversal()
# tree.preorder_traversal()
tree.postorder_traversal()
