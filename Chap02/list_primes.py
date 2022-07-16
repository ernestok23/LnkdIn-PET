#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# names aare case sensitive
#
# [] for lists              MUTABLE
# () for tuples             IMMUTABLE
# range() for ranges        IMMUTABLE
# {} for dictionaries       MUTABLE
#
#
# Don't confuse a test for PRIME number from a test for an EVEN number
# A PRIME is only divisible by itself and 1
# An EVEN returns zero when divided by 2

def isPrime(n):
    if n <= 1:
        return False
    for j in range(2, n):
        w = (n % j)
        # Step through OK
        #print('isPrime(), n = {}, j = {}, w = {}'.format(n, j, w))
        if w == 0:
            return False
    else:
        return True



def list_Primes(k = 100):
    for i in range(k):      # i < k, that's how the range function works
    
        # This print is good for debugging to show the index of the loop
        # but it will confuse the result: without this print, the primes.
        # will all be lited in one line.
        # with this debugging print, i.e. the line: 
        #    
        #   11 list_Primes(), i = 12
        #
        # indicates that 11 is a prime, followed by a space (from "end = ' ' ")
        # and the print showing the list_Primes() next iteration, in this case 12
        # means 11 is a prime, and because the
        #print('list_Primes(), i = {}'.format(i))
        if isPrime(i):
            
            # print() inserts a newline
            # end inserts a space after the x instead of a newline -which is
            # what happens after each print, and flush is to flush the output buffer
            print(i, end=' ', flush=True)
  
    print()     # this prints a newline by itself
        

#n = 5      
#n = 9      # not prime
n  = 57


# List primes up to a number
#---------------------------
list_Primes(59)

