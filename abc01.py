#!/usr/bin/python

import abc


class PluginBase(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def load(self, input):
        """Retrieve data from the input source and return an object."""
        return

    @abc.abstractmethod
    def save(self, output, data):
        """Save the data object to the output."""
        return


class Test(PluginBase):
    pass


try:
    tc = Test()
except TypeError:
    print 'Cannot instantiate an abstract baseclass'


class Test(PluginBase):

    def __init__(self):
        print 'successful instantiation'

    def load(self, input):
        pass

    def save(self, output, data):
        pass

tc = Test()
