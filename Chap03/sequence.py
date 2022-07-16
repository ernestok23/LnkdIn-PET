#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

#
# [] for lists              MUTABLE, sequential and iterable
# () for tuples             IMMUTABLE
# range() for ranges        IMMUTABLE
# {} for dictionaries       MUTABLE key:value, ...
# {} for sets               value,...
#
# Sequence Types:  any element can be of any type
#
#     MUTABLE:  Lists 
#
#   IMMUTABLE:  Tuples
#               Ranges
#-------------------------------------------
#
#-------------------------------------------
# List: created with [] - MUTABLE
#-------------------------------------------
# a list is created with []
# a list is a MUTABLE sequence, meaning, you can reassign the value of 
# an element
x = [ 1, 2, 3, 4, 5 ]
for i in x:
    print('i is {}'.format(i))

# each item can be of different types
x = [ 1, 'two' ,3.0 , 4, 5 ]
for i in x:
    print('i is {}'.format(i))


x[2] = 55          # position indxex starts at 0
for i in x:
    print('i is {}'.format(i))
    

    


#-------------------------------------------
# Tuples: created with () - IMMUTABLE
#-------------------------------------------
# a tuple is like a list but it is IMMUTABLE
# it is delimited by ()
y = ( 11, 22, 33, 44, 55 )
for i in y:
    print('i is {}'.format(i))

y[1] = 12          # this is an error


#--------- From the video
# I find that it's generally a good idea to favor the immutable type tuple over 
# the immutable type list, unless you know that you need to change the elements 
# in the list. So, I'll tend to use the parentheses by default, and only use 
# the square brackets when I know that I need to change something. 
#------------------------------------------------------------------------------
# My thoughts:
# This will prevent changing something in the list by mistake
# And especially true if a program will be doing its own inferencing
#
# Reference data should go on Tuples
# It is a good feature of the language to have this distinction between 
# Lists and Tuples
#------------------------------------------------------------------------------



#-------------------------------------------
# Range: is IMMUTABLE
#        {end}      starts at zero
#        {start [, [end] [, [step]] ] }
#-------------------------------------------
z = range(12)       # start at 0 up to (12 
for i in z:
    print('i is {}'.format(i))


z = range(2,12)     # start, end  at [2, 12)
for i in z:
    print('i is {}'.format(i))



z = range(2,51, 3)     # start, end, step by 3 ; [2,51)
for i in z:
    print('i is {}'.format(i))

# I can't change the value of a range item. Ranges are Immutable
z = range(2,12)     # start, end  at [2, 12)
for i in z:         # just to veriy the range
    print('i is {}'.format(i))


a = z[2]
print(a)
print('z[2] = {}'.format( z[2] ) )
print('z[2] = {}'.format( a ) )

#z[2] = 99       # this will give an error becuase ranges are immutable
#-------------------------------------------------------------




# I can construct a MUTABLE list with the result from range()
# using the list() constructor
#-------------------------------------------------------------
z_list = list( range(1,51, 4) )
for i in z_list:
    print('i is {}'.format(i))

    
# Here I can change the value of an element of the list  
print('z_list[5]: {}'.format(z_list[5]))    # before
z_list[5] = 777
print('z_list[5]: {}'.format(z_list[5]))    # after

for i in z_list:
    print('i is {}'.format(i))    



    
    
#-------------------------------------------
# Dictionaries are MUTABLE
#
# Dictionary: it is a searchable sequence of key:value pairs
# any elemkent -key, value, can be of any type
#
# In this case the key is a literal, much like in Perl that
# is a key to a value, not necessarily a numerical index
#-----------------------------------------------------------
#x = { 'one':1, 'two':2, 'three':3, 'four':4, 'five':5 }
# this is the same as the line above, but in the more familiar display
x = { 'one':1, 
      'two':2, 
      'three':3, 
      'four':4, 
      'five':5 
    }
for i in x:
    print('i is {}'.format(i))      # this just gives me the keys



# to get the pair key:value for each element in the dictionary
#---------------------------------------------------------
for k, v in x.items():                  # this returns two tuples, 
    print('k: {}, v:{}'.format(k, v))   # for the key and the value



k = 'three'
print('k: {}, v:{}'.format(k, x[k]))   # before

x[k] = 'pepe'                     # update the value of a key
print('k: {}, v:{}'.format(k, x[k]))   # after


for k, v in x.items():                  
    print('k: {}, v:{}'.format(k, v))   # this gives me the key:value pairs






    
    


