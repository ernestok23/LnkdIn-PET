#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
#
#
# [] for lists              MUTABLE, sequential and iterable
# () for tuples             IMMUTABLE
# range() for ranges        IMMUTABLE
# {} for dictionaries       MUTABLE key:value, ...
# {} for sets               value,...
#
# Python uses dynamic tying: it changes the type based on the value of the var
# type(<var>) is a built-in function that prints the type of a var
# you can create your own types as well
# here is just to show the dynamic typing

# In Python everything is an object, so a Type is the same as a Class
# Strings are objects. 
# Even literal strings are objects

x = 7
print('x is {}'.format(x))
print(type(x))    # this is a built-in function that prints the type of a var


x = 7.0
print('x is {}'.format(x))
print(type(x))    


x = 7 / 3        # the result will be a float
print('x is {}'.format(x))
print(type(x))    


x = 7 // 3        # the result will be an int
print('x is {}'.format(x))
print(type(x))    


x = 7 % 3        # the result will be an int, for the remainder
print('x is {}'.format(x))
print(type(x))    




#==========================================================
# DO NOT USE floats FOR MONEY CALCULATIONS
#            ------
#
# The Decimal type is useful for accurate arithmetic calculation 
# (e.g., when money is involved)
#==========================================================
# This is the difference between accuracy and precision
# float are not accurate
#------------------------------------------------------
x = .1 + .1 + .1 - .3        # the result IS NOT ZERO
print('x is {}'.format(x))
print(type(x))    

# to solve the above imprt a module
# from decimal import *
# now it works: for money you will need to convert to Decimal and compute from there
# the type then is decimal.Decimal
# which means it is the Decimal class, 
#              from the decimal library
# that's why the notation <library>.<Class>
from decimal import *      # from decimal import everything
a = Decimal('.10')         # it is in quotes becuase we don't want to pass it as float
b = Decimal('.30')
x = a + a + a - b
print('x is {}'.format(x))
print(type(x))    




# single or double quoutes work the same: the var will be of type string
x = "pepe"
print('x is {}'.format(x))
print(type(x))    


x = 'pepo'
print('x is {}'.format(x))
print(type(x))    


# with three single or double quotes surrouding the strg you can make it multiline
# and will print multiline.
x = '''
pepo
se
fue al
mercado
and will
return
when he is
done
'''
print('x is {}'.format(x))
print(type(x))    


x = True
print('x is {}'.format(x))
print(type(x))



# Comparisaon operators also return boolean values
#--------------------------------------------------
x = 7 > 5
print('x is {}'.format(x))
print(type(x))
    

x = 7 < 5
print('x is {}'.format(x))
print(type(x))


x = 7 == 5
print('x is {}'.format(x))
print(type(x))


# The following evaluates to False
#---------------------------------
#   NoneType
#   0 (zero value)
#   empty string

# This is used to represent the absence of a value
x = None                 # this is the Python NoneType
print('x is {}'.format(x))
print(type(x))    

x = '' #'pepe' #4
if x:
    print('True, x is {}'.format(x))
else:
    print('False, x is gurnisht')

#--------------------------------------------------



# Strings are objetcs. 
# Even literal strings are objects
# so here it calls the capitalize() method
x = 'pepo'.capitalize()
print('x is {}'.format(x))
print(type(x))    

x = 'pepo'.upper()
print('x is {}'.format(x))
print(type(x))    


# using the format method as well, using positional args
x = 'pepo {} {} {}'.format('and', 'pepa', 'pig')
print('x is {}'.format(x))
print(type(x))    

# you can specify positions for the args
x = 'pepo {2} {0} {1}'.format('and', 'pepa', 'pig')
print('x is {}'.format(x))
print(type(x))    


# you can right and left adjust (justify the args)
# I left justify {2} to 15 spaces, and
# right justify {1} to 9 spaces
# nothing for {0}
x = 'pepo {2:<15} {0} {1:>9}'.format('and', 'pepa', 'pig')
print('x is {}'.format(x))

# fills the format of each arg with 0s
# for {0}, it follows with 14 0s to make u the 15 places
# for {1}, it leads with 8 0s to make up the 9 places
x = 'pepo {0:<015} {1:>09}'.format(5, 9)
print('x is {}'.format(x))


x = 'pepo {0:<015} {1:>09}'.format(532, 93445)
print('x is {}'.format(x))



# with no formatting I am getting only the {}
x = 'pepo {} {}'
print('x is {}'.format(x))


# using an f-string
a = 8
b = 9
x = f'pepo {a} and {b}'
print('x is {}'.format(x))

# using the formatting to pad with 0s
x = f'pepo {a:>09} and {b:<09}'
print('x is {}'.format(x))


x = f'pepo {a:<09} and {b:>09}'
print('x is {}'.format(x))

 
#=====================================================================
#type() and id(), "is" operator, isinstance() 
#---------------------------------------------------------------------

# In Python everything is an object, so a Type is the same as a Class
# Strings are objects. 
# Even literal strings are objects
#
# [] for lists              MUTABLE
# () for tuples             IMMUTABLE
# range() for ranges        IMMUTABLE
# {} for dictionaries       MUTABLE
#
#---------------------------------------------------------------------

x = range(1,6)      # IMMUTABLE
print('x is {}'.format(x))
print(type(x))    # this is a built-in function that prints the type of a var

