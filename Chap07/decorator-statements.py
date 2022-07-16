#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# Just test the decorators
# Remmber: everything in Python is an object
# Functions and blocks define scopes
# use f-strings if you intend to include a variable in the string, otherwise use print

#
# [] for lists              MUTABLE, sequential and iterable
# () for tuples             IMMUTABLE
# range() for ranges        IMMUTABLE
# {} for dictionaries       MUTABLE key:value, ...
# {} for sets               value,...
#

#-------------------------------------------
import platform

the_version = platform.python_version()
print('This is python version {}'.format(the_version))
#--------------------------------------------------------------

#%%
"""
A DECORATOR is a form of metaprogramming and it can be described as a 
special type of function that returns a WRAPPER function.
"""
def f1():
    print('this is f1')
    
f1()        # call f1() by itself

# Everything in Python is an object. f1 is a function object
# Here assign the function object f1 to the variable x, without the paranthesis
#------------------------------------------------------
x = f1()        # without the ()

# Since everything is an object, a variable is an object too and I can simply 
# call the function f1 by calling x. 
#------------------------------------------------------
x()         # call f1() via x    

#--------------------------------------------------------------

#%%
"""
Here, f1_1() is a WRAPPER function for f2():
    f2 is defined within the scope of f1, so 
    you CAN'T call f2 directly

The following is the output of the execution of this cell:
    The execution starts after the deinition of the functions

--> START of execution
--> ASSIGNMENT x = f1_1 - This is x: <function f1_1 at 0x000001D8578D7C10>
--> TRACE def f1_1() - this is f1_1: <function f1_1 at 0x000001D8578D7C10>
--> CALL TRACE def f2 - this is f2: <function f1_1.<locals>.f2 at 0x000001D85924E700>
--> TRACE From f1_1(), post-f2 call
--> This is the x_return: <function f1_1.<locals>.f2 at 0x000001D85924E700>
------------------------------
------------------------------
>>>>>> Just for kicks: 
--> TRACE def f1_1() - this is f1_1: <function f1_1 at 0x000001D8578D7C10>
--> CALL TRACE def f2 - this is f2: <function f1_1.<locals>.f2 at 0x000001D85924EAF0>
--> TRACE From f1_1(), post-f2 call
--> This is the return of y = f1_1(): <function f1_1.<locals>.f2 at 0x000001D85924EAF0>
------------------------------
--> TRACE def f1_1() - this is f1_1: <function f1_1 at 0x000001D8578D7C10>
--> CALL TRACE def f2 - this is f2: <function f1_1.<locals>.f2 at 0x000001D85924E5E0>
--> TRACE From f1_1(), post-f2 call
--> This is the return of z = f1_1(): <function f1_1.<locals>.f2 at 0x000001D85924E5E0>
------------------------------
--> ASSIGNMENT xx = f1_1 - This is xx: <function f1_1 at 0x000001D8578D7C10>
--> TRACE def f1_1() - this is f1_1: <function f1_1 at 0x000001D8578D7C10>
--> CALL TRACE def f2 - this is f2: <function f1_1.<locals>.f2 at 0x000001D85924E940>
--> TRACE From f1_1(), post-f2 call
--> This is the xx_return: <function f1_1.<locals>.f2 at 0x000001D85924E940>

From the above, he M of f1_1 remains the same through various calls, since it was 
defined in the main program
HOWEVER, on each call to f1_1() allocates its own space, and so the M address for 
f2() VARIES and that MAKES SENSE, since in general a function maybe called multiple 
times from the same active transaction, and each call will have to retain the values of their
executions


"""
#----------------------------------------------------------------------
def f1_1():         
    print(f'--> TRACE def f1_1() - this is f1_1: {f1_1}')

    def f2(n):
        print(f'--> {n} TRACE def f2 - this is f2: {f2}')

    # At this indentation, you are in the f1_1() context
    #-------------------------------------------------------
    f2('CALL')     # call f2()                               
    print('--> TRACE From f1_1(), post-f2 call' )
    
    return f2     # f1_1() returns the object f2


# Assign the function object f1_1 to the variable x
#----------------------------------------------------------------    
print('--> START of execution')
x = f1_1                
print(f'--> ASSIGNMENT x = f1_1 - This is x: {x}')    # this is the M address of f1_1()


x_return = x()     # calls f1_1(), which executes f2() and returns the function object f2   

# print the x() return value: x_return, which IS f2
#--------------------------------------------------------------
print(f'--> This is the x_return: {x_return}')
print('------------------------------')
print('------------------------------')

# Just for kicks
#---------------
print('>>>>>> Just for kicks: ')
y = f1_1()                
print(f'--> This is the return of y = f1_1(): {y}')    # this is the M address of f2() returned by f1_1()
print('------------------------------')

z = f1_1()                
print(f'--> This is the return of z = f1_1(): {z}')    # this is the M address of f2() returned by f1_1()
print('------------------------------')


xx = f1_1    
print(f'--> ASSIGNMENT xx = f1_1 - This is xx: {xx}')    # this is the M address of f1_1()
xx_return = xx()     # this calls f1_1(), which executes and calls f2() from inside
print(f'--> This is the xx_return: {xx_return}')

#--------------------------------------------------------------
#--------------------------------------------------------------
#--------------------------------------------------------------

#%%
"""
Now we are going to create a DECORATOR

A DECRATOR is a function that returns another function, usually applied 
as a function transformation using the @wrapper syntax
"""

# f1_3() is a wrapper for f2()
def f1_3(f):         # takes an argument that it will use as a function
    def f2():
        print(f'--> TRACE this is f2 BEFORE function call: {f2}')
        f()     # call f3 -the function that was passed in the argument list
        print(f'--> this is f2 AFTER function call: {f2}')
        #------------------------------------------
        # no return from f2


    print(f'--> TRACE this is f1_3: {f1_3}')
    print(f'--> TRACE this is the ARGUMENT f: {f}')
    print(f'--> TRACE this is f1_3.f2: {f2}')
    f2()

    return f2     # the return value from f1_3 is the function object f2


def f3():
        print(f'--> TRACE this is f3: {f3}')

print('--> START of execution')
x1_3 = f1_3(f3)                    # assign the return value, which is f2
print(f'--> ASSIGNMENT x1_3 = f1_3(f3) - This is x: {x1_3}')  # M address of f2


# I am going to execute x1_3() that will run f2()
#------------------------------------------------
# remember I can't call f2() directly, but I can call it 
# using x1_3()
#
# NOTE: x1_3 has the value of f2, from the return above: x1_3 = f1_3(f3)
# and f2() has no return value and that's why x1_3_return is None
#
# So in this case, f1_3() is a WRAPPER function for f2()
# Remember: you can't call f2() directly
x1_3_return = x1_3()    # this actually calls f2()
print(f'This is the x1_3_return: {x1_3_return}')    # print the return value


#%%
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------

# just create a DECORATOR without all the comments and without passing an 
# argument to the wrapper function f1_4()
#------------------------------------------------------------------------
def f1_4():         # takes an argument that it will use as a function
    def f2_4():
        print(f'--> this is f2_4: {f2_4}')

    print(f'--> this is f1_4: {f1_4}')
    f2_4()

    return f2_4  

#------------------------------------------------------
print('-------------------------')
x1_4  = f1_4    # assigns the function object f1_4
x1_4f = f1_4()  # assigns the return value of f1_4(), the function object f2_4

print(f'This is the x1_4: {x1_4}')    

a = x1_4()    # call x1_4 as if it were a function       
print(f'This is the a: {a}')    

b = x1_4f
print(f'This is the b: {b}')    




