# age = int(input("Enter your Age :")) 
# if (age>=18):
#     print("You are Adult")
# else:
#     print("You Are not Adult")

#Elif Statement
# marks = int (input("Enter Your Marks :"))
# if (marks>=90):
#     print("Grade A")
# elif (marks>=80):
#     print("Grade B")
# elif (marks>=60):
#     print("Grade C")
# else:
#     print("Fail")

# in elif we check if first condition beacame False
# nesting is valid in python

# age = int (input("Enter your Age :"))
# if (age >=18):
#     print("Eligible For Drive")
#     if (age >=80):
#         print ("You are too Old to Drive")
#     else:
#         print("You can Drive")

# else:
#     print("Not Eligible for Driving")

#WAP to Check a No. entered is Even or ODD

# num =  int (input("Enter a No. :"))
# if (num %2 == 0):
#     print ("Even No")

# else:
#     print("ODD No.")

# WAP to check a No. is Positive or Negative or Zero

# num = int(input("Enter a No. :"))
# if (num > 0):
#     print("Positive No.")
# elif (num < 0):
#     print("Negative No.")
# else:
#     print("Zero")

# WAP to find the Largest among 3 No.

# num1 = int(input("Enter 1st No."))
# num2 = int(input("Enter 2nd No."))
# num3 = int(input("Enter 3rd No."))

# if (num1>num2) and (num1>num3):
#     print("Largest No. is ",num1)
# elif (num2>num1) and (num2>num3):
#     print("Largest No. is ",num2)
# else:    print("Largest No. is ",num3)

#WAP to check a No. is Multiple of 7 or nOt

num = int (input("Enter the No. to check the Multiple of 7 :"))
if (num%7 == 0):
    print(num, "is multiple of 7")
else:
    print(num, "is not multiple of 7")