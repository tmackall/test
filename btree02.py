#!/usr/bin/python

import random


class node(object):
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def add(self, val):
        # if the value is greater than the node go right
        if val < self.val:
            if self.left is not None:
                self.left.add(val)
            else:
                self.left = node(val)
        # if the value is less than the current node value, go left
        if val > self.val:
            if self.right is not None:
                self.right.add(val)
            else:
                self.right = node(val)

    def find(self, val):
        if val == self.val:
            return True
        if val < self.val:
            if self.left is not None:
                return self.left.find(val)
        elif val > self.val:
            if self.right is not None:
                return self.right.find(val)

    def __iter__(self):
        return self.val

    def __next__(self):
        return self.right.val

    @classmethod
    def nprint(cls, node):
        if node.left is not None:
            cls.nprint(node.left)
        print node.val
        if node.right is not None:
            cls.nprint(node.right)

    @classmethod
    def find_depth(cls, node, depthl=1, depthr=1):
        if node.left is not None:
            depthl += 1
            return cls.find_depth(node.left, depthl, depthr)
        if node.right is not None:
            depthr += 1
            return cls.find_depth(node.right, depthl, depthr)
        if depthl > depthr:
            return depthl
        else:
            return depthr


if __name__ == '__main__':
    n = node(50)
    for i in range(100):
        n.add(random.randint(1, 100))

    node.nprint(n)
    for i in node:
        print i
    print node.find_depth(n)
    # print n.find(25)
