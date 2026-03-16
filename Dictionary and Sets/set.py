# Set
# Set is a collection which is unordered, unchangeable*, and unindexed.
# Sets are written with curly brackets.
# *Note: Set items are unchangeable, but you can remove items and add new items.
# list and dictionary are not allowed in set because they are mutable (changeable) data types
# set do not allow duplicate values

# set = {1,2,2,2,3,"Hello","World","World"}
# print(set) # print the set (duplicate values are removed)

# null_set = set() # create an empty set
# print(null_set) # print the empty set

# Set Method
# set are mutaable but their elements are immutable

# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add(2)
# collection.remove(1)
# collection.add("Hello")
# collection.add((1,2,3))
# # collection.add([1,2,3]) # list is not allowed in set because it is mutable (changeable) data type

# collection.pop() # remove a random item from the set

# print(collection) # print the set (duplicate values are removed)

# set1 ={1,2,3,4,5}

# set2 = {4,5,6,7,8}

# print(set1.union(set2)) # return a new set that contains all items from both sets, duplicates are removed

# print(set1.intersection(set2))

# Q) Store the Following Word Meaning in python diictionary:
# table : " a piece of Furniture ", "list of fact and Figure"
# cat : "A Small Animal"

# dictioanry = {
#     "table": [" a piece of Furniture ", "list of fact and Figure"],
#     "cat": ["A Small Animal"]
# }

# print(dictioanry)

# WAP to Enter marks of 3 Subject from user and store them in a dictionary. Start with an empty dictionary & add one by one 
# use subject name as a key and marks as a value. Finally print the dictionary.

# marks = {}
# subject1 = input("Enter the name of subject 1: ")
# marks1 = int(input("Enter the marks of subject 1: "))
# subject2 = input("Enter the name of subject 2: ")
# marks2 = int(input("Enter the marks of subject 2: "))
# subject3 = input("Enter the name of subject 3: ")
# marks3 = int(input("Enter the marks of subject 3: "))

# marks[subject1] = marks1
# marks[subject2] = marks2
# marks[subject3] = marks3

# # print(marks)

# marsks ={}

# sub1 = input("Enter the Sub1 Name")
# marks1 = int(input("Enter sub1 Marks"))

# sub2 = (input("Enter sub2 Marks"))
# marks2 =(input("enter marks2"))

# marsks[sub1] = marks1
# marsks[sub2] = marks2

# print(marsks)

# Figure out to store 9 & 9.0 as a seprate values in the set
# you can take the help of built in data types)

values = {
    ("float" , 9.0),
    ("int" , 9),
    (9,"9.0")
}

print(values)
