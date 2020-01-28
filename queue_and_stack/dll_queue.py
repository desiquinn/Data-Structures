import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        #     - Because we need to be able to access both the head and the tail of the list
        self.storage = DoublyLinkedList()

    # Adds item to the back of the queue
    def enqueue(self, value):
        # increase size of queue by 1
        self.storage.add_to_tail(value)
        self.size += 1

    # Removes and returns item from the front of the queue
    def dequeue(self):
        if not self.storage.head:
            return None
        else:
            self.size -= 1
            return self.storage.remove_from_head()

    # Returns the length of the queue
    def len(self):
        return self.size

"""
Queue is FIFO like a line

"""