#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# [] for lists              MUTABLE, sequential and iterable
# () for tuples             IMMUTABLE
# range() for ranges        IMMUTABLE
# {} for dictionaries       MUTABLE key:value, ...
# {} for sets               value,...

# A set is an UNORDERED collection with NO DUPLICATE elements. 
# Like the other collections in Python, members can be of any type
#
# Basic uses include membership testing and eliminating duplicate entries. 
# Set objects also support mathematical operations like union, intersection, 
# difference, and symmetric difference
#
# Curly braces or the set() function can be used to create sets
#
# To create an empty set you have to use set(), not {}; the latter 
# creates an empty dictionary

#----------------------------------------------------------------

import platform

# print() is a function
print('This is python version {}'.format(platform.python_version()))
print('------------')



def main():
    # Define two different sets, using strings with the set() function
    # set() expects only one argument
    a = set("We're gonna need a bigger boat.")
    b = set("I'm sorry, Dave. I'm afraid I can't do that.")
    c = set(range(1,20))
    
    # the following, will print an uordered list of the unique characters in 
    # each string. NO DUPLICATEs
    #
    # { dWa.ngbeit'ro}
    # {v,tofdn'rys.mIeD achi}
    # {12345678910111213141516171819}
    #
    # for the last set,noticed it went from 1 to 19,range() doesn't include 
    # the upper end, also the set() apparently considers each nnumber as unique
    
    #-------------------------------------------------------------------
#%%
    print_set(a)
    print_set(b)
    print_set(c)

#%%
    # SORT: You can sort the sets
    #----------------------------
    print_set(sorted(a))
    print_set(sorted(b))
    print_set(sorted(c))
    
#%%
    # MEMBERSHIP: in operator
    # check is an element is a membr of a set
    #----------------------------------------
    if 'a' in a:
        print('a is in the set a')
    else:
        print('a is NOT the set a')

    if 'S' in a:
        print('S is in the set a')
    else:
        print('S is NOT the set a')

        
#%%
    # MEMBERS of ONE set and NOT the OTHER: - operator
    # Check for members in set a but not in b
    # 
    # this is the output:
    #    
    # The type of delta_a_not_b is: <class 'set'>
    # {gWb}
    # {'g', 'W', 'b'}
    #  DELTA members in A not B: {'g', 'W', 'b'}
    #---------------------------------------------
    print_set(sorted(a))
    print_set(sorted(b))

    # Get the type of the output first, as a curiosity
    delta_a_not_b = a - b
    print(f'The type of delta_a_not_b is: {type(delta_a_not_b)}')

    print_set(delta_a_not_b)
    
    # each member is printed separated
    print(f'DELTA members in A not B: {delta_a_not_b}')
    print(f'len(a) : {len(a)}, len(b) : {len(b)}, len(delta_a_not_b) : {len(delta_a_not_b)}')

    
#%%
    # MEMBER of ONE set OR  the OTHER: | operator
    # this IS the UNION of a and b BECAUSE a set CANNOT contain duplicates
    # so the resulting set of the OR will not contain duplicated elements
    # hence:
    #   Len(a|b) <= len(a) + len(b)
    #---------------------------------------------------------------------
    print_set(sorted(a))
    print_set(sorted(b))

    either_both_a_or_b = a | b
    print(f'The type of either_both_a_or_b is: {type(either_both_a_or_b)}')

    print_set(either_both_a_or_b)
    print(f'OR members of A and B: {either_both_a_or_b}')
    print(f'len(a) : {len(a)}, len(b) : {len(b)}, len(either_both_a_or_b) : {len(either_both_a_or_b)}')
    
    
    # now define two disjoint sets using the set() function
    # with set(), you pass one string
    #
    # This is the output:
    #
    #   {len(set_2)}, len(set_1_OR_2) : {len(set_1_OR_2)}')
    #   UNION of set_1 and set_2: {'1', '2', '3', '7', '9', '8', '34'}
    #   len(set_1) : 3, len(set_2) : 4, len(set_1_OR_2) : 7        
    #-----------------------------------------------------------------
    set_1 = set('123')
    set_2 = {'7', '8', '9', '34'}   # another way of defining a set
    set_1_OR_2 = set_1 | set_2
    print(f'UNION of set_1 and set_2: {set_1_OR_2}')
    print(f'len(set_1) : {len(set_1)}, len(set_2) : {len(set_2)}, len(set_1_OR_2) : {len(set_1_OR_2)}')
    
    

#%%
    # MEMBER of ONE exclusive OR  the OTHER, not both XOR operator
    #-------------------------------------------------------------
    # XOR  members in either or both of a and b: ^ operator
    print_set(sorted(a))
    print_set(sorted(b))

    xor_a_b = a ^ b
    print(f'The type of xor_a_b is: {type(xor_a_b)}')

    print_set(xor_a_b)
    print(f'XOR members of A and B: {xor_a_b}')
    print(f'len(a) : {len(a)}, len(b) : {len(b)}, len(xor_a_b) : {len(xor_a_b)}')

#%%
    # MEMBER of both sets: & operator
    # this is  the INTERSECTION of the sets
    #--------------------------------------
    print_set(sorted(a))
    print_set(sorted(b))

    both_a_and_b = a & b
    print(f'The type of both_a_and_b is: {type(both_a_and_b)}')

    print_set(both_a_and_b)
    print(f'BOTH members of A and B: {both_a_and_b}')
    print(f'len(a) : {len(a)}, len(b) : {len(b)}, len(both_a_and_b) : {len(both_a_and_b)}')


#%%
    p = set('eaeapepe')
    print(f'The type of p is: {type(p)}')

    print(p)
    print_set(p)
    

#%%
def print_set(o):
    print('{', end = '')
    for x in o: print(x, end = '')
    print('}')

#%%
if __name__ == '__main__': main()
