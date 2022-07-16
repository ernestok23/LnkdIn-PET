#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# Note that I included a float in the list below, and the 
# loop runs OK
words = ['one', 'two', 'three', 6.78, 'four', 'five']


# this is an easier way to go through iterable lists, than the while loop
for i in words:   # this iterates -in order- through every element in the list
    print(i)

