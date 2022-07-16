#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# [] for lists              MUTABLE, sequential and iterable
# () for tuples             IMMUTABLE
# range() for ranges        IMMUTABLE
# {} for dictionaries       MUTABLE key:value, ...
# {} for sets               value,...
#----------------------------------------------------------------

import platform

print('This is python version {}'.format(platform.python_version()))
print('------------')


def main():
    # A dictionary is defined with {<key>:<value>, ...}
    #
    # Keys and Values can be of ANY type
    # Keys MUST be IMMUTABLE (of course), strings and numbers 
    # can always be keys
    #
    #--------------------------------------------------
    animals = { 'kitten': 'meow', 
                'puppy': 'ruff!', 
                'lion': 'grrr',
                'giraffe': 'I am a giraffe!', 
                'dragon': 'rawr'
              }
    print_dict(animals)

#%%
   # you can also create a dictionary using a dictionary dict()
   # CONSTRUCTOR
   # Note the syntactic differences: 
   #    () instead of {}, and
   #    ,  instead of :
   #
   # It is a bit easier to type and to read, for the same result
   #----------------------------------------------------------------
    people = dict( one = 'Moe', 
                   two = 'larry', 
                   three = 'Curly',
                 )
    print_dict(people)

#%%
    print_dict(animals)
    
    # also print with the <dict>.items() method 
    #
    # for k, v in animals.items():
    #    print(f'This is k:v : {k}:{v}')
    #------------------------------------------
    print_items(animals)
    

    # also print with the <dict>.keys() method 
    #------------------------------------------
    #for k in animals.keys(): print(f'This is the key k : {k}')
    print_keys(animals)

    # Similarly for values
    #---------------------
    print_values(animals)


    # A dictionary is indexed byt its keys
    # print a specific value
    #-------------------------------------
    print(f"This is animals['giraffe']: {animals['giraffe']}")


    # Change a value
    #-----------------------
    print(f"BEFORE: This is animals['giraffe']: {animals['giraffe']}")
    animals['giraffe'] = 'La jirafa'
    print(f"AFTER: This is animals['giraffe']: {animals['giraffe']}")


    # Add a value
    #------------
    animals['dog'] = 'Wow'
    print(f"ADD: This is animals['dog']: {animals['dog']}")
    print_items(animals)


    # SEARCH for  key using the IN operator
    #---------------------------------------
    print('dog' in animals)     # returns True
    print('Found it!' if 'dog' in animals else 'Gurnisht') # Print something
    

    # Use the <dict>.get() method to return a value if you don't know if 
    # the key exists, otherwise you get an error for a wrong key
    #------------------------------------------------
    print(animals.get('dogg'))  # Returns None
    print(animals.get('lion'))  # Returns the value


#%%
    print_dict(people)
    print_items(people)
    print_keys(people)
    print_values(people)

#%%
def print_dict(o):
    for x in o: print(f'{x}: {o[x]}')


def print_items(o):
    for k, v in o.items():
        print(f'This is k:v : {k}:{v}')


def print_keys(o):
    #for k in animals.keys(): print(f'This is the key k : {k}')
    for k in o.keys(): 
        print(f'This is the key k : {k}')


def print_values(o):
    for v in o.values(): 
        print(f'This is the value v : {v}')




if __name__ == '__main__': main()

    
