# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notesmain.ui'
#
# Created: Thu Aug 21 21:13:24 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from alta import  Ui_Alta
from Llistar import Ui_Llista
from Borra import Ui_Borra
import sys
import signal

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Notes(object):
    def sortir(*args):
        """Handler for the SIGINT signal."""
        #sys.stderr.write('\r')
        if QtGui.QMessageBox.question(None, '', "Segur que vols sortir ?",
                                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
                                QtGui.QMessageBox.No) == QtGui.QMessageBox.Yes:
            QtGui.QApplication.quit()
    
    def crea(* args):
        print ("creo contingut")
        Dialog = QtGui.QDialog()
        uialta = Ui_Alta()
        uialta.setupUi(Dialog)
        Dialog.exec_()
        
    def cell_was_clicked(self, row, column):
        print("Row %d and Column %d was clicked" % (row, column))
        item = self.table.itemAt(row, column)
        self.ID = item.text()
        
    def llista(* args):
        print("llista contingut")
        Dialog = QtGui.QDialog()        
        uillista = Ui_Llista()
        uillista.setupUi(Dialog)        
        Dialog.exec_()
    def borra(* args):
        print("borra contingut de la base de dades")
        Dialog = QtGui.QDialog()        
        uiborra= Ui_Borra()
        uiborra.setupUi(Dialog)        
        Dialog.exec_()
        
    def setupUi(self, Notes, app):
        Notes.setObjectName(_fromUtf8("Descompte"))
        Notes.resize(180, 300)
        Notes.setMinimumSize(QtCore.QSize(108, 247))
        Notes.setMaximumSize(QtCore.QSize(180, 300))
        self.centralwidget = QtGui.QWidget(Notes)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pB_crear = QtGui.QPushButton(self.centralwidget)
        self.pB_crear.setGeometry(QtCore.QRect(10, 20, 83, 24))
        self.pB_crear.setObjectName(_fromUtf8("pB_crear"))
        self.pB_crear.clicked.connect(self.crea)
        self.pB_llistar = QtGui.QPushButton(self.centralwidget)
        self.pB_llistar.setGeometry(QtCore.QRect(10, 70, 83, 24))
        self.pB_llistar.setObjectName(_fromUtf8("pB_llistar"))
        self.pB_llistar.clicked.connect(self.llista)
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 120, 83, 24))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.clicked.connect(self.borra)
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 170, 83, 24))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_4.clicked.connect(self.sortir)
        
        self.retranslateUi(Notes)
        QtCore.QMetaObject.connectSlotsByName(Notes)
        Notes.setTabOrder(self.pB_crear, self.pB_llistar)
        Notes.setTabOrder(self.pB_llistar, self.pushButton_3)
        Notes.setTabOrder(self.pushButton_3, self.pushButton_4)

    def retranslateUi(self, Notes):
        Notes.setWindowTitle(_translate("Descompte", "Descompte acumulat", None))
        self.pB_crear.setText(_translate("Descompte", "Afegir", None))
        self.pB_llistar.setText(_translate("Descompte", "Llistar", None))
        self.pushButton_3.setText(_translate("Descompte", "Borrar", None))
        self.pushButton_4.setText(_translate("Descompte", "Sortir", None))

