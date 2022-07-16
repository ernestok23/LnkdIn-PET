#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 0x0a
y = 0x02
z = x & y

print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')
#%%
x = 0x0a
y = 0x02
z = x & y

print(f'AND (hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')
print(f'AND (bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')
#%%
x = 0x0a
y = 0x02
z = x | y

print(f'OR (hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')
print(f'OR (bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')

#%%
x = 0x0a
y = 0x05
z = x | y

print(f'OR (hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')
print(f'OR (bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')

#%%
# XOR : one or the other
x = 0x0a
y = 0x02
z = x ^ y

print(f'XOR (hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')
print(f'XOR (bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')
#%%
x = 0x0a
y = 0x0a
# XOR : one or the other
z = x ^ y     # bin will be all 0s

print(f'XOR (hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')
print(f'XOR (bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')

#%%
x = 0x0a
y = 0x05
# XOR : one or the other
z = x ^ y     # bin will be all 1s

print(f'XOR (hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')
print(f'XOR (bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')
#%%
x = 0x0a
y = 0x0f

# XOR : one or the other.
# with y set to 0x0f, this becomes an effective way of flipping the bits of x
z = x ^ y     # it will flip the bits of x

print(f'XOR (hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')
print(f'XOR (bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')

#%%
x = 0x0a
y = 0x01        
w = 0x03

# << shift left bitwise. you can shift 1+ positions

z = x << y     # shift the bits 1 position to the left
t = x << w     # shift the bits 3 positions to the left


print(f'XOR (hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')
print(f'XOR (bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')
print()
print(f'XOR (hex) x is {x:02x}, w is {w:02x}, t is {t:02x}')
print(f'XOR (bin) x is {x:08b}, w is {w:08b}, t is {t:08b}')
#%%
x = 0x0a
y = 0x01        
w = 0x03

# >> shift right bitwise. you can shift 1+ positions

z = x >> y     # shift the bits 1 position to the left
t = x >> w     # shift the bits 3 positions to the left


print(f'XOR (hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')
print(f'XOR (bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')
print()
print(f'XOR (hex) x is {x:02x}, w is {w:02x}, t is {t:02x}')
print(f'XOR (bin) x is {x:08b}, w is {w:08b}, t is {t:08b}')







