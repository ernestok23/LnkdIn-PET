#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
#
#
# [] for lists              MUTABLE, sequential and iterable
# () for tuples             IMMUTABLE
# range() for ranges        IMMUTABLE
# {} for dictionaries       MUTABLE key:value, ...
# {} for sets               value,...
#
"""
# Script: test__name__.py
# Use:      to test the return of the __name__ spcial variable
#           use this script by itslef and also being called by 
#           the call_test__name__.py script

# All functions return a value
# If you don't specify a return value, it will return 'None'
#
# Python has no distinction between a function and a procedure
#
# When you assign a MUTABLE, yuo assign a REFERENCE to the MUTABLE
#-----------------------------------------------------------
"""

def main():
    kitten()
    
    # the following print() prints __main__
    print('From test__name__.main(), This is __name__ {}'.format(__name__) )



def kitten():
    print('From test__name__.kitten() : Meow.')
    print('From test__name__.kitten(), this is the value of __name__ : {}'.format(__name__))


"""
# This special variable __name__ gets its value depending on how we execute the 
# containing script. This lets you decide you whether you want to run the script. 
# Or that you want to import the functions defined in the script.
#
# When you run your script, the __name__ variable equals __main__. 
# When you import the containing script, it will contain the name of the script.
#
# See you example of call_test__name__.py and test__name__.py
#-------------------------------------------------------------
# 1.- When you run test__name__.py, the value of __name__ is __main__
#
# 2.- When you run call_test__name__.py, that imports test__name__.py, 
#     you get the following:
#       from call_test__name__.py, __name__ is __main__
#       from test__name__.py, __name__ is test__name__
# 
"""
# So here, __name__ will return __main__, so it will run the main() method
if __name__ == '__main__': main()
