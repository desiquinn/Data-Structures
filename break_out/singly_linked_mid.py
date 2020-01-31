"""Spec: How do you find and return the middle node of a singly linked list 
in one pass? You do not have access to the length of the list. If the 
list is even, you should return the first of the two “middle” nodes. 
You may not store the nodes in another data structure.

Source:

"""

class List_node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Singly_list:
    def __init__(self, node=None):
        self.head = node

    def find_mid(self):
        # assign 1st pointer (middle) to head and iterate by 1
        # assign 2nd pointer (current) to head and iterate by 2
        # loop through the list while 2nd pointer.next is not none
            # increment 1st pointer by 1 and reassign middle
            # increment 2nd pointer by 2 and reassign current
        # return 1st pointer

"""
Reverse through a singly linked list
Source: https://www.geeksforgeeks.org/reverse-a-linked-list/
How the list starts:
curr = 1
curr.prev = null
curr.next = 2

Pseudo Code:
prev = null

while curr is not None
next = curr.next
curr.next = prev
prev = curr
curr = next
"""