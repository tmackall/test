#!/usr/bin/python
from random import randint
import sys

class treeb(object):
    data = None
    nodel = None
    noder = None

    def __init__(self, datain):
        print 'create data: %s' % datain
        self.data = datain
        self.nodel = None
        self.noder = None

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
            t.add(val)
            cnt += 1
        if cnt >= int(size / 2):
            done = True

    treeb.print_tree(t)
