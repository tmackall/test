#!/usr/bin/python


class A(object):
    def f(self):
        return 'class A'


class B(object):
    def f(self):
        return 'class B'


class C(B, A):
    pass

c = C()
#
# will print from whichever is inherited first (class B)
print c.f()


class A():
    def f(self):
        return 'class A'


class B():
    def f(self):
        return 'class B'


class C(A, B):
    pass

c = C()
#
# will print from whichever is inherited first (class A) - inheriting from object
# doesn't seem to make a difference (at least here)
print c.f()
