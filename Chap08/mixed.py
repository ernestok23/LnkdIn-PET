#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

"""
In Python, everything is an object and variables store references to objects
Objects can contain references to other objects
This means that it's possible to store anything in a data structure.

# [] for lists              MUTABLE, sequential and iterable
# () for tuples             IMMUTABLE
# range() for ranges        IMMUTABLE
# {} for dictionaries       MUTABLE key:value, ...
# {} for sets               value,...

"""


#%%
import platform

# print() is a function
print('This is python version {}'.format(platform.python_version()))
print('------------')


# globals
dlevel = 0 # manage nesting level

def main():
    r = range(11)   # this is a range
    l = [ 1, 'two', 3, {'4': 'four' }, 5 ]               # this is a list with integers, 
                                                         #     strings, a dictionary
    t = ( 'one', 'two', None, 'four', 'five' )           # this is a tuple
    s = set("It's a bird! It's a plane! It's Superman!") # this is a set
    d = dict( one = r, two = l, three = s )              # this is a dictionary
    mixed = [ l, r, s, d, t ]                            # this is a list

    """
    print(mixed)
    
    This is the output of mixed, that is a list consisting
    of the contents of the variables previously defined
    -------------------------------------------------------
    [[1, 'two', 3, {'4': 'four'}, 5], range(0, 11), 
     {'e', 'b', 'p', 'd', '!', 'i', ' ', 'n', 'l', 'u', 'm', 'a', 'r', 't', 'I', "'", 's', 'S'}, 
     {'one': range(0, 11), 'two': [1, 'two', 3, {'4': 'four'}, 5], 
      'three': {'e', 'b', 'p', 'd', '!', 'i', ' ', 'n', 'l', 'u', 'm', 'a', 'r', 't', 'I', "'", 's',
                'S'}}, 
     ('one', 'two', None, 'four', 'five')
    ]
    """

    disp(mixed)                                          # dispay function
    """    
    This is the output. Note you call disp() with mixed, that is a list consisting
    of the variable previously defined
    
    [ [ 1 'two' 3 { 4: 'four' } 5 ] 
    [ 0 1 2 3 4 5 6 7 8 9 10 ] 
    { ' ' '!' "'" 'I' 'S' 'a' 'b' 'd' 'e' 'i' 'l' 'm' 'n' 'p' 'r' 's' 't' 'u' } 
    { one: [ 0 1 2 3 4 5 6 7 8 9 10 ] two: [ 1 'two' 3 { 4: 'four' } 5 ] three: { ' ' '!' "'" 'I' 'S' 'a' 'b' 'd' 'e' 'i' 'l' 'm' 'n' 'p' 'r' 's' 't' 'u' } } 
    ( 'one' 'two' Nada 'four' 'five' ) 
    ] 
    """



# The structures can be as complicated as we need
# We can iterate through the structures to see what is inside of them
# the disp function eaxmines each element of the argument list and then decide what to do
#
# isinstance() determines whether an object is an instance of a class or subclass
#--------------------------------------------------------------------------------
def disp(o):
    global dlevel

    dlevel += 1
    # isinstance() determines whether an object is an instance of a class or subclass
    # 
    if   isinstance(o, list):  print_list(o)
    elif isinstance(o, range): print_list(o)
    elif isinstance(o, tuple): print_tuple(o)
    elif isinstance(o, set):   print_set(o)
    elif isinstance(o, dict):  print_dict(o)
    elif o is None: print('Nada', end=' ', flush=True)
    else: print(repr(o), end=' ', flush=True)
    dlevel -= 1

    if dlevel <= 1: print() # newline after outer

def print_list(o):
    print('[', end=' ')
    for x in o: disp(x)
    print(']', end=' ', flush=True)

def print_tuple(o):
    print('(', end=' ')
    for x in o: disp(x)
    print(')', end=' ', flush=True)

def print_set(o):
    print('{', end=' ')
    for x in sorted(o): disp(x)
    print('}', end=' ', flush=True)

def print_dict(o):
    print('{', end=' ')
    for k, v in o.items():
        print(k, end=': ' )
        disp(v)
    print('}', end=' ', flush=True)

if __name__ == '__main__': main()
