import sys
sys.path.append('..')
from singlyLinkedList import *

def reverseLinkListRecursive(start):
    if start is None or start.next is None:
        return start
    newHead = reverseLinkListRecursive(start.next)
    start.next.next = start
    start.next = None
    return newHead

def reverseLinkListIterative(start):
    prev = None
    while start:
        temp = start.next
        start.next = prev
        prev = start
        start = temp
    return prev

# Create the linked list
mylist = SLL()
mylist.insert_at_last(1)
mylist.insert_at_last(2)
mylist.insert_at_last(3)
mylist.insert_at_last(4)
mylist.insert_at_last(5)

# Print original linked list
print("Original linked list:")
mylist.print_list()

# Reverse the linked list recursively
new_start_recursive = reverseLinkListRecursive(mylist.start)

# Print the reversed linked list
print("\nReversed linked list (recursive):")
mylist.start = new_start_recursive
mylist.print_list()

# Create the linked list again
mylist = SLL()
mylist.insert_at_last(1)
mylist.insert_at_last(2)
mylist.insert_at_last(3)
mylist.insert_at_last(4)
mylist.insert_at_last(5)

# Reverse the linked list iteratively
new_start_iterative = reverseLinkListIterative(mylist.start)

# Print the reversed linked list
print("\nReversed linked list (iterative):")
mylist.start = new_start_iterative
mylist.print_list()
