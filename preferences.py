from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *


class Preferences(QDialog):

    checkBoxSig = Signal(bool)

    def __init__(self, parent=None, showToolbar=True):
        super(Preferences, self).__init__(parent)

        self.resize(200, 100)
        self.setWindowTitle("Preferences")

        self.checkBox = QCheckBox("Show main toolbar")
        self.checkBox.setChecked(showToolbar)
        closeBtn = QPushButton("close")

        layout = QVBoxLayout()
        layout.addWidget(self.checkBox)
        layout.addWidget(closeBtn)

        self.setLayout(layout)

        closeBtn.clicked.connect(self.close)
        self.checkBox.stateChanged.connect(self.checkBoxStateChanged)

    def checkBoxStateChanged(self):
        self.checkBoxSig.emit(self.checkBox.isChecked())
