#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# simple fibonacci series
# the sum of two elements defines the next set

a, b = 0, 1
while b < 1000:
    #print(b, end = ' ', flush = True)  # this prints in one line
    print('{} '.format(b))              # this prints one value per line
    #a, b = b, a + b()                  # this makes two assignments on one line
                                        # a = b
                                        # b = a + b()
                                        
    # here I am doing the same, the old fashion way with  a temp var
    # the above is more efficient though, I am just playing
    temp = a
    a = b
    b += temp
    print('{}, {}, {}'.format(temp, a, b))

print() # line ending
