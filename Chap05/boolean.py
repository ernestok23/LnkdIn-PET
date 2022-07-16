#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
#
#----------------------------------------------------------------------------
# AND, OR, NOT
# and also
# in        Value in set
# not in    Value not in set
# is        Same object identity id()
# is not    not sme object identity id()
#
#----------------------------------------------------------------------------
#%%
a = True
b = False
x = ( 'bear', 'bunny', 'tree', 'sky', 'rain' ) # x is  collection
y = 'bear'

if a and b:
    print('expression is true')
else:
    print('expression is false')
#%%

if not b:
    print('expression is true')
else:
    print('expression is false')
    
#%%
if not a:
    print('expression is true')
else:
    print('expression is false')
    
#%%
if y in x :
    print('expression is true')
else:
    print('expression is false')
    
#%%    
if 'pepe' in x :
    print('expression is true')
else:
    print('expression is false')
    
#%%
if 'tree' in x :
    print('expression is true')
else:
    print('expression is false') 
   
#%%
if y not in x :
    print('expression is true')
else:
    print('expression is false')

#%%
# this is true because strings are not mutable
if y is x[0] :
    print('expression is true')
else:
    print('expression is false')

print('id(y) is: {}'.format(id(y)))
print('id(x[0]) is: {}'.format(id(x[0])))

#%%
if y is x[1] :
    print('expression is true')
else:
    print('expression is false')

print('id(y) is: {}'.format(id(y)))
print('id(x[1]) is: {}'.format(id(x[1])))

#%%
if y is not x[1] :
    print('expression is true')
else:
    print('expression is false')

print('id(y) is: {}'.format(id(y)))
print('id(x[1]) is: {}'.format(id(x[1])))




