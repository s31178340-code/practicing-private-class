# users = ["ali", "javad", "hosein"]
# while True:
#     actions = input("enter your action :")

#     if actions == "exit":
#         exit()
#     if actions == "show_users":
#         print(users)
#     else:
#         print("Your action doesn't exist")


# a = 10
# a = a-1
# a -= 1
# a += 1
# a *= 2

# print(a)

name = "mahdi"
age = 20

# print(name, "age is :", age)
sentence = name + "is" + str(age)
print(sentence)
# ---------------------------------------------------
"f_string"
"format"
sentence_f_string = f"{name} is {age}"
print(sentence_f_string)


name = "javad"
age = 13
city = "tehran"

# javd is 13 and he is from tehran

# --------------------------------------------------------------------
# dictionary
# --------------------------------------------------------------------
age_ali = 23
number_ali = 918777
city_ali = "Tehran"

age_maryam = 14
number_maryam = 918999
city_maryam = "Shiraz"

alis_info = {"age": 23, "number": 918555, "city": "Tehran"}

# Get Value
print(alis_info["age"])
city_ali = alis_info["city"]

# Add New Value
alis_info["Country"] = "Iran"
print(alis_info)
