"""
VARIABLES ARE THE CONTAINERS FOR STORING DATA VALUES.
Python has no command for declaring a variable .
A Variable is created the moment you first assign a value to it 
"""
x=5 # x is of type int 
y="hello world!!" # y is of type str
print("Value of x:",x,"\nValue of y:",y) 

# If you want to specify the datatype  of a variable , this can be done with casting.
x=str(3) #this will be '3'
y=int(3) #this will be 3
z=float(3) #this will be 3.0

print("\n",x,"\n",y,"\n",z)

# GET THE TYPE
# You can get the datatype of a variable with the "type()" function 
a=10
b="Rabin"
print(type(a))
print(type(b))

# STRING VARIABLES CAN BE DECLARED EITHER BY USING SINGLE OF DOUBLE QUOTES.

A="Rabin"
# is the sane as
A='Rabin'

# Variables names are case-sensitive
# This will create two variables:
a=10
A="Robin"
# A will not overwrite a


"""
............PYTHON VARIABLES NAMES............
A variable can have a short name (like x and y)  or a more descriptive name( age, name, total_vloume).

"""
# RULES FOR PYTHON VARIABLES
"""
-->A variable must start with a letter or the underscore character
-->A variable cannot start with a number
-->A variable name can only contain alpha-numeric characters and underscores(A-z, 0-9,and _)
-->A variable name cannot be any of the python keywords. 
""" 

# MULTI WORDS VARIABLE NAMES
"""
Variable names with more than one word can be diffucult to read.
There are several techniques you can usse to make them more readable
    
"""
# -->Camel Case
# each word except the first , starts with a capital letter
myVariableName ="Rabin"
# --> Pascal Case
# Each word starts with a capital letter
MyVariableName="Robin"
# -->Snake Case
# Each word is seperate by a undeerscore character:
my_variable_name="Rawin"


# ASSIGN MULTIPLES VALUES
# Many values to multiple variables
# python allows you to assign values to multiple variables in one line 
x,y,z="Mango", "Orange", "Banana"
print(x)
print(y)
print(z)

# One value to multiple variables
# we can assign the same value to multiple variables in one line
x=y=z="Grapes"
print(x)
print(y)
print(z)

# UNPACK A COLLECTION
# IF you have a collection fo a values in a list, tuple etc.
# python allows you to extract the values into variables. 
# This is called unpacking
print("***********Unpacking**************")
fruits=["Apple","Banana","Mango"]
x,y,z=fruits
print(x)
print(y)
print(z)