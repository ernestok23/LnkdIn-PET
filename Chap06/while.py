#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

#--------------------------------------------------------
#
# [] for lists              MUTABLE, sequential and iterable
# () for tuples             IMMUTABLE
# range() for ranges        IMMUTABLE
# {} for dictionaries       MUTABLE key:value, ...
# {} for sets               value,...

#%%
# >>>>> Needed to install a new version of Spyder v5.3.1  because the input() function was throwing an error
# The Python version that came with Spyder v.5.3.1 is 3.8.10 -older than the Spyder v5.1.5 that came with Python 3.9.2 
# with Anaconda.
# Those two versions of Spyder are installed separately. 
# Anaconda comes woth v5.1.5, and hasn't been updated to v5.3.x yet
#
# Imports a module from the library
# you may have multiple import statements
import platform

# print() is a function
print('This is python version {}'.format(platform.python_version()))


# The following is from Ch2 to refresh
# while     iterates on condition
# for ...   iterates over a sequence (a collection type)
#%%

# Note that I included a float in the list below, and the 
# loop runs OK
words = ['one', 'two', 2.34, 'three', 'four', 'five']

#%%
n = 0
while(n < 5):
    print(words[n])
    n += 1
    
print()         # prints a blank line

#%%
# a for loop uses a sequence -collection type- to control the loop
# the body of the loop executes for each item in the collection
#
# this is an easier and more compact way to go through iterable lists, 
# than the while loop
for i in words:     # this iterates through every element in the list
    print(i)

#--------------------------------------------------------

# Now it comes from Ch6
#%%

secret = 'swordfish'
print('The secret is {}'.format(secret))

pepe = input('Input for pepe: ')
print('You entered: {}'.format(pepe))

pw = ''
while pw != secret:
        pw = input('What is the secret word? ')
print('Done')

#%%
# three while and for loop controls are:
#   continue            to go back to the top of the loop and test the condition again
#   break               to exit the loop
#   else                executes only if the loop ends normally, not if break 
#

secret = 'swordfish'
print('The secret is {}'.format(secret))

pw = ''

count = 0
skip_after   = 4
max_attempts = 5

auth = False


while pw != secret: # and count > max_attempts:
    count += 1  
    if count > max_attempts: 
            print('Wrong password')
            break
    else:
            if count > skip_after :  # to skip the remaining attempts to input
               print('Skip {} ...'.format(count))
               continue     
    pw = input(f"{count}:What is the secret word?: ")
else:
    auth = True         # else gets execute ONLY if you exit the loop normally, 
                        # not ny break
        
print('Authorized' if auth else 'NOT AUTHORIZED')


