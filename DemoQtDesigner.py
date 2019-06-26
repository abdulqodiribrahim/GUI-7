import sys

from Modul7_4 import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainForm(QDialog):
	def __init__ (self, parent = None):
		QDialog.__init__(self,parent)
		self.ui = Ui_Form()
		self.ui.setupUi(self)
		self.ui.Hello.clicked.connect(self.HalloClicked)
		
	def HalloClicked(self):
		QMessageBox.information(self,'Demo Qt Desigber', 'Hallo %s, Apa Kabar' %self.ui.lineEdit.text())
		
if __name__ == "__main__":
	a = QApplication(sys.argv)
	form = MainForm()
	form.show()
	a.exec_()



self.Register.clicked.connect(self.Registrasi1)

def Registrasi1(self):
        self.FromRegistrasi = QtWidgets.QMainWindow()
        self.form = Ui_FormRegistrasi()
        self.form.setupUi(self.FromRegistrasi)
        self.FromRegistrasi.show()


self.Registrasi.clicked.connect(self.save)

	def save(self):
		NIK = self.NIK.text()
		Nama = self.Nama.text()
		Username = self.Username.text()
		Password = self.Password.text()
		Email = self.Email.text()
		TTL = self.TTL.text()
		Alamat = self.Alamat1.text()

		insert = (NIK, Nama, Username, Password, Email, TTL, Alamat)

		if createConnection():
			sql = 'insert into costumer values ' + str(insert)
			displayData(sql)

def displayData(sqlStatement):
    print('processing query...')
    qry = QSqlQuery(db)
    qry.prepare(sqlStatement)
    qry.exec()

