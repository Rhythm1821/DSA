class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class CLL:
    def __init__(self,last):
        self.last=last
    def is_empty(self):
        return self.last==None
    def insert_at_start(self,data):
        n=Node(data)
        if not self.is_empty():
            n.next=self.last.next
            self.last.next=n
        else:
            n.next=n
            self.last=n
    def insert_at_last(self,data):
            n=Node(data)
            if self.is_empty():
                n.next=n
                self.last=n
            else:
                n.next=self.last.next
                self.last.next=n
                self.last=n
    def search(self,data):
        pass