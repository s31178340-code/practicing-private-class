# a = 10
# b = 20
# print(a)

# a = input('Enter Youe Age: ')
# b = int(a)

# print(a, type(a))
# print(b, type(b))

# correct_password= 1234
# username= input('enter your password')
# username= int(username)
# if correct_password==username :
#     print('ok')
# else :
#     print('no')



# type_age= None
# username= input('enter your age:')
# username= int(username)
# if username<10 :
#     type_age="child"
# elif username>10 :
#     type_age='teenager'
# print(type_age)


score= 0
correct_number= 3
user= input('enter your number: ')
user= int(user)
if user==correct_number :
    score=1+score
elif user!=correct_number :
    score= score-1
print(score)