from collections import deque

"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

        # if value >= parent.value and right branch is empty create right branch
        if self.right is None and value >= self.value:
            self.right = BSTNode(value)
            return value
        # if value < parent.value and left branch is empty create left branch
        if self.left is None and value < self.value:
            self.left = BSTNode(value)
            return value
        # if value >= parent.value and right branch is occupied recurse
        if self.right is not None and value >= self.value:
            self.right.insert(value)
        # if value < parent.value and left branch is occupied recurse
        if self.left is not None and value < self.value:
            self.left.insert(value)
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value: return True
        # if target > self.value and self has a right child recurse in child
        if target > self.value and self.right: 
            return self.right.contains(target)
        # if target < self.value and self has a left child recurse in child
        if target < self.value and self.left: 
            return self.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # if no self.right return value
        if not self.right: return self.value
        # else recurse in right child
        return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # mutate self.value
        fn(self.value)
        # recurse through all children
        if self.left: self.left.for_each(fn)
        if self.right: self.right.for_each(fn)
        

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        # if left child recurse in left child
        if self.left: self.left.in_order_print()
        # print value
        print(self.value)    
        # if right child recurse in right child
        if self.right:self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        #create que and append self to the end
        que = deque()
        que.append(self)

        # while que is not empty itterate
        while len(que) > 0:
            # ref the last node appended and remove it
            current = que.popleft()
            # if ref has left child append it to the que
            if current.left:que.append(current.left)
            # if ref has right child append it to the que
            if current.right:que.append(current.right)
            # print ref.value
            print(current.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        # create stack and append self
        stack = []
        stack.append(self)

        # while stack is not empty itterate
        while len(stack) > 0:
            # ref the last node appended and remove it
            current = stack.pop()
            # if ref has left child append it to the que
            if current.right: stack.append(current.right)
            # if ref has right child append it to the que
            if current.left: stack.append(current.left)
            # print ref.value
            print(current.value)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""

bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)



print('Print "in order"')
bst.in_order_print()

print()
print('- Print "bft" -')
print()
bst.bft_print()

print()
print('- Print "dft" -')
print()
bst.dft_print()
"""
bst.dft_print()
"""
"""

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_dft()
print("post order")
bst.post_order_dft()

"""