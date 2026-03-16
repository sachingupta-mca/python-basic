# Dictionary -- use to store data in kry value pair
# they are mutable(changable) (we can change the value of dictionary)
# they are unordered (we cannot access the element by index)
# they are defined by using curly braces {}
#they do not allow duplicate keys but they allow duplicate values

# info = {
#     "key" : "value",
#     "name" : "Sachin",
#     "age" : 12,
#     "city" : "Raghunathpur",
#     "is_student" : True,
#     "subjects" : ["Math", "Science", "English"],
#     "topics" : ("dictionary", "list", "tuple"),

# }

# print(info)
# print(info["name"]) # access the value of key "name"
# info["age"] = 13 # change the value of key "age"
# print(info)

# Nested Dictionary

student = {
    "name" : "Sachin",
    "age" : 12,
    "city" : "Raghunathpur",
    "is_student" : True,
    "subjects" : ["Math", "Science", "English"],
    "topics" : ("dictionary", "list", "tuple"),
    "marks" : {
        "Math" : 90,
        "Science" : 85,
        "English" : 95
    }
}

# print(student)
# print(student["name"])
# print(student["marks"]["Math"]) # access the value of key "Math" in nested dictionary "marks"

# print(student.keys()) # print all the keys of dictionary
# print(student.values()) # print all the values of dictionary
# print(student.items()) # print all the key value pairs of dictionary
# print(student.get("name")) # access the value of key "name" using get() method
# print(list(student.items())) # print all the key value pairs of dictionary in list format

print(student["name"]) # access the value of key "name" using square brackets []
print(student.get("name")) # best method

