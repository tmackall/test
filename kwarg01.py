
def foo(a, b, c):
    print '%s, %s, %s' % (a, b, c)


def foo2(x=4, y=5, z=6):
    print '%s, %s, %s' % (x, y, z)

a = {'x': 1, 'y': 2, 'z': 3}
b = [3, 2, 1]

foo(*a)
foo2()
# values sent
foo2(**a)
# keys sent
foo2(*a)
# list sent to first kwarg (x)
foo2(b)
#
foo2(*b)
