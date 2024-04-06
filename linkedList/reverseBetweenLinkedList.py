import sys
sys.path.append('..')
from singlyLinkedList import *

def reverseFirst(start, n):
    """
    Reverse the first n nodes starting from the given start node.
    
    Parameters:
    start (Node): The starting node from which to begin the reversal.
    n (int): The number of nodes to reverse.
    
    Returns:
    Node: The new head of the reversed list.
    """
    prev = None
    curr = start
    while n > 0:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        n -= 1
    start.next = curr
    return prev

def reverseBetween(start, m, n):
    """
    A function that reverses a portion of a linked list between positions m and n.
    
    Parameters:
    start (ListNode): The starting node of the linked list.
    m (int): The starting position to reverse from.
    n (int): The ending position to reverse until.
    
    Returns:
    ListNode: The head of the linked list with the specified portion reversed.
    """    
    if m==1:
        return reverseFirst(start, n)
    else:
        start.next = reverseBetween(start.next, m-1, n-1)
    return start


# Create the linked list again
mylist = SLL()
mylist.insert_at_last(1)
mylist.insert_at_last(2)
mylist.insert_at_last(3)
mylist.insert_at_last(4)
mylist.insert_at_last(5)

# Print original linked list
print("Original linked list:")
mylist.print_list()

# Reverse the linked list between m and n
new_start = reverseBetween(mylist.start, 2, 4)

# Print the reversed linked list
print("\nReversed linked list:")
mylist.start = new_start
mylist.print_list()