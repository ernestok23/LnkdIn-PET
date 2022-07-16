#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 18
y = 13
#x = 89

# blocks have to be indented and that indentation defines the block
# lines in the block have to be indented at the same level to be considered 
# part of the same block.
# You may nest blocks, and they will have their own indentation within 
# the parent (contaning) block
#
# Blocks DO NOT define the scope of variables
#
# There are no CASE or SWITCH statements in Python.
# You can have the same logic with a string of if, elif, else 
if x < y:
    z = 1
    print('x < y: x is {} and y is {}'.format(x, y))
elif x <= 15:
    z = 2
    print('x is <=5 {}'.format(x))
elif x <= 20:
    z = 3
    print('x is <=20 {}'.format(x))
elif x <= 50:
    z = 4
    print('x is <=50 {}'.format(x))
else:
    z = 5
    print('en que quedamo a la final x > y: x is {} and y is {}'.format(x, y))
    
print('z value is: {}'.format(z))
