# python has the following datatypes built-in by default, in these categories
"""
-->>Text type: str
-->>Numeric Types: int, float, complex
-->>Sequence Types: list, tuple, range
-->>Mapping Type: dist
-->>Set Types: set, frozenset
-->>Boolean Type: bool
-->>Binary Types: bytes, bytearray, memoryview
-->>None type: Nonetype
"""
# Getting the data types
#  we can get the data type of any object by using the 'type() ' function:

x='10'
print(type(x))

# SETTING THE DATA TYPES
# In python , the data type is set when you assign a value to a variable:
print("\nSetting the specific data type\n")
x=str('Hello World') #str
print(x)
print(type(x))

x=int(10) #int
print(x)
print(type(x))

x=float(20.5) #float
print(x)
print(type(x))

x=complex(1j) #complex
print(x)
print(type(x))

x=list(("Apple", "Banana","Mango" ))#list 
print(x)
print(type(x))

x=tuple(("Apple", "Banana", "Cherry")) #tuple
print(x)
print(type(x))

x=range(10) #range
print(x)
print(type(x))

x={"name":"Rabin", "age":"20"} #dict
print(x)
print(type(x))
x=dict(name="Rabin", age=20)#dict
print(x)
print(type(x))

x={"Apple", "Banana","Grapes"} #set
print(x)
print(type(x))

x=frozenset({"Apple","Banana","Grapes"}) #frozenset
print(x)
print(type(x))

x=True #bool
print(x)
print(type(x))

x=bool(5) #bool
print(x)
print(type(x))

x=b"Hello" #bytes
print(x)
print(type(x))
x=bytes(5) #bytes
print(x)
print(type(x))

x=bytearray(5) #bytearray
print(x)
print(type(x))

x=memoryview(bytes(5)) #memoryview
print(x)
print(type(x))

x=None
print(x)
print(type(x))

