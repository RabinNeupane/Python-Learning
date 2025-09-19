mylist=["apple",'banana','cherry']
print(mylist[0])
print(len(mylist))

# list items- data types
    # --> Lists item can be of any data types:
    # --> Also, list can contain different data types
list1=['apple','banana', 'mango','cherry']
list2=[1,2,3,4,5,6,7,8,9]
list3=[True,False,True,True]
print(list1)
print(list2)
print(list3)

list4=['abc',12,True,40,'male']
print(list4)
print(type(list4))

thislist=list(('apple','banana','mango'))
print(thislist)


# Negative indexing
        # --> Negative indexing means start from the end
        # --> -1 refers to the last item, -2 refers to the second last etc.


mylist=['apple','grapes','banana', 'mango']
print(mylist[-1])


# Range  of indexes
list=['apple','banana','cherry','orange','kiwi','melon','mango']
print(list[2:5])

# check if item exists
        # --> to determine if a specified item is present in a list use the keyword 'in'.
if 'apple' in list:
    print("Yes, 'apple' is in the fruit list")

# Change list items
thislist=['apple','banana','cherry']
thislist[1]='blackcurrant'
print(thislist)

# change a range of item values

thislist=['apple','banana','cherry','orange','kiwi','mango']
thislist[1:3]=['blackcurrant','watermelon']
print(thislist)

# if we insert more items than we replace, the new items will be inserted where you specified,
#  and the remaining items will move accordingly
# ----> change the second value by replacing it with two new values:
mylist=['apple','banana','cherry']
mylist[1:2]=['blackcurrant','watermelon']
print(mylist)


# Insert items
        # --> to insert a new list iten, without replacing any of the existing values ,
        #  we can use the 'insert()' method.
#  insert 'watermelon' as the third item:
list=['apple','banana','cherry']
list.insert(2,'watermelon')
print(list)


# Python- Add list items
        # --> To add an item to the end of the list, use the append() method
        # --> To insert a list item at a specified index, use the insert() method

# append() method
list=['apple','banana','cherry']
list.append('orange')
print(list)

# insert() method
list=['apple','banana','grapes']
list.insert(2,'watermelon')
print(list)


# Extend list
        # --> To append elements from another list to the current list, use the extend() method
thislist=['apple', 'banana', 'cherry']
tropical=['mango','pineapple','papaya']
thislist.extend(tropical)
print(thislist)



# Python-remove list items

# To remove specified item
        # --> The remove() method removes the specified item,

list=['apple','banana','grapes','orange']
list.remove('banana')
print(list)

# If there are more rhan one item with specified value, the remove() method removes the first occurrence

list=['apple','banana','grapes','banana','cherry']
list.remove('banana')
print(list)

# Removed Specified Index
        # --> the pop() method removes the speccified index.
list=['apple','banana','grapes','banana','cherry']
list.pop(1)
print(list)

#  if we donot specify the index, the pop() method removes the last item.
list=['apple','banana','grapes','banana','cherry']
list.pop()
print(list)


# The del keyword also removes the specified index:

list=['apple','banana','grapes','orange']
del list[1]
print(list)

# The del keyword can also delete the list completely.

thislist1=['apple','banana','cherry']
del thislist1

# Clear the lists
        # --> the clear() method empties the list
        # --> the list still remain but it has no content
lista=['apple','banana','cherry']
lista.clear()
print(lista)

#python-loop lists 

# Loop through a list
                # --> we can loop through the list items by using a for loop:
list=['apple','banana','grapes','cherry']
for x in list:
    print(x)
# Loop through the index Numbers
                # --> we can also loop through the list items by referring to their index number.
                # -->use the range() and len() function to create a suitable iterable

list=['apple','banana','grapes','cherry','mango']
for i in range(len(list)):
    print(list[i])


# Using a while loop
                # --> use the len function to determine the length of the list,
                #  then start at 0 and loop your way through the list items by referring to their indexes.

thislist=['apple','banana','grapes','mango']
i=0
while i<len(thislist):
    print(thislist[i])
    i=i+1


#  list Comprehension
                # --> list comprehension offers the shortest syntax for looping through lists:

list=["WATERMELON",'apple','banana','grapes','mango']
[print(x) for x in list]


# Python-list comprehension
        # --> list comprehension offers a shorter syntax when you want to create 
        # a new list based on the values of an existing list.

fruits=['apple','banana','cherry','kiwi','mango']
newlist=[]
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)


#  using list comprehension we can do all that with only one line of code:
fruits=['apple','banana','cherry','kiwi','mango']
newlist=[x for x in fruits if 'a' in x]
print(newlist)
