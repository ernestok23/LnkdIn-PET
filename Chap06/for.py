#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

#
# [] for lists              MUTABLE, sequential and iterable
# () for tuples             IMMUTABLE
# range() for ranges        IMMUTABLE
# {} for dictionaries       MUTABLE key:value, ...
# {} for sets               value,...

# define a tuple of animals
# this can be any sequence or iterator
#-------------------------------------
animals = ( 'bear', 'bunny', 'dog', 'cat', 'velociraptor' )

for pet in animals:
    if pet == 'dog': continue   # skip the print for dog
    #elif pet == 'velociraptor': break

    print(pet)
else:
    print('those are all the animals')
    
    
    
    

#%%

# this can be a range(), this supplies an iterator
for pet in range(5):
    print(pet)


