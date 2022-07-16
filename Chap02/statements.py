#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import platform

# compare with : print('This is python version {}'.format(platform.python_version()))
# this assignment, is an expression but also a statement because 
# it is a line of code by itself
the_version = platform.python_version()

# the print() function is an expression -even thouh we don't use the return value, 
# and it is also a statement 
print('This is python version {}'.format(the_version))
