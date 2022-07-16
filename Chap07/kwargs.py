#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# keyword arguments are like a list of arguments that are dictionaries
# instead of tuples. 
# This allows you to have a function with a variable number of named arguments
#
# [] for lists              MUTABLE, sequential and iterable
# () for tuples             IMMUTABLE
# range() for ranges        IMMUTABLE
# {} for dictionaries       MUTABLE key:value, ...
# {} for sets               value,...

#-----------------------------------------------------------------------------
def main():
    
    # here you called the function with a dictionary
    kitten(Buffy = 'meow', Zilla = 'grr', Angel = 'rawr')



# Note the ** prefixing the function argument
# the function expects a reference to a dictionary
def kitten(**kwargs):       # kwargs: keyword arguments
    i = 1
    if len(kwargs):
       print(f'There are {len(kwargs)} arguments')
      
       # here you go through the dictionary printing the key + values
       for k in kwargs:
           print('Kitten {} says {}'.format(k, kwargs[k]))
           
       i += 1  # 2, or -2, etc
       
    else: print('Meow.')

if __name__ == '__main__': main()

#%%

# defining as a dictionary
x = dict(Buffy = 'meow', Zilla = 'grr', Angel = 'rawr', Genious = 'Mongo Aurelio')

# then call passing a reference to the dictionary
kitten(**x)