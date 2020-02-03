from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.capacity = limit
        self.current_size = 0
        self.dll = DoublyLinkedList()
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # if key value pair doesn't exist in self.storage
        if key not in self.storage:
            # return None
            # print(self.storage)
            return None
        # if key value pair does exist in self.storage
        else:
            # retrieves value that belongs to key
            # print(self.storage)
            node = self.storage[key]
            # print(node)
            # value = node.value
            # move key-value pair to the end of the order
            self.dll.remove_from_tail()
            self.dll.add_to_head(node)
            # returns the value associated with the key
            return node

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # if key already exists in the cache
        if key in self.storage:
            # overwrite the old value associated with the key with the new value
            self.storage[key] = value       
        # if the cache is at max capacity
        elif self.current_size == self.capacity:
            # remove oldest entry in cache (tail)
            deleted = self.dll.remove_from_tail()
            del self.storage[deleted[0]]
            # add given key value pair to cache to the head
            self.dll.add_to_head((key,value))
            self.storage[key] = value
        # else if cache not at max capacity and key doesn't exsist
        else:
            # add given key value pair to cache to the head
            self.dll.add_to_head((key,value))
            self.storage[key] = value
            # increment current size
            self.current_size += 1


