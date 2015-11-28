#!/usr/bin/python

def dec(func):
    def something_extra(*args):
        print 'something extra'
        return func(*args)

    return something_extra


@dec
def add(x,y):
    return x + y


ssum = add(2,3)
print 'sum = %s' % ssum
