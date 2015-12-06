#!/usr/bin/python

import random

class node(object):
    def __init__(self, val):
        self.prev = None
        self.val = val
        self.next = None


class lList(object):
    # constructor - init vars head, tail
    def __init__(self):
        self.head = None
        self.tail = None

    # add() - take a value and add a node. Update prev point to new node and new next pointer to null
    def add(self, val):
        # create a node
        lnode = node(val)

        # if head is None, add node and point head and tail the new node
        if self.head is None:
            self.head = lnode
            self.tail = lnode
        # create node and add it to the tail
        else:
            self.tail.next = lnode
            lnode.prev = self.tail
            self.tail = lnode

    # find() - traverse the list looking for a matching val - return 0 success and non-zero fail
    # size() - return the num of nodes in the list
    # lprint() - print the list
    def llprint(self):
        pnode = self.head
        while pnode is not None:
            print pnode.val
            pnode = pnode.next



myllist = lList()
for i in range(10):
    myllist.add(i)
myllist.llprint()
