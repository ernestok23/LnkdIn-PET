#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import platform

# a block is delimited by indentation, and is indicated by the common indents

def main():
    message()

def message():
    print('This is python version {}'.format(platform.python_version()))
    print('line 2')
#        print('line 3')    # this will give an error due to wrong indentation


# ths following is outside of any function and will be executed even before main()
print('line5')


# main() is called here from this conditional statement
# this is a very common pattern
# you can see: if there is a main, then execute teh main() function in the file
#
# this forces the interpreter to read the entire script before execution
if __name__ == '__main__': main()
