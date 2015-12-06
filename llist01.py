

class node(object):
    def __init__(self, data_in):
        self.data = data_in
        self.next = None

class llist(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, item):
        self.tail.next = item
        self.tail = item
        if self.head is None:
           self.head = item
        return

    def print(self):
        while self.next is not None:



