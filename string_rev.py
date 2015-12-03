#!/usr/bin/python

def string_rev(in_string):
    '''
    input a string - the output will be the reverse of the input string in a new object
    '''
    ret_string = ''
    idx = 0
    for i in range(len(in_string),0):
        ret_string += in_string[i]
        idx += 1

    return ret_string


a = "123456"
print a[::-1]
print a[0:3]
print a[::-1]
print a[:-2]


