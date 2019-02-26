"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node

    def add_to_head(self, value):
        # create a variable that references self.head
        prev_head = self.head
        # if that variabl = None
        if not prev_head:
            # create a LisNode from that value ans set self.head to that
            self.head = ListNode(value)
        # Else
        else:
            prev_head.insert_before(value)
            self.head = prev_head.prev
            # run insert_before() on variable, to insert value at the head of the list
            # reassign self. head to be variable.prev

    def remove_from_head(self):
        # if no elements in the list, or self.head == None:
        if not self.head:
            return None
        # # if single element? Or self.head == self.tail
        # WHY DONT WE NEED TO CHECK THIS?
        # if self.head == self.tail:
        #   self.head.delete()
        #   return None
        # if multiple linked elements?
        else:
            # create ref to head
            head = self.head
            # run delete method on self.head
            self.head.delete()
            # return head.value
            return head.value

    def add_to_tail(self, value):
        # create variable that references new listNode created from value
        new_node = ListNode(value)
        # check if list is empty
        if not self.head:
            # if so, makes new_node head and tail
            self.head = new_node
            self.tail = new_node
        # if not empty
        else:
            # use insert After method to insert new node after the tail
            self.tail.insert_after(new_node)
            # make new self.tail = new_node
            self.tail = new_node

    def remove_from_tail(self):
       # if no elements in the list:
        if not self.tail:
            # return none
            return None
        # if there is one element in the list aka there is no self.tail.prev:
        if not self.tail.prev:
            # make a reference to tail
            tail = self.tail
            # set head and tail == None
            self.head = None
            self.tail = None
            # return variable.value
            return tail.value
        # if more than 1 element in the lise
        else:
            # create ref to tail
            tail = self.tail
            # run delete method on self.tail to remove it
            self.tail.delete()
            # self.tail should now equal tail.prev
            self.tail = tail.prev
            # return the value of self.tail
            return self.tail.value

    def move_to_front(self, node):
        # check if already is in front
        if self.head is not node:
            if node.next and node.prev:  # if in a middle spot
                node.prev.next = node.next
                node.next.prev = node.prev
            current_head = self.head
            self.head = node
            node.next = current_head
            current_head.prev = node

    def move_to_end(self, node):
        pass

    def delete(self, node):
        pass

    def get_max(self):
        pass
