


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
        if self.right: self.right.for_each(fn)
        if self.left: self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

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
"""
bst = BinarySearchTree(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_dft()
print("post order")
bst.post_order_dft()

"""

