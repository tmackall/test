#!/usr/bin/python

import os


def dir_list_recursive(dir_in, dir_list=[]):
    if os.path.isdir(dir_in):
        dir_list = os.listdir(dir_in)
        for dir in dir_list:
            dir_new = os.path.join(dir_in, dir)
            dir_list.append(dir_new)
            dir_list_recursive(dir_new, dir_list)


if __name__ == '__main__':
    paths = dir_list_recursive('/home/tmackall/bin')
    print 'paths: %s' % paths
    exit(0)
