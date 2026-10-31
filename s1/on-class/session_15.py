# correct_password= '1234'
# correct_username= 'ali'
# user= input('enter your password:')
# user_1= input("enter your username:")
# if user==correct_password and user_1==correct_username:
#     print('you are allowed to enter here:')
# else :
#     print('you are not allowed to enter here:')

# has_car= 'True'
# Target_city= 'arak'
# user= input('enter your target city:')
# user_1= input('do you have a personal vehicle:')
# if user==Target_city and user_1==has_car :
#     print('you can travel')
# else :
#     print('no')

# for a in[12 , 250, 1233] :
#     if a>12 :
#         print('its greater', a)

# user= input('enter your age:')
# user= int(user)
# allowed_list=[]
# banned_list=[]
# if user<=13 :
#     banned_list.append(user)
# elif user>13:
#     allowed_list.append(user)
# print(allowed_list)

# a=[42, 7, 91, 15, 63, 28, 4, 76, 33, 58, 12, 99, 21, 67, 38, 5, 84, 49, 73, 30]
# b=[]
# for c in a :
#     b.append(c*2)
# print(b)


# def multiply(a , b):
#     n= a*b
#     return n
# m= multiply(2, 3)
# d= multiply(8,9)
# print(m)
# print(d)


# def multiply(a , b):
#     n= a**b
#     return n
# m= multiply(2,3)
# d= multiply(8,2)
# print(m)
# print(d)

# import random
# print(random.randint(30,42))

# b=range(1,10)
# b=list(b)
# print(b)

# def zarb(a,b):
#     print(a**b)

# zarb(2,4)

# import random
# print(random.randint(1,100))
# c=[]
# b=range(0,10)
# for a in b:
#     y=random.randint(0,100)
#     c.append(y)

# print(c)

# import random
# def a(min , max):
#     c=random.randint(min , max)
#     if c%2==0 :
#         print("divided is avaible")
#     else:
#         print('divided isnt avaible')

# a(5,200)


# from kivy.app import runTouchApp
# from kivy.uix.button import Button
# runTouchApp(Button(text="hello"))

# from kivy.uix.button import Button
# Button= Button(text='hello')


# from kivy.uix.button import Button
# from kivy.app import runTouchApp
# runTouchApp(Button(text='hello'))

# from PySide6.QtWidgets import QApplication, QWidget,QPushButton , QHBoxLayout , QLabel

# app= QApplication()

# widget= QWidget()

# button= QPushButton("HELLO WORLD")

# lable= QLabel('username')

# v_1= QHBoxLayout()
# v_1.addWidget(button)
# v_1.addWidget(lable)

# widget.setLayout(v_1)

# widget.show()
# button.show()
# app.exec()


# from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel , QHBoxLayout, QVBoxLayout , QLineEdit , QCheckBox
# app= QApplication()

# widget= QWidget()

# button= QPushButton('pushbutton')
# button_2= QPushButton('pushbutton')

# user_lable= QLabel('username')
# pass_lable= QLabel('password')

# line_1= QLineEdit()
# line_2=QLineEdit()

# check_1= QCheckBox('دریافت کد تخفیف')
# check_2= QCheckBox('def')

# h_0= QHBoxLayout()

# h_1= QHBoxLayout()

# h_2= QHBoxLayout()

# h_3=QHBoxLayout()

# v_1= QVBoxLayout()

# h_0.addWidget(check_1)
# h_0.addWidget(check_2)

# h_1.addWidget(user_lable)
# h_1.addWidget(line_1)

# h_2.addWidget(pass_lable)
# h_2.addWidget(line_2)

# h_3.addWidget(button)
# h_3.addWidget(button_2)

# v_1.addLayout(h_1)
# v_1.addLayout(h_2)
# v_1.addLayout(h_3)
# v_1.addLayout(h_0)

# widget.setLayout(v_1)

# widget.show()
# app.exec()


# from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QCheckBox, QHBoxLayout, QVBoxLayout

# app = QApplication()

# wgt = QWidget()

# Button_1 = QPushButton('انصراف')
# Button_2 = QPushButton('خرید')

# check_1 = QCheckBox('دریافت فاکتور دیجیتال')
# check_2 = QCheckBox('استفاده از کد تخفیف')
# check_3 = QCheckBox('پذیرفتن قوانین خرید')

# H_1 = QHBoxLayout()
# H_5 = QHBoxLayout()

# H_1.addWidget(check_1)
# H_1.addWidget(check_2)
# H_1.addWidget(check_3)

# H_5.addWidget(Button_1)
# H_5.addWidget(Button_2)

# v_1 = QVBoxLayout()


# v_1.addLayout(H_1)
# v_1.addLayout(H_5)


# wgt.setLayout(v_1)

# wgt.show()
# app.exec()


# a = ["reza", 'mohamad', 'kazem', 1, 2, 4, True]
# # a[start index:end index:step]
# print(a[0:6:2])
# print(a[-1])


alis_info = {"name": "ali", "age": 23, "last_name": "hoseini", "gender": "male"}
mahnazs_info = {"name": "mahanz", "age": 20, "last_name": "jafari", "gender": "female"}

print(alis_info["last_name"])
print(mahnazs_info["age"])
alis_info["email"] = "aaa@eample.com"
print(alis_info)
