from PySide6.QtWidgets import QPushButton, QWidget, QVBoxLayout, QApplication


a = ["c1", "c2", "c3", "c4"]

app = QApplication()
wgt = QWidget()
vl = QVBoxLayout()

for i in a:
    pb = QPushButton(i)
    vl.addWidget(pb)

wgt.setLayout(vl)

wgt.show()
app.exec()
