from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QHBoxLayout, QVBoxLayout

app = QApplication()


wgt = QWidget()

user_label = QLabel("Username")
pass_label = QLabel("Password")

user_push = QPushButton("C-1")
pass_push = QPushButton("C-2")

user_h_lay = QHBoxLayout()
pass_h_lay = QHBoxLayout()

container_v_lay = QVBoxLayout()


user_h_lay.addWidget(user_label)
user_h_lay.addWidget(user_push)

pass_h_lay.addWidget(pass_label)
pass_h_lay.addWidget(pass_push)


container_v_lay.addLayout(user_h_lay)
container_v_lay.addLayout(pass_h_lay)

wgt.setLayout(container_v_lay)

wgt.show()
app.exec()
