#!/usr/bin/python

def deco(fun):


    def inner(*args):
        print 'this is a wrapper'

        return fun(*args)

    return inner



@deco
def add_me(*args):

    tot = 0
    for val in args:
        tot += val

    return tot



if __name__ == '__main__':
    nums = []

    for i in range(100):
        nums.append(i)

    print add_me(*nums)
