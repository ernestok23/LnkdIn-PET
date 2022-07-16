#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

"""
# [] for lists              MUTABLE, ordered collection, sequential and iterable
# () for tuples             IMMUTABLE
# range() for ranges        IMMUTABLE
# {} for dictionaries       MUTABLE key:value, ...
# {} for sets               value,...
#----------------------------------------------------------------

With 
    list.append()   add at the end
    list.pop()      pop from the end

you can use the list as a stack


Smart exercise:
---------------    
Given:          x = ['-','X','X','-']
to make it into     ['-','-','X','X']
you will do: 
    x.insert(0,x.pop())

    which means, you insert at the beginning, the character you pop form the end

"""

import platform

# print() is a function
print('This is python version {}'.format(platform.python_version()))

#%%


def main():
    game = [ 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock', 'Moe', 'Larry', 'Curly', 'Tom', 'Jerry', 'BugsBunny', 'RoadRunner' ]
    print('ORIGINAL: ', end=' ', flush=True)
    print_list(game)


    # Make a copy to test sort
    #-------------------------
    game_copy = game
    print('COPY: ', end=' ', flush=True)
    print_list(game_copy)


    # SORT: the sort() and reverse() changes the list permanently
    #------------------------------------------------------------
    game_copy.sort()
    print_list(game_copy)

    game_copy.reverse()
    print_list(game_copy)


    # this sorts but keeps the list in the original order
    #------------------------------------------------------
    # game.sorted()            # <<< This is an ERROR
    print_list(sorted(game))   # <<< This works abd keeps game as original   


    # this way you can sort

    
    # Access an individual item in the list
    #---------------------------------------
    print(f'This is game[2]: {game[2]}')

    
    # Access a SLICE of the list, [): includes the start, not the end
    #-----------------------------------------------------------------
    print(f'SLICE: This is the slice game[1:4]: {game[1:4]}')
    print(f'SLICE: This is the slice game[1:4]: {game[0:5:2]}')
    
 
    # Access a SLICE of the list with a step
    # like range, you have start, stop, step
    #---------------------------------------
    print(f'SLICE by STEP: This is the slice game[1:7:2]: {game[1:7:2]}')

 
    # SEARCH a list for the index() of an element
    # everything is an object: use the <list>.index() method
    #-------------------------------------------------------
    i = game.index('Moe')   
    print(f'SEARCH: This is i {i}, for Moe game[i]: {game[i]}')
    print(game[i])
 
    # Lists are MUTABLE, so I can APPEND() an item at the end
    #-------------------------------------------------------
    game.append('Shemp')   
    print('APPEND: ', end=' ', flush=True)
    print_list(game)


    # Lists are MUTABLE, so I can INSERT() an item at a position
    #---------------------------------------------------------
    game.insert(1, 'Donut')   
    print(f'INSERT: This is game[1]: {game[1]}')
    print_list(game)

 
    # Lists are MUTABLE, so I can CHANGE an item
    #-------------------------------------------
    game[3] = 'The' + game[3]
    print(f'CHANGE: This is game[3]: {game[3]}')
    print_list(game)


    # Lists are MUTABLE, so I can REMOVE() an item By Value
    #-----------------------------------------------------
    game.remove('Paper')
    print('REMOVE by VALUE - Paper : ', end=' ', flush=True)
    print_list(game)

    
    # Lists are MUTABLE, so I can REMOVE() an item By Index
    # using POP(i)
    #------------------------------------------------------
    game.pop(4)
    print('REMOVE by INDEX - 4 : ', end=' ', flush=True)
    print_list(game)


    # Lists are MUTABLE, so I can POP() remove from the end
    # returns the removed value
    #-------------------------------------------------------
    ret_pop = game.pop()
    print('REMOVE from the END : ', end=' ', flush=True)
    print(f'REMOVED: {ret_pop}')
    print_list(game)


    # POP(i) and element at a particular index
    #------------------------------------------
    print(game[3])
    ret_pop = game.pop(3)
    print('REMOVE at 3: ', end=' ', flush=True)
    print(f'REMOVED: {ret_pop}')
    print_list(game)



    # Lists are MUTABLE, so I can DELete an item by index
    # using del, and you will get the same result
    #----------------------------------------------------
    del game[1]     # does not return a value. I prefer the method for the same
    print('DEL by INDEX - 1 : ', end=' ', flush=True)
    print_list(game)


    # DELete elements by SLICE
    #----------------------------------------------------
    print_list(game)
    del game[0:5:2]     # does not return a value. I prefer the method for the same
    print('DEL by start.stop,step - 0:5:2 : ', end=' ', flush=True)
    print_list(game)




    # Join lists using JOIN() on a string type
    # This is the output:
    # JOIN ", ":  Tom, Spock, Scissors, RoadRunner, Paper, Moe, Lizard, Larry, Jerry, Curly, BugsBunny    
    #-----------------------------------------
    print('JOIN ", ": ', end=' ', flush=True)
    print(', '.join(game))
    
    
    comma_list = ', '.join(game)    
    print(f'This is comma_list: {comma_list}')
    print('------------')


    # Get a COUNT of the list with len() function, not an object method
    #------------------------------------------------------------------
    print(f'The LENGTH of game is {len(game)}')




#-------------------------------------------------------------------
#-------------------------------------------------------------------

# A TUPLE works the same as a list, except that is it IMMUTABLE and indicated
# by parenthesis
# You CAN'T append, insert, pop, change etc because it is IMMUTABLE

    game = ( 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock', 'Moe', 'Larry', 'Curly', 'Tom', 'Jerry', 'BugsBunny', 'RoadRunner')
    print('ORIGINAL: ', end=' ', flush=True)
    print_list(game)



#%%
def print_list(o):
    for i in o: 
        print(i, end=' ', flush=True)
   
    print()
    print('------------')
    print()     # this is an extra line at the end 



if __name__ == '__main__': main()

