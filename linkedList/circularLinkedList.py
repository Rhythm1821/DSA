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
        if self.is_empty():
            return None
        temp=self.last.next    
        while temp!=self.last:
            if temp==data:
                return temp
            temp=temp.next
        if temp.item==data:
            return temp
        return None
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n
            if temp==self.last:
                self.last=n
    def print_list(self):
        if not self.is_empty():
            temp=self.last.next
            while temp!=self.last:
                print(temp.next,end=" ")
                temp=temp.next
            print(temp.item)
    def delete_first(self):
        pass
    def delete_last(self):
        pass
    def delete_item(self):
        pass