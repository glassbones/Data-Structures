"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # wrap the value in a Node
        newNode = ListNode(value)
        # check if the Linked List is empty 
        if not self.head:
            # set head and tail to the new node 
            self.head = newNode
            self.tail = newNode
            self.length += 1
        # otherwise, the list has at least one node 
        else:
            # update the heads `prev_node` to the new node 
            self.head.prev = newNode
            # update the new node's `next_node` to the old head 
            newNode.next = self.head
            # update `self.head` to point the new node we just added 
            self.head = newNode
            self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # check if the linked list is empty
        if not self.head:
            return None
        
        # check if the linked list has only one node 
        if self.head == self.tail:
            # store the node we're going to remove's value 
            current = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return current.value
                
        # otherwise, the linked list has more than one Node 
        else:
            current = self.head
            self.head = self.head.next
            self.head.prev = None
            current.next = None
            self.length -= 1
            return current.value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # wrap the value in a Node
        newNode = ListNode(value)
        # check if the Linked List is empty 
        if self.head is None and self.tail is None:
            # set head and tail to the new node 
            self.head = newNode
            self.tail = newNode
            self.length += 1
        # otherwise, the list has at least one node 
        else:
            # update the last node's `next_node` to the new node 
            self.tail.next = newNode
            # update the new node's `prev_node` to the old tail 
            newNode.prev = self.tail
            # update `self.tail` to point the new node we just added 
            self.tail = newNode
            self.length += 1
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if not self.head:
            return None
        
        # check if the linked list has only one node 
        if self.head == self.tail:
            # store the node we're going to remove's value
            current = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return current.value
                
        # otherwise, the linked list has more than one Node 
        else:
            current = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            current.prev = None
            self.length -= 1
            return current.value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # check if the linked list empty
        if not self.head:
            return None
        # check if there is only one linked list node
        if self.head == self.tail:
            return node
        # check to see if node is already at the front
        if node == self.head:
            return self.head

        # remove node from list
        self.delete(node)
        # add node to head
        self.add_to_head(node.value)
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        # check if the linked list empty
        if not self.head:
            return None
        # check if there is only one linked list node
        if self.head == self.tail:
            return node
        # check to see if node is already at the end
        if node == self.tail:
            return self.tail
            
        # remove node from list
        self.delete(node)
        # add node to head
        self.add_to_tail(node.value)
    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # check if the linked list is empty 
        if not self.head:
            return None

        # check if the linked list has only one node 
        if self.head == self.tail:
            current = self.head.value
            # store the node we're going to remove's value 
            if self.head == node:
                self.head = None
                self.tail = None
                self.length = 0
                return current

            return current

        # check if node is head
        if node.prev == None:
            self.remove_from_head()
            return self.head.value

        # check if node is tail
        if node.next == None:
            self.remove_from_tail()
            return self.tail.value
        
        else:
            # connect the nodes connected to the node
            node.next.prev = node.prev
            node.prev.next = node.next
            # unconnect the node
            node.next = None
            node.prev = None
            self.length -= 1
            return node

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        # check if the linked list is empty 
        if not self.head:
            return None
        # ref value of head
        max_value = self.head.value
        # ref current node
        current = self.head
        # itterate through all items on list until current = None
        while current:
            # if new current value > old current value update current value
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value