# create a MUTABLE list from a range with the list() consytructor
x = list( range(1,6))      # MUTABLE
print('x is {}'.format(x))
print(type(x))    # this is a built-in function that prints the type of a var


# create a IMMUTABLE tuple from a range with the tuple() consytructor
x = tuple( range(1,6))      # IMMUTABLE
print('x is {}'.format(x))
print(type(x))    # this is a built-in function that prints the type of a var

#%%
# create a MUTABLE dictionary
x = { 'one':1, 
      'two':2, 
      'three':3, 
      'four':4, 
      'five':5 
    }
print('x is {}'.format(x))
print(type(x))    # this is a built-in function that prints the type of a var

# to print the key and value of the dictionary
for m in x:
    print(f'{m} and {x[m]}')

#%%


#print (x.type())        # Error:  the x object no method type()

# again a list
x = [1, 2, 3, 4, 5]
print('x is {}'.format(x))
print(type(x))    # this is a built-in function that prints the type of a var


# again a tuple 
x = (1, 2, 3, 4, 5)
print('x is {}'.format(x))
print(type(x))    # this is a built-in function that prints the type of a var

# another tuple
x = (1, 'two', 3.0, [4, 'four'], 5)
print('x is {}'.format(x))
print(type(x))      # this is a built-in function that prints the type of a var
print(type(x[0]))   # return the type of the 2nd element
print(type(x[1]))   # return the type of the 2nd element
print(type(x[2]))   # return the type of the 2nd element
print(type(x[3]))   # return the type of the 2nd element
print(type(x[4]))   # return the type of the 2nd element

# getting the type of each element from a for loop
# the i is not the index, and rather the element itself
for i in (x):
        print( '{} is of type {}'.format(i,type(i)) )      # this is a built-in function that prints the type of a var

# now we make duplicate of x
y = (1, 'two', 3.0, [4, 'four'], 5)

print('x is {}'.format(x))
print('y is {}'.format(y))
print('--------------------------------')

print('x is of type {}'.format(type(x)))
print('y is of type {}'.format(type(y)))
print('--------------------------------')


# unique identifier for an object: id()
#
# id() returns a unique identifier for each object
# the id() of the following is different because they are 
# two different objects
#
#
# When referred items point to the same IMMUTABLE string, they have the same id.
#
# Lists are MUTABLE objects. So, the Python Memory Manager (PMM) doesn’t reuse 
# the existing list but creates a new one in the memory. 
#
# The return of the is operator depends on the implementation of the PMM
#-----------------------------------------------------------------------
print('x id() is {}'.format(id(x)) ) 
print('y id() is {}'.format(id(y)) )
print('--------------------------------')


print('x[0] id() is {}'.format(id(x[0])) ) 
print('y[0] id() is {}'.format(id(y[0])) )
print('--------------------------------')

print('x[1] id() is {}'.format(id(x[1])) ) 
print('y[1] id() is {}'.format(id(y[1])) )
print('--------------------------------')

print('x[2] id() is {}'.format(id(x[2])) ) 
print('y[2] id() is {}'.format(id(y[2])) )
print('--------------------------------')

print('x[3] id() is {}'.format(id(x[3])) ) 
print('y[3] id() is {}'.format(id(y[3])) )
print('--------------------------------')

print('x[4] id() is {}'.format(id(x[4])) ) 
print('y[4] id() is {}'.format(id(y[4])) )
print('--------------------------------')



# Create two tuples and check the is operator result
# tuples are IMMUTABLE objects
#---------------------------------------------------
p = (1, 2, 3, 4, 5)
q = (1, 2, 3, 4, 5)
print('p is {}'.format(p))
print('q is {}'.format(q))
print('id(p):{}, id(q) {}'.format(id(p), id(q)))
if p is q:
    print('YES p is the same as q')
else:
    print('NO p is NOT the same as q')


# Create two ranges and check the is operator result
# a range is an IMMUTABLE object
#---------------------------------------------------
p = range(5)
q = range (5)
print('p is {}'.format(p))
print('q is {}'.format(q))
print('id(p):{}, id(q) {}'.format(id(p), id(q)))
if p is q:
    print('YES p is the same as q')
else:
    print('NO p is NOT the same as q')


# back to the lists x and y
#
# do two vars reference the same object ?: is operator
# is compares the id() of the two variables
#
# here x is NOT the same as y because they are two different objects
# even though they have the same values
#------------------------------------------------------------------
if x is y:
    print('YES x is the same as y')
else:
    print('NO x is NOT the same as y')

print(len(x))


# loop through the elements and check if they are the same
#---------------------------------------------------------
j = len(x)
i = 0
print('The lengh of the lists is {}'.format(j))
while(i < j):
    print('{} - x: {} and y: {}'.format(i, x[i], y[i]))
    if x[i] is y[i] :
        print('SAME {} , {}'.format( id(x[i]), id(y[i]) ) )
        print()
    else:
        print('DIFFERENT {} , {}'.format( id(x[i]), id(y[i]) ) )
        print()
    i += 1
        


# to check the type of an object: isinstance()
#
# there is a function isinstance() to check the type of an object
# play the following with the various definitions of x above
#----------------------------------------------------------------
if isinstance(x, list):
    print('YES x is a list')
elif isinstance(x, range):
    print('YES x is a range')
elif isinstance(x, tuple):
    print('YES x is a tuple')
else:
    print('NO x is something else')


























