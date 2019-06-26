# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Modul7_4.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(726, 269)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(150, 40, 271, 16))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(150, 70, 431, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.Exit = QtWidgets.QPushButton(Form)
        self.Exit.setGeometry(QtCore.QRect(310, 200, 93, 28))
        self.Exit.setObjectName("Exit")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(260, 100, 195, 30))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Hello = QtWidgets.QPushButton(self.widget)
        self.Hello.setObjectName("Hello")
        self.horizontalLayout.addWidget(self.Hello)
        self.Clear = QtWidgets.QPushButton(self.widget)
        self.Clear.setObjectName("Clear")
        self.horizontalLayout.addWidget(self.Clear)

        self.retranslateUi(Form)
        self.Exit.clicked.connect(Form.close)
        self.Clear.clicked.connect(self.lineEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Cplain Teks memasukkan Teks"))
        self.Exit.setText(_translate("Form", "Exit"))
        self.Hello.setText(_translate("Form", "Hello"))
        self.Clear.setText(_translate("Form", "Clear"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
