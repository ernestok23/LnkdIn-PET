#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


# [] for lists              MUTABLE, sequential and iterable
# () for tuples             IMMUTABLE
# range() for ranges        IMMUTABLE
# {} for dictionaries       MUTABLE key:value, ...
# {} for sets               value,...

# A list COMPREHENSION is a list CREATED based on another list or iterator
# It also works for sets

#%%
import platform

# print() is a function
print('This is python version {}'.format(platform.python_version()))
print('------------')

#%%
def main():
    seq = range(11) # range from 0 to 10
    print_list(seq)

#%%
    # create a LIST comprehension
    #----------------------------
    seq2 = [x * 2 for x in seq]
    print_list(seq2)


#%%    
    # get a LIST of members not divisible by 3
    #-----------------------------------------
    seq3 = [x for x in seq if x % 3 != 0]
    print_list(seq3)

#%%    
    # create a LIST of tuples
    #------------------------
    seq_tuples = [(x, x**2, x**3)  for x in seq]
    print_list(seq_tuples)


#%%    
    # create a LIST from a function
    # here import the value of PI, and create a list of pi rounded to the
    # number of decimals determined by the value of each element in seq
    #--------------------------------------------------------------------
    from math import pi
    seq_function = [round(pi, i) for i in seq]
    print_list(seq_function)


#%%    
    # create a SET
    #-------------
    seq_dict2 = {x for x in 'porca miseria' if x not in 'ps'}
    print_list(seq_dict2)


#%%    
    # create a DICTIONARY
    #--------------------
    seq_dict = {x:x**2 for x in seq}
    print_items(seq_dict)

#%%
def print_list(o):
    for x in o: print(x, end = ' ')
    print()


def print_items(o):
    for k, v in o.items():
        print(f'This is k:v : {k}:{v}')



#%%
if __name__ == '__main__': main()
