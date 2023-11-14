class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.item=item
        self.prev=prev
        self.next=next

class DLL:
    def __init__(self,start):
        self.start=start
    def is_empty(self):
        return self.start==None
    def insert_at_start(self,data):
        n=Node(None,data,self.start)
        if not self.is_empty():
            self.start.prev=n
        self.start=n
    def insert_at_last(self,data):
        temp=self.start
        if self.start is not None:
            while temp.next is not None:
                temp=temp.next
        n=Node(temp,data,None)
        if temp==None:
            self.start=n
        else:
            temp.next=n
        
    def search(self,data):
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                if temp==data:
                    return temp
                temp=temp.next
            return None