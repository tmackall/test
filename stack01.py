#!/usr/bin/python
'''Implement 2 stacks in a single array'''

import random


class StacksSingleList(object):

    def __init__(self, stack1, stack2, size=100):
        self.stack = size * [hex(255)]
        self.head = {}
        self.s1 = stack1
        self.s2 = stack2
        self.head[stack1] = 0
        self.head[stack2] = size - 1
        print self.stack, self.head

    def add(self, val, stack):
        index = self.head[stack]

        if stack == self.s1:
            self.head[stack] += 1
        else:
            self.head[stack] -= 1

        self.stack[index] = val

    def prints(self):
        print self.stack

s1 = 'stack_low'
s2 = 'stack_high'
vals = random.sample(xrange(1000), 10)
s = StacksSingleList(s1, s2, 10)

print 'vals start: %s' % vals
for vall, valu in zip(vals[::2], vals[1::2]):
    s.add(vall, s2)
    s.add(valu, s1)

s.prints()
