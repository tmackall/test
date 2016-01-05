#!/usr/bin/python

def foo(a, b, c):
    print '%s, %s, %s' % (a, b, c)


def foo2(x=4, y=5, z=6):
    print '%s, %s, %s' % (x, y, z)

def foo3(*args):
    print '{}'.format(*args)

a = {'x': 1, 'y': 2, 'z': 3}
a1 = {'a': 1, 'y': 2, 'z': 3}
b = [3, 2, 1]



#
# pass in keys only - should be x, y, z passed to a,b,c
foo(*a)
foo(*a1)
foo3(*a)
foo3(a)
print 'foo3(*b)'
foo3(*b)
print 'foo3(b)'
foo3(b)
#
# no params - will work because all are kwargs
foo2()
# values sent
print 'foo2(**a)'
foo2(**a)
# keys sent
print 'foo2(*a)'
foo2(*a)
# list sent to first kwarg (x)
print 'foo2(b)'
foo2(b)
#
print 'foo2(*b)'
foo2(*b)
