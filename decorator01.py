#!/usr/bin/python
import sys

def dec(func):
    def something_extra(*args,**kwargs):
        print '{}'.format(args)
        func_ret = func(*args, **kwargs)
        return func_ret + 1

    return something_extra

@dec
def add(x,y):
    return x + y

if __name__ == '__main__':

    if len(sys.argv) > 1:
        a1 = int(sys.argv[1])
        a2 = int(sys.argv[2])
    else:
        a1 = 3
        a2 = 2

    ssum = add(a1,a2)
    print 'sum = %s' % ssum
