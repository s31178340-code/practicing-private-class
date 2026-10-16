from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QHBoxLayout, QVBoxLayout, QLineEdit

app = QApplication()


wgt = QWidget()

user_label = QLabel("Username")
pass_label = QLabel("Password")

username_le = QLineEdit()
password_le = QLineEdit()

user_h_lay = QHBoxLayout()
pass_h_lay = QHBoxLayout()

container_v_lay = QHBoxLayout()


user_h_lay.addWidget(user_label)
user_h_lay.addWidget(username_le)

pass_h_lay.addWidget(pass_label)
pass_h_lay.addWidget(password_le)


container_v_lay.addLayout(user_h_lay)
container_v_lay.addLayout(pass_h_lay)

wgt.setLayout(container_v_lay)

wgt.show()
app.exec()
