# Strings are Array
"""
like  many other popular programming languages, string in python are arrays of unicod characters.
However, Python does not have a character data type, a single character is simply a string  with a length of 1.

"""
a="Hello world"
print(a[10])

# LOOPING THROUGH A STRING
for x in "banana":
    print(x)

# String length
        #--> to get the length of a string , use 'len()' function
a="Rabin Neupane"
print(len(a))


# CHECK STRING
        # -->To check if a certain phrase or character is present in a string , we can use the leyword 'in'.
txt=" A quick brown fox jumps over the lazy dog."
if("brown" in txt):
    print("yes, 'brown is present in text'")

# check if not
        # -->To check if a certain phrase or character is not present in a string , we can use the leyword 'not in'.
        
text="A best things in life is freedom"
if("rabin" not in text):
    print("YES, the word 'rabin' is not in text")







# PYTHON-SLICING STRINGS
"""
we can return a range of a character by using the slice syntax.
specify the start index and the end index, seperated by a coloc, to return a part of the string


"""

# Get the  character from position 2 to position 5 (Not included)
n="Hello, world!"
print(n[2:6])

# slice to the end
print(n[2:])

# slice from the start
print(n[:7])


# Python-Modify strings
        # --> python has a set of built-in methods that you can usse on strings
        # --> The 'upper()' methods returns the string in upper case:
        # --> The 'lower()' methods returns the string in lower case:
a="rabin neupane"
print(a.upper())

b='RABIN NEUPANE'
print(b.lower())

# Remove whitespace
        # -->Whitespace is the space before and/or after the actual text, and very ofteen you want to remove this space.
        # --> the 'strip() methods  removes any whitespace from the beginning or the end.
m=" Hello, World!! "
print(m.strip())

# Replace string
    # --> The 'replace()' method replaces a string with another string
n='Rabin Neupane'
print(n.replace('b', 'w'))

# Split String
        # --> The split() methods returns a list where the text between the specified seperator becomes the list items
        # --> The split() methods splits the string into substrings if it finds instances of the seperator
a='Hello, World'
print(a.split(","))


# Python-String Concatenation
        # --> To concatenate, or combine, two strings you can use the + operator.
a="Hello"
b="World"
c=a+" "+b
print(c)

# Python-Format-Strings
        # --> we cannot combine strings and numbersf like below,
age=20
# This will produce an error
# txt="My name is Rabin, I am " + age
# # print(txt) 

# -->  but we can combine strings and numbers by using f-strings or format() method

# F-strings
age=20
text=f"My name is Rabin, I am {age}"
print(text)


# placeholde and modifiers
        # -->> A placeholder can contain variables, operations, functions, and modifiers to format the value.
price=1000
text=f"\nThe price is {price:.2f} dollars"
print(text)


# Python-Escape Characters
        # --> TO insert characters that are illegal in a string , use an escape character
        # --> An escape character is a backslash \ followed by the character you want to insert
        # --> An example of an illegal character is a double quote inside that is surrounded by double quotes:
# txt="We are so called "vikings" from the north."
        # --> to fix the problem, use the escape character
txt="We are so called \"vikings\" from the north."

# Eacape-Characters
# --> single quote \'
txt='it\'s all right.'
print(txt)

# --> backslash \\
txt="This will insert one \\ (backslash)"
print(txt)

# --> New line \n
txt="Hello\nWorld"
print(txt)

# -->Carriage return-->\r
txt="Rabin\rNeupane"
print(txt)
# -->Tab-->\t
txt="Hello\tWorld"
print(txt)
# --> Backspace-->\b
txt="Hello \bWorld"
print(txt)

# --> Form feed-->\f
print("This is form feed\n")
txt="Hello\fWorld"
print(txt)

# -->Octal value-->\ooo
txt="\110\145\154\154\157"
print(txt)
# -->Hex value-->\xhh
txt="\x48\x65\x6c\x6c\x6f"
print(txt)
