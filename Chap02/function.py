#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# All functions return a value
# def defines the function
# the definition always takes paranthesis even if the function takes no args

# [] for lists              MUTABLE, sequential and iterable
# () for tuples             IMMUTABLE
# range() for ranges        IMMUTABLE
# {} for dictionaries       MUTABLE key:value, ...
# {} for sets               value,...

#----------------------------------------------------------------------------
def function(n):
    print(n)


# here I provide a default arg in case I call the function with no values
def function_with_default(n = 23):
    print(n)


# here I provide a default arg + a return statement to return value(s)
def function_with_default_and_return(n = 36):
    print(n)
    return(n, n*2, n*3, n**2, n**3)



function(47)
function()      # this call gives an error b/c the function needs as arg

function_with_default(18)   # here it will use the arg I am passing
function_with_default()     # in this case it returns the defined return value


# All functions return a value
#-----------------------------
# If I run the program at this stage, note the the line below is an assignment
# of the return value of the function called, function_with_default(), 
# so the function will execute and it will do what it does: it will print 
# defined default value that's why you see it in the console; 
#  as for x, it will contain the return value of the function, which is nothing, 
# that's why the print below prints None, which
# is a keyword a special value in Python that means the absence of a value
x = function_with_default()
print('this is x: {}'.format(x))

#%%
# Now printing the default, and ALSO returning a value
#-----------------------------------------------------
y = function_with_default_and_return()
print('this is y: {}'.format(y))
print(f'this is y[3]: {y[3]}')

# slice the tuple
#----------------
y_select = y[1:3]
print(f'this is y_select from y[1:3]: {y_select}')


#%%
# The range specification does not include the upper bound, so I have to go len()+1
# to consider the last element in the tuple
#---------------------------------------------------------------------------
print('this is y: {}'.format(y))
y_step_slice = y[0:5:2]
print(f'this is y_step_slice from y[0:5:2]: {y_step_slice}')

# IT WILL NOT GIVE AN ERROR: go beyond the available elements in the tuple: 
# but it will only print up to the available elements in the tuple
#---------------------------------------------------------------------------
y_step_slice = y[0:9:2]
print(f'this is y_step_slice from y[0:9:2]: {y_step_slice}')


 