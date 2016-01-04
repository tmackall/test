#!/usr/bin/python
from random import randint
import sys

class treeb(object):

    def __init__(self, datain):
        print 'create data: %s' % datain
        self.data = datain
        self.nodel = None
        self.noder = None

    def addi(self, val):
        done = False

        node = self
        while not done:
            if val < node.data:
                if node.nodel is not None:
                    node = node.nodel
                else:
                    node.nodel = treeb(val)
                    done = True
            elif val > node.data:
                if node.noder is not None:
                    node = node.noder
                else:
                    node.noder = treeb(val)
                    done = True
            else:
                done = True

    def add(self, datain):
        if datain < self.data:
            if self.nodel is None:
                self.nodel = treeb(datain)
            else:
                self.nodel.add(datain)
        if datain > self.data:
            if self.noder is None:
                self.noder = treeb(datain)
            else:
                self.noder.add(datain)

    def check_exists(self, val):
        if val < self.data:
            if self.nodel is not None:
                return self.nodel.check_exists(val)
            else:
                return False
        elif val > self.data:
            if self.noder is not None:
                return self.noder.check_exists(val)
            else:
                return False
        elif val == self.data:
            print 'already exists: %s' % val
            return True

    def remove(self):
        return 0

    @classmethod
    def print_tree(cls, node):
        if node.nodel is not None:
            cls.print_tree(node.nodel)
        print node.data
        if node.noder is not None:
            cls.print_tree(node.noder)

#    @classmethod
#    def get_max_depth(cls, node):
#        stackt = []
#        stackt.append(node)
#        list_depth = []
#        done = False
#        # iterate until we have exhausted all nodes
#        while (stackt):
#
#            node = stackt[0]
#            # iterate left
#            if node.nodel is not None:
#                stackt.insert(0, nodel)
#            elif node.noder is not None:
#                stackt.insert(0, nodel)
#            else:
#
#
#        # if node left is not node, place on stack and continue
#        # if node left is None, capture the depth in a list
#        # iterate right
#        # if node right is not node, place on stack and continue
#        # if node right is None, capture the depth in a list

if __name__ == "__main__":

    #
    # command line size - check it
    if len(sys.argv) > 1:
        size = int(sys.argv[1])
    else:
        size = 10

    #
    # set binary tree
    mid = int(size/2)
    t = treeb(mid)

    done = False
    cnt = 0
    while not done:
        val = randint(1, size)
        print val
        if t.check_exists(val) is False:
            t.addi(val)
            cnt += 1
        if cnt >= int(size / 2):
            done = True

    treeb.print_tree(t)
