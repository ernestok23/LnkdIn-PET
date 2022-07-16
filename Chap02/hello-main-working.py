#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import platform

# a block is delimited by indentation, and is indicated by the common indents
# a comment ends at the end of the line
# the end of the line is significant in Python

def main():
    message()

def message():
    # to print a variable value, use the format() method from the string object
    # remember: everything in Python is an object
    # everything that returns a value is an expression, and a statement
    # can also be an expression
    print('This is python version {}'.format(platform.python_version()))
    print('line 2')
    print('spizzicuzzi')
#        print('line 3')    # this will give an error due to wrong indentation

#   The if statement defines a separate block
    #if True:
    if False:
        print('a bailar con las mas gorda')
    else:
        print('a bailar con las mas alegre')

# The following will be executed first because it is outside all blocks
# and will be executed even beore main() is executed       
print(">>>> Executed before main(), because it is outside any blocks")



# main() is called here from this conditional statement
# this is a very common pattern
# you can see: if there is a main, then execute teh main() function in the file
#
# this forces the interpreter to read the entire script before execution
if __name__ == '__main__': main()


