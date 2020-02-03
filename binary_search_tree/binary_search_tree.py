import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            # print(f"{value} is smaller than {self.value}")
            if self.left == None:
                self.left = BinarySearchTree(value)
                # print(value)
                # print(self.value)
                # print(f"add to left {self.left}")
                # print(self.right)
            else:
                # print(value)
                # print(self.value)
                # print(self.left)
                # print(self.right)
                # print("Something to the left send it back in")
                self.left.insert(value)
        else:
            # print(f"{value} is larger than {self.value}")
            if self.right == None:
                self.right = BinarySearchTree(value)
                # print(value)
                # print(self.value)
                # print(self.left)
                # print(f"add to right {self.right}")
            else:
                # print(value)
                # print(self.value)
                # print(self.right)
                # print("Something to the right send it back in")
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            print(f"value in root check {self.value}")
            print(f"target in root check {target}")
            return True
        if target < self.value:
            print(f"{target} is smaller than {self.value}")
            #look left
            if not self.left:
                print("None")
                return False
            else:
                print(self.value)
                print(target)
                return self.left.contains(target)
        else:
            print(f"{target} is larger than {self.value}")
            #look right
            if not self.right:
                print("None")
                return False
            else:
                print(self.value)
                print(target)
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right:
            print(self.right)
            print(self.value)
            return self.value
        else:
            print(self.right.value)
            print(self.value)
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
