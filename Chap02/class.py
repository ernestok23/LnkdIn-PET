#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
#
# [] for lists              MUTABLE
# () for tuples             IMMUTABLE
# range() for ranges        IMMUTABLE
# {} for dictionaries       MUTABLE
#

class Duck:
    sound = 'Quack, Quack, Quaaaaaaaack! '
    walking = 'Walks like a another duck'
    # self is NOT a keyword, but it is called like that by convention
    # it is a reference to an object instantiated by the class
    def quack(self):
        print('Quaaack!')
        print(self.sound)

    def walk(self):
        print('Walks like a duck.')
        print(self.walking)


class Tree:
    height=5
    def Height(self):
        print('height is {}'.format(self.height))



def main():
    donald = Duck()     # this makes donald as object of the Duck class
    donald.quack()
    donald.walk()
    
    # print the object attributed from main
    print('From main ...{}...{}'.format(donald.sound, donald.walking))
    
    Elm=Tree()
    Elm.Height()

if __name__ == '__main__': main()
