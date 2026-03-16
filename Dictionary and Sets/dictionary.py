# Dictionary -- use to store data in kry value pair
# they are mutable(changable) (we can change the value of dictionary)
# they are unordered (we cannot access the element by index)
# they are defined by using curly braces {}
#they do not allow duplicate keys but they allow duplicate values

info = {
    "key" : "value",
    "name" : "Sachin",
    "age" : 12,
    "city" : "Raghunathpur",
    "is_student" : True,
    "subjects" : ["Math", "Science", "English"],
    "topics" : ("dictionary", "list", "tuple"),

}

print(info)
print(info["name"]) # access the value of key "name"
info["age"] = 13 # change the value of key "age"
print(info)
