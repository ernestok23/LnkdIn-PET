#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
#
# [] for lists              MUTABLE, sequential and iterable
# () for tuples             IMMUTABLE
# range() for ranges        IMMUTABLE
# {} for dictionaries       MUTABLE key:value, ...
# {} for sets               value,...

def main():
    kitten('meow', 'grrr', 'purr', 'moe', 'moe', 'moe')
    kitten()

# *args indicates a variable length argument sequence, which is actually a tuple
# and being a tuple it is IMMUTABLE
# it is traditional to call the list of arguments args
# this approach is useful if you nede to call a function with a varying number 
# of arguments
#-------------------------------------------------------------------------------
def kitten(*args):
    i = 1
    if len(args):
        print(f'There are {len(args)} arguments')
        print(f'elemnt 0 is {args[0]}')
        
        for s in args:  # this lists the arguments in the arg list (tuple)
            #print(s)
            print(f'{i} " - " {s}')
            #i += 2
            i += 1  # 2, or -2, etc
    else: print('Meow ... Boooo... no arguments.')

if __name__ == '__main__': main()

#%%
# create a tuple (IMMUTABLE) with the args 
#-----------------------------------------
seq_of_args = ('seq1', 'seq2', 'seq3', 'moe')

# call is passing the tupple: it goes as 1 (one) argument
kitten(seq_of_args)

# call by reference -prefix the tuple with *
# this is useful when you call a function with different numbers of arguments
#
# The difference between this call with (*seq_of_args) and the one above with just 
# (seq_of_args), is the (*seq_of_args) passes various arguments and you may access
# each one as args[i], the (seq_of_args) is just one argument and args[0] will
# return the entire sequence as one element
#-----------------------------------------------------------------------------
kitten(*seq_of_args)
