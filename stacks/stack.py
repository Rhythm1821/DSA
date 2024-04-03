
# class Stack:
#     def __init__(self):
#         self.items = []
    
#     def is_empty(self):
#         return len(self.items)==0
    
#     def push(self,data):
#         self.items.append(data)
    
#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop()
#         else:
#             raise IndexError("Stack is empty")
    
#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1]
#         else:
#             raise IndexError("Stack is empty")
    
#     def size(self):
#         return len(self.items)
    
# stack = Stack()
# stack.push(10)
# stack.push(20)
# stack.push(30)
# print("Top element is",stack.peek())
# print("Removed element",stack.pop())
# print("Top element is",stack.peek())
# print()


# # Stack inheriting list class

# class Stack(list):
#     def is_empty(self):
#         return len(self)==0
    
#     def push(self,data):
#         self.append(data)
    
#     def pop(self):
#         if not self.is_empty():
#             return super().pop()
#         else:
#             raise IndexError('Stack is empty')
    
#     def peek(self):
#         if not self.is_empty():
#             return self[-1]
#         else:
#             raise IndexError("Stack is empty")
        
#     def size(self):
#         return len(self)
    
#     def insert(self,index,data):
#         raise AttributeError("No attribute insert in stack")
    

# stack = Stack()
# stack.push(10)
# stack.push(20)
# stack.push(30)
# print("Top element is",stack.peek())
# print("Removed element",stack.pop())
# print("Top element is",stack.peek())
# print()


# Stacks using linked list
import sys
sys.path.append('..')
from linkedList.singlyLinkedList import SLL

class Stack(SLL):
    def __init__(self, start=None):
        super().__init__()
        self.item_count = 0 
    def is_empty(self):
        return super().is_empty()
    
    def push(self,data):
        self.insert_at_start(data)
        self.item_count+=1

    def pop(self):
        if not self.is_empty():
            self.delete_first()
            self.item_count-=1
    
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("Stack is empty")
        
    def size(self):
        return self.item_count
    
stack = Stack()
stack.push(10)    
stack.push(20)    
stack.push(30)
print("Top element on the stack is, ",stack.peek())
stack.pop()
print("Top element on the stack is, ",stack.peek())