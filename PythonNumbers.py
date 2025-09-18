"""
There are three numeric types in python:
-->int
-->float
-->complex
VARIABLES OF NUMERIC TYPES ARE CREATED WHEN YOU ASSIGN A VALUE TO THEM:
"""
X=1
X=2.896
X=1j


#--> int
        #--> int or integer, is a whole number, positive or negative , without decimal , of unlimited length.
x=1
x=2312323432542342422357285
z=-23423423 

#-->float
        #--> float, or "floating point number" ia a number , positive or negative, containing one or more decimals.
x=1.20
x=2.0
x=-23.43453 
            #--> float can also be scientific numbeers with an "e" to indicate the power of 10.
x=35e4
y=15E4
z=-34.7e12

#-->complex
        #--> complex number are written with a "j" as the imaginary part:
x=3+5j
y=2j
z=-3j


# TYPE CONVERSION
        # --> We can convert from one type to another  with the int(), float, and complex() methods
x=5
y=2.4
z=1j

#convert from int to float
a=float(x)
print(a)
print(type(a))

#convert from float to int
b=int(y)
print(b)
print(type(b))

#convert from int to complex
c=complex(x)
print(c)
print(type(c))

# WE CANNOT CONVERT COMPLEX NUMBERS INTO ANOTHER NUMBER TYPE.

#@@@@@@@@@@@@@@@@@ RANDOM NUMBER  @@@@@@@@@@@@@@@@
"""
PYTHON doesnot have a 'random()' function to make a random number, but python has a 
built in nodule called  'random' that can be used to make a random numbers:

"""

import random
print(random.randrange(1,20))



