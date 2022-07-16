#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

"""
A decorator is a function that returns another function, usually applied as a function 
transformation using the @wrapper syntax
"""

import time

# this function will wrap the passed function f between two timestamps

# [] for lists              MUTABLE
# () for tuples             IMMUTABLE
# range() for ranges        IMMUTABLE
# {} for dictionaries       MUTABLE key:value, ...
# {} for sets               value,...
#
#---------------------------------------------------------------------
def elapsed_time(f):
    def wrapper():
        t1 = time.time()
        f()
        t2 = time.time()
        print(f'Elapsed time: {(t2 - t1) * 1000} ms')
    return wrapper


@elapsed_time
def big_sum():      #big_sum() has the decorator @elapsed_time that wraps it
    num_list = []
    print(f'type of big_sum {type(num_list)}')
    
    for num in (range(0, 10000)):
        num_list.append(num)
    print(f'Big sum: {sum(num_list)}')

def main():
    big_sum()       #because it has a DECORATOR, it executes elapsed_time()

# NOTE: 
# without the DECORATOR -i.e. you commented it out, big_sum() will execute 
# the big_sum() function instead of the elasped_time() wrapper
#
# The DECORATOR definition MUST:
#       be right before the function it wraps, and
#       have the name of a defined function
#
# So the DECORATOR seeme useful, for one, if you want to put some instrumentation
# around a function for debugging or logging without making those changes in 
# the function itself.
#
# If for debugging, then you must comment out the decorators
# It seems to be a cleaner approach to having a variable set to determine
# whether or not to print debugging info -like in Perl, becuase in that case you 
# would have the instrumentation code, insied the function and that can make it messy
# just look at your examples and the decorator-statements.py
# 

if __name__ == '__main__': main()
