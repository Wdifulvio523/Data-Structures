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
        # get a ref to the current head [0]
        current_head = self.head
        
        # if it is none, make a new head from passed value
        if not current_head:
            self.head = ListNode(value)
        
        else:
              # if it is not the head, add it before and turn the previous head into the previous value
            current_head.insert_before(value)
            self.head = current_head.prev

    def remove_from_head(self):
        if not self.head:
            return None
        else:
            head = self.head
            self.head.delete()
            return head.value

    def add_to_tail(self, value):
        # create reference to current tail
        current_tail = self.tail
        
        # if there is no item in the list
        if not self.head:
            #create a new ListNode using the value, set it as head and tail
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
        
        # if there are items in the list
        else:
            # insert the value after the current tail, set self.tail = current_tail.next
            current_tail.insert_after(value)
            self.tail = current_tail.next

    def remove_from_tail(self):
        # if no tail return none
        if not self.tail:
            return None
        # if tail is also the head, make both == None
        if self.head == self.tail:
            # make a reference to the tail
            tail = self.tail
            # make both head and tail None
            self.head = None
            self.tail = None
            # return the removed value
            return tail.value

        # if tail is not also the head, remove it
        else:
            # make a reference to the tail
            tail = self.tail
            # run delete on self.tail
            self.tail.delete()
            # new self.tail is self.tail.prev
            self.tail = self.tail.prev
            # return removed value
            return tail.value

    def move_to_front(self, node):
        # check if already is in front
        if self.head is not node:
            if node.next and node.prev:  # if in a middle spot
               node.delete()
            current_head = self.head
            self.head = node
            node.next = current_head
            current_head.prev = node

    def move_to_end(self, node):
         # check if the nodelist is empty
        if self.tail is not node:
            if node.next and node.prev:  # if in a middle spot
                node.delete()
            current_tail = self.tail
            self.tail = node
            node.prev = current_tail
            current_tail.next = node

    # def delete(self, node):
    #     if node.next is None and node.prev is not None:
    #         node.prev.next = None
    #         self.tail = node.prev
    #         return node.value
    #     if node.prev is None and node.next is not None:
    #         node.next.prev = None
    #         self.head = node.next
    #         return node.value
    #     if node.prev is None and node.next is None:
    #         self.head = None
    #         self.tail = None
    #         return node.value
    #     else:
    #         node.delete()
    #         if node == self.head:
    #             self.head = node.next
    #         if node == self.tail:
    #             self.tail = node.prev
    #     return node.value


    def delete(self, node):
        #check if list is completely empty
        if not self.head and not self.tail:
           return None 

        # if our list has only a single nocde, then we delete it
        # both self.head and self.tail should be none
        if self.head == self.tail:
            self.head = None
            self.tail = None
        #check if given node is the head
        # set the self.head pointer to the next node
        # delete the node
        if self.head == node:
            self.head = node.next
            node.delete()

        #check if given node is the tail
        #set self.tail pointer to the prev node
        # delete the node
        if self.tail == node:
            self.tail = node.prev
            node.delete()

        #otherwise, node is in the middle of list
        #jut call node.delete()
        else:
            node.delete()

    def get_max(self):
        # store max value in a variable
        max = 0 
        current = self.head
        # if list is empty
          # return None
        if not self.head:
            return None
        # if list has only one item
        if self.head == self.tail:
            return self.head.value
          #return item
        while current:
          if current.value > max:
            max = current.value
          current = current.next
        # compare the current element to the max value
          #if current elem is > max value, current elem is new max value
        # return max value
        return max