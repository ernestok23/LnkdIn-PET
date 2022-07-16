# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 20:29:59 2022

@author: kuper

# Script: call_test__name__.py
# Use:      to test the return of the __name__ special variable
#           from itslef and also being from the imported script
#           test__name__.py

"""

# note that the import DOES NOT take the expension py of the imported file
# Pyhton will add that when looking for that file
#-------------------------------------------------------------------------
import test__name__ as tn

def main():
    tn.kitten()
    print('FROM call_test__name__.main(): This is __name__ {}'.format(__name__) )


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
if __name__ == '__main__': main()
