#!/usr/bin/python
import logging

LOGGER = logging.getLogger(__name__)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
LOGGER.addHandler(ch)

class Node(object):
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
    #def find(self):
    #def delete(self):

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_data(self):
        return self.data

    def add(self, data):
        '''
        add() - adds a new data item the tree
        '''
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.add(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.add(data)


def print_tree(node):
    if node is not None:
        print_tree(node.get_left())
        print node.get_data()
        print_tree(node.get_right())

#
# create the initial node object
node = Node(5)

node.add(4)
node.add(3)
node.add(2)
node.add(6)
node.add(7)
print_tree(node)
