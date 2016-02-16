#!/usr/bin/python

import abc


class Animal:
    def __init__(self, name):    # Constructor of the class
        self.name = name

    @abc.abstractmethod
    def talk(self):              # Abstract method, defined by convention only
        pass


class Cat(Animal):
    def talk(self):
        return 'Meow!'


class Dog(Animal):
    def talk(self):
        return 'Woof! Woof!'

if __name__ == '__main__':

    animals = [Cat('Missy'),
               Cat('Mr. Mistoffelees'),
               Dog('Lassie')]

    for animal in animals:
        print animal.name + ': ' + animal.talk()
