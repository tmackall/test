

class node(object):
    def __init__(self, data_in):
        self.data = data_in
        self.next = None
        self.prev = None

class llist(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.node = None

    def insert(self, node_in):
        self.tail.next = node_in
        self.tail = node_in
        if self.head is None:
           self.head = node_in
        return



