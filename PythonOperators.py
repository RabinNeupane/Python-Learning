# Operators are used to perform operations on variables and values
"""
Python provides the operators in the following group:
-->Arithmetic operator
    -->Arithmetic operators are used with numeric 
    values to perform common mathematical operation
    (+,-,*,/,%,**,//)
"""
# Exponentiation
x=2
y=3
print(x**y)

# The floor division // rounds the result down to the nearest whole number
x=14
y=2
print(x//y)


"""
-->Assignment operator
    -->Assignment operator are used to assign the value to the variables:
    (=,+=,-=,*=,/=,%=,//=,**=,&=,|=,^=,>>=,<<=,:=)
"""
# --> &= bitwise AND
x=7
x&=3
print(x)

# --> |= bitwise OR
x=7
x|=3
print(x)

# --> ^= bitwise XOR(exclusive OR): 1^0=1, 1^1=0

x=3
x^=2
print(x)

# --> >>=  right shift( Effectively divides the number by 2^3=8)
x=40  #101000
x>>=3 #000101
print(x)

# --> <<= left shift (( Effectively multiplies the number by 2^3=8))

"""
-->Comparison operator
    --> Comparision operator are used to compare two values:
    (==,!=,>,<,>=,<=)
"""

"""
-->Logical operator
    --> Logical operators are used to combine conditional statements
    (and, or, not)

"""
# --> and
x=5
print( x>3 and x<10)
# returns True because 5 is greater than 3 AND 5 is less than 10

# --> or
x=5
print(x>3 or x<4)
# returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)

# --> not
x=5
print(not(x>3 and x<10))
# returns False because not is used to reverse the result


"""
-->Identity operator
    --> Identity operator are used to compare the objects , not if they are equal,
        but if they are actually the same object, with the same memory location
        (is, is not)
"""

# --> is
        #Returns true if both variables are the same objects
x=["apple", "banana"]
y=["apple", "banana"]
z=x
print(x is z)
# returns TRUE because z is the same object as x
print(x is y)
#  returns FALSE because x is not the same object as y, even if they have the same content

print(x==y)
# to demonstrate the difference between " is " and "==": 
    #  this comparision returns TRUE because x is equal to y.
"""
-->Membership operator
    --> Membership operators are used to test if a sequencw is presented in an object
    (in , not in)
"""
# --> in
        # --> Returns true if a sequence with the specified value is present in the object
x=["apple", 'banana']
print("banana" in x)   
    # Returns true because a sequence with the value " banana" is in the list

# --> not in 
        # --> Returns true if a sequence with the specified value is not present in the object
print("pineapple" not in x)
"""
-->Bitwise operator 
    --> Bitwise operator are used to compare(binary) numbers:
    (AND&,OR|,XOR^,NOT~,ZERO fill left shift[<<],signed right shift>>)

"""

# OPERATOR PRECEDENCE
    # --> operator precedence describes the order in which operations are performed