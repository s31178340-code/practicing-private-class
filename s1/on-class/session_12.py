from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout

app = QApplication()

widget = QWidget()

button = QPushButton('Click on me')
button_2 = QPushButton('Cancel')

v_l = QHBoxLayout()
v_l.addWidget(button)
v_l.addWidget(button_2)

widget.setLayout(v_l)

button_2.show()
widget.show()
app.exec()
