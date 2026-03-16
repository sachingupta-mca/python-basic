# tuples
# tuples are immutable(not changeable) sequences, typically used to store collections of heterogeneous data
# tuples are defined by using parentheses ()
# tuples are just like strings 
# tuples are ordered (we can access the element by index)

# WAP to input 5 No. from user and store in a tuple and print the tuple
# num1 = int(input("Enter 1st No. :"))
# num2 = int(input("Enter 2nd No. :"))
# num3 = int(input("Enter 3rd No. :"))
# num4 = int(input("Enter 4th No. :"))
# num5 = int(input("Enter 5th No. :"))

# num_tuple = (num1, num2, num3, num4, num5)
# print(num_tuple)
# print(type(num_tuple))
# print(num_tuple[0]) # access the 1st element of tuple
# print(num_tuple[1]) # access the 2nd element of tuple

# tup = ()
# print(tup)
# print(type(tup))

# a = (1, 2, 3, 4, 5)
# print(a)
# print(a[::-1])
# print("Index of 3:", a.index(3)) # find the index of 1st occurance of 3
# print("Count of 2:", a.count(2)) # count the occurance of 2 in the tuple

#WAP to check if a list cointain palidrome of elements or not
# Palidrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward
# b = [1,2,3,2,1]
# a = ("madam", "hello", "level", "world", "radar")
# for i in a:
#     if i == i[::-1]:
#         print(i, "is a palindrome")
#     else:
#         print(i, "is not a palindrome")

list1 = [1,2,1]
list2 = [1,2,3]

copy_list1 = list1.copy() 
copy_list1.reverse()
if copy_list1 == list1:
    print("list1 is a palindrome")
else:
    print("list1 is not a palindrome")
