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

