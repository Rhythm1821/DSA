# Queue using list
"""
class Queue:
    def __init__(self):
        self.items=[]
        # self.front=None
        # self.rear=None
        self.size=0
    
    def is_empty(self):
        return self.items==None
    
    def enqueue(self,data):
        self.items.append(data)
        self.size+=1
    
    def dequeue(self):
        if not self.is_empty():
            self.items.pop(0)
            self.size-=1
        else:
            raise IndexError("Queue is empty")
    
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return self.size
    
q1=Queue()
# print(q1.get_front())
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
print(q1.get_front())
print(q1.get_rear())
q1.dequeue()
print(q1.get_front())
print(q1.get_rear())
print(q1.size)
"""

# Queue inheriting linked list
"""
import sys
sys.path.append('..')
from linkedList.singlyLinkedList import SLL

class Queue(SLL):
    def __init__(self,start=None):
        super().__init__()
        self.start=start
        self.count=0
    def is_empty(self):
        return super().is_empty()
    
    def enqueue(self,data):
        if not self.is_empty():
            self.insert_at_start(data)
            self.count+=1
        else:
            raise IndexError("Queue is empty")

    def dequeue(self):
        if not self.is_empty():
            self.delete_last()
            self.count-=1
        else:
            raise IndexError("Queue is empty")
    def get_front(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("Queue is empty")

    # def get_rear(self):
    #     if not self.is_empty():
    #         for i in self.
    #     else:
    #         raise IndexError("Queue is empty")

    def size(self):
        return self.count
"""

# Queue uing linked list
"""
class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.item_count=0
    
    def is_empty(self):
        return self.item_count==0
    
    def enqueue(self,data):
        n=Node(data)
        if self.is_empty():
            self.front=n
        else:
            self.rear.next=n

        self.rear=n
        self.item_count+=1
    
    def dequeue(self):
        if self.is_empty():
            raise "Queue is empty"
        elif self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            self.front=self.front.next
        self.item_count-=1
    
    def get_front(self):
        if self.is_empty():
            raise "Queue is empty"
        return self.front.item
    
    def get_rear(self):
        if self.is_empty():
            raise "Queue is empty"
        return self.rear.item

    def size(self):
        return self.item_count
    
q1=Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
print(q1.get_front())
print(q1.get_rear())
q1.dequeue()
print(q1.get_front())
print(q1.get_rear())
"""

# Deque using list

"""
class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items)==0

    def insert_front(self,data):
        self.items.insert(0,data)

    def insert_rear(self,data):
        self.items.append(data)

    def delete_front(self):
        if self.is_empty():
            raise "Deque is empty"
        self.items.pop(0)

    def delete_rear(self):
        if self.is_empty():
            raise "Deque is empty"
        self.items.pop()

    def get_rear(self):
        if self.is_empty():
            raise "Deque is empty"
        return self.items[-1]

    def get_front(self):
        if self.is_empty():
            raise "Deque is empty"
        return self.items[0]
    
    def size(self):
        return len(self.items)
    
d1=Deque()
d1.insert_front(10)
d1.insert_front(20)
d1.insert_rear(30)
d1.insert_rear(40)
print(d1.get_front(), d1.get_rear())
"""


# Deque using doubly linked list
"""
class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next

class Deque:
    def __init__(self):
        self.front=None
        self.rear=None
        self.count=0
    
    def is_empty(self):
        return self.front==None
    
    def insert_front(self,data):
        n=Node(prev=None,item=data,next=self.front)
        if self.is_empty():
            self.rear=n
        else:
            self.front.prev=n
        self.front=n
        self.count+=1

    def insert_rear(self,data):
        n=Node(prev=self.rear,item=data,next=None)
        if self.is_empty():
            self.front=n
        else:
            self.rear.next=n
        self.rear=n
        self.count+=1

    def delete_front(self):
        if self.is_empty():
            raise "Deque is empty"
        elif self.front==self.rear:
            self.front=None 
            self.rear=None 
        else:
            self.front=self.front.next
            self.front.prev=None
        self.count-=1

    def delete_rear(self):
        if self.is_empty():
            raise "Deque is empty"
        elif self.front==self.rear:
            self.front=None 
            self.rear=None 
        else:
            self.rear=self.rear.prev
            self.rear.next=None
        self.count-=1

    def get_rear(self):
        if self.is_empty():
            raise "Deque is empty"
        return self.rear.item

    def get_front(self):
        if self.is_empty():
            raise "Deque is empty"
        return self.front.item
    
    def size(self):
        return self.count
    
d1=Deque()
d1.insert_front(10)
d1.insert_front(20)
d1.insert_rear(30)
d1.insert_rear(40)
print(d1.get_front(), d1.get_rear())
"""

# Priority Queue

"""
class PriorityQueue:
    def __init__(self):
        self.items=[]
    
    def is_empty(self):
        return len(self.items)==0
    
    def push(self,data,priority):
        index=0
        while index<len(self.items) and self.items[index][1]<priority:
            index+=1
        self.items.insert(index,(data,priority))

    def pop(self):
        if self.is_empty():
            raise "Queue is empty"
        return self.items.pop(0)[0]

    def size(self):
        return len(self.items)

p1=PriorityQueue()
p1.push("Amit",4)
p1.push("Arjun",7)
p1.push("Ashima",2)
p1.push("Agrah",5)
p1.push("Anant",8)
p1.push("Ambika",1)

while not p1.is_empty():
    print(p1.pop())
"""

# Priority Queue using Linked List
"""
class Node:
    def __init__(self,item=None,priority=None,next=None):
        self.item=item
        self.priority = priority
        self.next=next
    
class PriorityQueueLinkedList:
    def __init__(self):
        self.start=None
        self.count=0
    def is_empty(self):
        return self.start==None
    
    def push(self,data,priority):
        n=Node(data,priority)
        if not self.start or priority<self.start.priority:
            n.next=self.start
            self.start=n
        else:
            temp=self.start
            while temp.next and temp.next.priority<priority:
                temp=temp.next
            n.next=temp.next
            temp.next=n
        self.count+=1
    
    def pop(self):
        if self.is_empty():
            raise "Queue is empty"
        data=self.start.item
        self.start=self.start.next
        self.count-=1
        return data
    
    def size(self):
        return self.count
    
p1=PriorityQueueLinkedList()
p1.push("Amit",4)
p1.push("Arjun",7)
p1.push("Ashima",2)
p1.push("Agrah",5)
p1.push("Anant",8)
p1.push("Ambika",1)

while not p1.is_empty():
    print(p1.pop())
"""