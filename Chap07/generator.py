#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

#
# [] for lists              MUTABLE, sequential and iterable
# () for tuples             IMMUTABLE
# range() for ranges        IMMUTABLE
# {} for dictionaries       MUTABLE key:value, ...
# {} for sets               value,...

"""
A generator is a special class of function that serves as an iterator.
Instead of returning a single value the generator returns a stream of values.

The range() is a generator
"""


def main():
    #for i in range(25):
    #for i in inclusive_range(25):
    for i in inclusive_range(3,12,2):
        print(i, end = ' ')
    print()

"""
Example of range with a negative increase

a = range(10,-20,-2)    # a is just a var containing the range() function
list_a = list(a)        # create a list based on the range from a, and assign it to list_a
print(list_a)
[10, 8, 6, 4, 2, 0, -2, -4, -6, -8, -10, -12, -14, -16, -18]


the range will stop if the stop value is greater than the range computed value 
so the following will give an empty list
a = range(0,20,-2)
list_a = list(a)
print(list_a)
[]


even this will give yu an empty list, since the stop > start (10=10)
a = range(10,10,-2)
list_a = list(a)
print(list_a)
[]


now, list_a will only have the start 11
a = range(11,10,-2)
list_a = list(a)
print(list_a)
[11]


"""

# this is the generator function
def inclusive_range(*args):     # *args is a variable argument list
    numargs = len(args)         # number of args
    print(f'Received {numargs} arguments')
    #print(numargs)
    
    start = 0
    step = 1
    
    # initialize parameters for the range
    # range() can take 1,2 or 3 args, for start, stop and step respectively
    if numargs < 1:
        raise TypeError(f'expected at least 1 argument, got {numargs}')
    elif numargs == 1: 
        stop = args[0]      # the number is the max for the range, the stop
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    else: raise TypeError(f'expected at most 3 arguments, got {numargs}')

    # generator
    i = start
    while i <= stop:        # note the <= t be inclusive on the max of the range
        # yield is like return, but for the generator, which means
        # the execution goes back to the calling function until it yields 
        # the next value
        #
        # The yield call will return a value to the calling function, 
        # and then resume inside the generator function
        yield i

        print('i: {} is of type {}'.format(i, type(i)))
        i += step

if __name__ == '__main__': main()


#%%
"""
This is the output of the following

generator start = 3, stop = 5
BEFORE yield - start = 3
counter = 3
AFTER yield - start = 3
BEFORE yield - start = 4
counter = 4
AFTER yield - start = 4
BEFORE yield - start = 5
counter = 5
AFTER yield - start = 5

Note that it enters the generator function only once
On yield, it goes back to the calling function until the next yield
"""

def generator(start, stop):
    print(f'generator start = {start}, stop = {stop}')
    
    while (start<=stop):
        # The yield call will return a value to the calling function, 
        # and then resume inside the generator function
        print(f'BEFORE yield - start = {start}')
        
        yield start
        
        # This print comes coming back from the calling function
        # of course it will be the same start value as BEFORE
        print(f'AFTER yield - start = {start}') 
        
        start += 1

for counter in generator(3,5):
    print(f'counter = {counter}')
    # at this point it goes back to the generator function 
        
        
        
        
        
        
        
        
        