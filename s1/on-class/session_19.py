from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QLineEdit, QCheckBox
app = QApplication()

widget = QWidget()

button = QPushButton('Create')

user_lable = QLabel('Name')
line_1 = QLineEdit()

h_3 = QHBoxLayout()
v_1 = QVBoxLayout()

h_3.addWidget(user_lable)
h_3.addWidget(line_1)

v_1.addLayout(h_3)
v_1.addWidget(button)

widget.setLayout(v_1)


def aaa():
    line_value = line_1.text()
    print(line_value)


button.clicked.connect(aaa)

widget.show()
app.exec()
