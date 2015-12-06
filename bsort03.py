#!/usr/bin/python
import random

class node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add(self, data):
        '''
        add() - used to place a new value on the tree
        '''
        # less than top node, traverse left
        if data < self.data:
            if self.left is not None:
                self.left.add(data)
            # nothing left, add it
            else:
                self.left = node(data)
        # more than right node, traverse right
        if data > self.data:
            if self.right is not None:
                self.right.add(data)
            else:
                # nothing right, add it
                self.right = node(data)

    @classmethod
    def nprint(cls, node):
        '''
        nprint  - prints the tree in order
            - traverses left and prints the node value when it reaches the end
            - prints the top node
            - traverses right and prints the node value when it reaches the end
        '''
        if node.right is not None:
            cls.nprint(node.right)
        print node.data
        if node.left is not None:
            cls.nprint(node.left)

    @classmethod
    def find_depth(cls, node, ldepth=1, rdepth=1):
        if node.left is not None:
            ldepth += 1
            return cls.find_depth(node.left, ldepth, rdepth)
        elif node.right is not None:
            rdepth += 1
            return cls.find_depth(node.right, ldepth, rdepth)
        else:
            if rdepth > ldepth:
                return rdepth
            else:
                return ldepth

    @staticmethod
    def trav_iter(node):

        # top of the node - start left and then right
        for outer in (node.left, node.right):
            current = outer.left
            stack = []
            while current is not None and current.left is not None and current.right is not None:
                print "made it2"
                stack.append(current)
                if current.left is not None:
                    current = current.left
                else:
                    current = current.right
            print "made it"
            print stack









tree_size = 50
n =  node(tree_size/2)

for i in range(tree_size):
    n.add(i+1)

node.nprint(n)
#print 'depth: {0}'.format(node.find_depth(n))
node.trav_iter(n)


