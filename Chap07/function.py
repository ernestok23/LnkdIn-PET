#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


# All functions return a value
# If you don't specify a return value, it will return 'None'
#
# Python has no distinction between a function and a procedure
#
# When you assign a MUTABLE, you assign a REFERENCE to the MUTABLE
# Function arguments act like assignments
#
# [] for lists              MUTABLE, sequential and iterable
# () for tuples             IMMUTABLE
# range() for ranges        IMMUTABLE
# {} for dictionaries       MUTABLE key:value, ...
# {} for sets               value,...
#-----------------------------------------------------------
def main():
    kitten()
    
    # the following print() prints __main__
    print('This is __name__ {}'.format(__name__) )
    print()


    # Capture the return of kitten()
    # The return value is None of type NoneType
    # because the function didn't return any value
    x = kitten()
    print(f'Back in main(), this is x: {x}, of type {type(x)}')    
    print()
        
   
#-------------------------------------------------------------------
def kitten():
    print('Meow.')
    print('From kitten(), this is the value of __name__ : {}'.format(__name__))


"""
# This special variable __name__ gets its value depending on how we execute the 
# containing script. This lets you decide you whether you want to run the script. 
# Or that you want to import the functions defined in the script.
#
# When you run your script, the __name__ variable equals __main__. 
# When you import the containing script, it will contain the name of the script.
#
# See you example of call_test__name__.py and test__name__.py
#-------------------------------------------------------------
# 1.- When you run test__name__.py, the value of __name__ is __main__
#
# 2.- When you run call_test__name__.py, that imports test__name__.py, 
#     you get the following:
#       from call_test__name__.py, __name__ is __main__
#       from test__name__.py, __name__ is test__name__
# 
"""
# So here, __name__ will return __main__, so I run the main() method
if __name__ == '__main__': main() 


#%%
# Return a value
def retValueKitten():
    print('Return a value from retValueKitten.')
    return(45)

# Capture the return value
x = retValueKitten()
    
# The return value is None of type NoneType
# because the function didn't return any value
print(f'This is x: {x}, of type {type(x)}')    


#%%
# Return a List
def retListKitten():
    print('Return a value from retValueKitten.')
    
    # Notice the return value is enclosed in [] to make it a list
    return([45, 54, 63])

# Capture the return value
x = retListKitten()
    
# The return value is None of type NoneType
# because the function didn't return any value
print(f'This is x: {x}, of type {type(x)}')    
for i in x:
        print(f'From main, this is {i}')


#%%
# Return a tuple
def retTupleKitten():
    print('Return a value from retValueKitten.')
    return(42, 49, 56)

# Capture the return value
x = retTupleKitten()
    
# The return value is None of type NoneType
# because the function didn't return any value
print(f'This is x: {x}, of type {type(x)}')    
for i in x:
    print(f'From main, this is i: {i}')

#%%
# Return a dictionary: bite how you indicate dict(....)
def retDictKitten():
    print('Return a value from retValueKitten.')
    return dict(one = 1, two = 2, three = 3)

# Capture the return value
x = retDictKitten()
    
# The return value is None of type NoneType
# because the function didn't return any value
print(f'This is x: {x}, of type {type(x)}')    
for i in x:
    print(f'From main, this is i: {i} and {x[i]}')


#%%

def argKitten(n):
    print('{} Meow.'.format(n))
    print(f'{n} Meow.')             # using f-string
    
argKitten(5)

#%%
def argKitten(n):
    print('{} Meow.'.format(n))
    print(f'{n} Meow.')             # using f-string

    
# this returns a special None vaue, because the function doesn't explicitly 
# return a value
my_return = argKitten(5)            
print(f'This is the return: {my_return}')


#%%
def arg2Kitten(l, m, n):
    
    print(f'{l}, {m}, {n}')
    print('{} Meow.'.format(l))
    print(f'{n} Meow.')             # using f-string
    
    return("that's the end of meow")
    

my_return = arg2Kitten(1,2,3)   # this returns the strng from the function
print(f'This is the return: {my_return}')

#%%
# Define default values for the arguments, in case you don't pass all the arguments
# Any arguments with default values must be listed after the arguments with 
# expected values
#----------------------------------------------------------------------------------
def argDefaultKitten(l = 'l-default', m = 'm-default', n = 'n-default'):
    
    print(f'{l}, {m}, {n}')
    print('{} Meow.'.format(l))
    print(f'{n} Meow.')             # using f-string
    print('----------------------')
    
    return("that's the end of meow")
    

ret1 = argDefaultKitten()
ret1 = argDefaultKitten(11)
ret1 = argDefaultKitten(11, 22)
ret1 = argDefaultKitten(11, 22, 33)

my_return = argDefaultKitten(1,2,3)   # this returns the strng from the function
print(f'This is the return: {my_return}')

#%%
# Any arguments with default values must be listed AFTER the arguments 
# with expected values
# It is better to have default values for all parameters and hanlde that 
# inside the function
def argDefaultKitten(l, m = 'm-default', n = 'n-default'):
    
    print(f'{l}, {m}, {n}')
    print('{} Meow.'.format(l))
    print(f'{n} Meow.')             # using f-string
    print('----------------------')
    
    return("that's the end of meow")
    

# ret1 = argDefaultKitten()     # this would give you an error: not enough args
ret1 = argDefaultKitten(11)
ret1 = argDefaultKitten(11, 22)
ret1 = argDefaultKitten(11, 22, 33)

my_return = argDefaultKitten(1,2,3)   # this returns the strng from the function
print(f'This is the return: {my_return}')

#%%
# this -and all the above- are calls By-Vvalue
# you pass a copy of the value not a reference
#
# NOTE: integers are IMMUTABLE, so if you pass an integer
#       that value will have the same id()
#-----------------------------------------------------------------------------
def argByValueKitten(n):
    print(f'{id(n)} - {n} from the function.')             # using f-string
    n = 9
    print(f'{id(n)} - {n} from the function AFTER change.')             # using f-string
    print('{} Meow.'.format(n))
    print(f'{n} Meow.')             # using f-string


my_var = 5    
print(f'{id(my_var)} - {my_var} from main')

my_return = argByValueKitten(my_var)        # this returns None

print(f'This is the return: {my_return}')
print(f'{id(my_var)} - {my_var} from main')

#%%
# this is passed "By Value"
# Integers and strings are IMMUTABLE
#-----------------------------------------------------------------------------
def argByValueStrKitten(n):
    print(f'{id(n)} - {n} from the function.')             # using f-string
    n = 'Larry'
    print('{} Meow.'.format(n))
    print(f'{n} Meow.')             # using f-string


my_var = 'Moe'    
print(f'{id(my_var)} - {my_var} from main')

my_return = argByValueStrKitten(my_var)        # this returns None

print(f'This is the return: {my_return}')
print(f'{id(my_var)} - {my_var} from main')


#%%
# Call "By Reference"
# This is really a call By Value, but the value is a reference to a list
# which is a MUTABLE object, and you use it as such (a reference) inside 
# the function 
# When you assign a MUTABLE, you assign a reference to the MUTABLE
#-----------------------------------------------------------------------------
def argByRefKitten(n):
    print(f'{id(n)} - {n} from the function.')             # using f-string
    n[0] = 7
    print('{} Meow.'.format(n))
    print(f'{n} Meow.')             # using f-string


my_var = [5]        # this is a list -MUTABLE
print(f'{id(my_var)} - {my_var} from main')
my_return = argByRefKitten(my_var)        # this returns None

#print(f'This is the return: {my_return}')
print(f'{id(my_var)} - {my_var} from main')





