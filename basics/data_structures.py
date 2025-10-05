#Lists and Tuples

"""
LISTS
Lists are flexible and dynamic. They are ordered mutable set of items.
"""

#syntax for Lists
#<variable_name> = []

Students = ["Alice", "Bob", "Charlie", "Dan"]
print (Students)
#Indexing is the unique id assigned to each element in a list in python. the Index always starts with 0.
# Ex: ["Alice", "Bob", "Charlie", "Dan"]
#index [  0,     1    ,   2     ,    3 ]
print(Students[0])
print(Students[-2])
print(Students[1])

#how to slice a list. slicing always works with the "n-1" formula. 
# so when slicing, the last index will not be automatically printed. 

print(Students[0:2])
print(Students[-3:-1])
print(Students[-2:])
print(Students[1:])

#How to add to the list. Append takes in only one argument at a time
Students.append("Eve",)
print(Students)

#How to remove from the list. this can be done in two ways.
#first with "Remove"
#the second with "Pop". when pop is used, if no name inside the list is mentioned, it will simply delete the last value in the list.
Students.remove("Bob")
print(Students)

Students.pop()
print(Students)

#how to sort a list
scores = [98, 97, 69, 87, 56, 75, 97, 66]
scores.sort()
print(scores)
scores.reverse()
print(scores)

"""
TUPLES
Tuples are fixed and reliable. They cannot be modified or changed.
"""
#Syntax for tuple
# some_tuple = ()

some_tuple = (1,2,3,4,5,6)
print(some_tuple[1:])