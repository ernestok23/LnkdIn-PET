#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


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