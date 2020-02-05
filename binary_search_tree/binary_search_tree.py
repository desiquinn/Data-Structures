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
            # print(f"value in root check {self.value}")
            # print(f"target in root check {target}")
            return True
        if target < self.value:
            # print(f"{target} is smaller than {self.value}")
            #look left
            if not self.left:
                # print("None")
                return False
            else:
                # print(self.value)
                # print(target)
                return self.left.contains(target)
        else:
            # print(f"{target} is larger than {self.value}")
            #look right
            if not self.right:
                # print("None")
                return False
            else:
                # print(self.value)
                # print(target)
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right:
            # print(self.right)
            # print(self.value)
            return self.value
        else:
            # print(self.right.value)
            # print(self.value)
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
        # print(f"printing self {self}")
        # print(f"printing value {self.value}")
        # traverse the entire left
        if self.left:
            # print(f"printing left {self.left.value}")
            self.left.in_order_print(self.left)
        # print the root
        print(node.value) #just had to move the order arround!
        # traverse the entire right
        if self.right:
            # print(f"printing right {self.right.value}")
            self.right.in_order_print(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # make a queue
        q = Queue()
        # add root to the queue
        q.enqueue(self)
        # While there is stuff in the queue
        while q.len() > 0:
            # remove root from the queue
            temp = q.dequeue()
            # if temp.left add to queue
            if temp.left:
                q.enqueue(temp.left)
            # if temp.right add to queue
            if temp.right:
                q.enqueue(temp.right)
            # print value
            print(temp.value)
        

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # make a stack
        s = Stack()
        # add root to stack
        s.push(self)
        # While there is stuff in the stack
        while s.len() > 0:
            # remove root from stack and save to a temp variable
            temp = s.pop()
            # print temp.value
            print(temp.value)
            # if temp.left add to stack
            if temp.left:
                s.push(temp.left)
            # if temp.right add to stack
            if temp.right:
                s.push(temp.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        #print the root
        print(node.value)
        # Traverse the left
        if self.left:
            self.left.pre_order_dft(self.left)
        # Traverse the right
        if self.right:
            self.right.pre_order_dft(self.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        #traverse the left
        if self.left:
            self.left.post_order_dft(self.left)
        #traverse the right
        if self.right:
            self.right.post_order_dft(self.right)
        #print the root
        print(node.value)