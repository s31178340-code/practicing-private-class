
# First_person_info= {'Name':'Mohamad_Ali','Age':19 ,'Number':+989944334194, 'Domicile':'Arak'}
# a=First_person_info['Name']
# b=First_person_info['Number']
# c=First_person_info['Domicile']
# print(c)






# from PySide6.QtWidgets import QApplication , QWidget , QPushButton , QVBoxLayout
# a=['C0','C1' 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10']
# App=QApplication()
# wgt=QWidget()
# v_1=QVBoxLayout()

# for i in a:
#     button=QPushButton(i)
#     v_1.addWidget(button)

# wgt.setLayout(v_1)

# wgt.show()
# App.exec()



# from PySide6.QtWidgets import QApplication , QWidget , QLabel , QCheckBox , QLineEdit , QRadioButton , QTextEdit , QHBoxLayout , QVBoxLayout , QPushButton
# app= QApplication()
# wgt= QWidget()
# Lable_1= QLabel('First Name')
# Lable_2= QLabel('Last name')
# Lable_3=QLabel('Gender')
# Lable_4=QLabel('Bio')
# Check_1=QCheckBox('قبول قوانین')
# Check_2=QCheckBox('دریافت نوتیف')
# Radio_1=QRadioButton('Male')
# Radio_2=QRadioButton('Female')
# Line_1=QLineEdit()
# Line_2=QLineEdit()
# Text=QTextEdit()
# Button_1=QPushButton('Create')
# Button_2=QPushButton('Cancel')
# H_1=QHBoxLayout()
# H_2=QHBoxLayout()
# H_3=QHBoxLayout()
# H_4=QHBoxLayout()
# H_5=QHBoxLayout()
# v_0=QVBoxLayout()
# V_1=QVBoxLayout()
# H_1.addWidget(Lable_1)
# H_1.addWidget(Line_1)
# H_2.addWidget(Lable_2)
# H_2.addWidget(Line_2)
# H_3.addWidget(Check_1)
# H_3.addWidget(Check_2)
# H_4.addWidget(Lable_3)
# H_4.addWidget(Radio_1)
# H_4.addWidget(Radio_2)
# H_5.addWidget(Button_1)
# H_5.addWidget(Button_2)
# v_0.addWidget(Lable_4)
# v_0.addWidget(Text)
# V_1.addLayout(H_1)
# V_1.addLayout(H_2)
# V_1.addLayout(H_3)
# V_1.addLayout(H_4)
# V_1.addLayout(v_0)
# V_1.addLayout(H_5)
# wgt.setLayout(V_1)
# wgt.show()
# app.exec()