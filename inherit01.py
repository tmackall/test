#!/usr/bin/python
class A(object):
    def __init__(self):
        print 'A __init__'

    def f(self):
        return self.g()

    def g(self):
        return 'A'


class B(A):

    @staticmethod
    def b_sm():
        return 'B_SM'

    @classmethod
    def b_cm(cls):
        return 'B_CM'

    def g(self):
        return 'B'

    def z(self):
        return 'BZ'


class C(B):
    def f(self):
        # classmethods are inherited
        return 'C'

print 'a instant'
a = A()
print 'b instant'
b = B()
print dir(b)
print 'c instant'
# will use A __init__()
c = C()
print dir(c)
print 'output'
print a.f(), b.f()
print 'output1'
print a.g(), b.g()
print 'output2'
print c.g(), c.z(), c.f()
# both class and static methods are inherited
print '1', C.b_cm()
print '2', C.b_sm()
print 'done'
