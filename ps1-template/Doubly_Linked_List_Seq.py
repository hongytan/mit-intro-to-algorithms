class Doubly_Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.prev = None
        self.next = None

    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)

class Doubly_Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __str__(self):
        return '-'.join([('(%s)' % x) for x in self])

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        ###########################
        # Part (a): Implement me! #
        ###########################
        node = Doubly_Linked_List_Node(x)
        if self.head: # Check if there is a head node
            node.next = self.head
            self.head.prev = node
        self.head = node
        if not self.tail: # No tail node
            self.tail = node

    def insert_last(self, x):
        ###########################
        # Part (a): Implement me! #
        ###########################
        node = Doubly_Linked_List_Node(x)
        if self.tail: # Check if there is a tail node
            node.prev = self.tail
            self.tail.next = node
        self.tail = node
        if not self.head: # Empty linked list
            self.head = node # Set head to node

    def delete_first(self):
        x = None
        ###########################
        # Part (a): Implement me! #
        ###########################
        if self.head:
            x = self.head.item
            self.head = self.head.next
        if self.head:
            self.head.prev = None
        return x

    def delete_last(self):
        x = None
        ###########################
        # Part (a): Implement me! #
        ###########################
        if self.tail:
            x = self.tail.item
            self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        return x

    def remove(self, x1, x2):
        L2 = Doubly_Linked_List_Seq()
        ###########################
        # Part (b): Implement me! # 
        ###########################
        x1.prev.next = x2.next
        x2.next.prev = x1.prev
        L2.head = x1
        L2.tail = x2
        x1.prev = None
        x2.next = None
        return L2

    def splice(self, x, L2):
        ###########################
        # Part (c): Implement me! # 
        ###########################
        x.next.prev = L2.tail
        L2.tail.next = x.next
        L2.head.prev = x
        x.next = L2.head
        L2.head = None
        L2.tail = None
