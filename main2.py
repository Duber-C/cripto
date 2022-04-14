
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()

    layout = QVBoxLayout()
    btn = QPushButton("Hello World!")
    label = QLabel()
    label.setText("cosas")
    text = QLineEdit()
    layout.addWidget(label)
    layout.addWidget(text)
    layout.addWidget(btn)
    w.setLayout(layout)

    w.resize(600, 400)
    w.setWindowTitle('Cripto')
    w.setWindowIcon(QtGui.QIcon('img/cripto.ico'))
    w.show()

    sys.exit(app.exec_())