import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    # adds item to the back of the queue
    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1
        
    # removes item from the back of the queue
    def pop(self):
        if not self.storage.head:
            return None
        else:
            self.size -= 1
            return self.storage.remove_from_tail()

    # returns the length of the queue
    def len(self):
        return self.size

"""
Stack is FILO

"""