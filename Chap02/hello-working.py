#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# {} are placeholders for variables in a string
# to print a variable value, use the format() method from the string object
# format() is a method of the string object
#
# >>>   a statement is a unit of execution
# >>>   an expression is unit of evaluation
#
# remember: everything in Python is an object
# everything that returns a value is an expression, and a statement
# can also be an expression

x = 42

print('Hello, World.{}'.format(x))  # {} is a place-holder for a variable
                                    # format() is a method of the string object                                   

                                  
s = 'Hello, Worlds.{}'.format(x)
print(s)

# using a f string
print(f'F string - Hello, World . {x}')

y = 36
print('Now I have two vars {} and {}'.format(x,y))

z = 18
print('how about three vars {}, {} and {}'.format(x,y,z))

# storing the string in a var and then printing the var
pepe = 'how about three vars {}, {} and {}'.format(x,y,z)
print(pepe)
