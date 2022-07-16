#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# names aare case sensitive
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
        print('isPrime(), n = {}, j = {}, w = {}'.format(n, j, w))
        if w == 0:
            return False
    else:
        return True


def isPrime_StepThrough(n):
    if n <= 1:
        return False

    # the for command has an olptional else clause
    # A prime is only divisible by itself and 1
    for j in range(2, n):
        w = n % j
        # Step through OK
        print('isPrime_StepThrough(), n = {}, j = {}, w = {}'.format(n, j, w))
        if w == 0:
            return False
    else:
        return True



def list_Primes(k = 100):
    for i in range(k):
        print('list_Primes(), i = {}'.format(i))
        if isPrime(i):
            
            # end inserts a space after the x instead of a newline -which is
            # what happens after each print, and flush is to flush the output buffer
            #print('list_Primes(), i = {}, k = {}'.format(i, k), end=' ', flush=True)
            print(i, end=' ', flush=True)
  
    print()     # this prints an empty line
        



#n = 5      
#n = 9      # not prime
n  = 37

# Test isprime(n)
#---------------
if isPrime(n):
    print(f'isPrime(): {n} is prime')
else:
    print(f'isPrime(): {n} is NOT prime')


# Test isPrime_StepThrough(n)
#----------------------------
if isPrime_StepThrough(n):
    print(f'isPrime_StepThrough(): {n} is prime')
else:
    print(f'isPrime_StepThrough(): {n} is NOT prime')


# List primes up to a number
#---------------------------
list_Primes(19)

