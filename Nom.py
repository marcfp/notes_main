# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Nom.ui'
#
# Created: Sat Sep 20 19:03:07 2014
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Nom(object):
    
    
    @QtCore.pyqtSlot('QTableWidgetItem')#str)
    def canvi(self):     
        #print("faig el canvi a la base de dades")      
        #print("valor a actualitzar =",self.textEdit.toPlainText())        
        return(self.textEdit.toPlainText())
    def sortir(self):
        """Handler for the SIGINT signal."""
        #sys.stderr.write('\r')
        #if QtGui.QMessageBox.question(None, '', "Segur que vols sortir ?",
        #                        QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
        #                        QtGui.QMessageBox.No) == QtGui.QMessageBox.Yes:
        #reject
        self.Dialog.reject
            

      
        
    def setupUi(self, Dialog, valor, col, row, llista):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(479, 125)
        self.pB_cancela = QtGui.QPushButton(Dialog)
        self.pB_cancela.setGeometry(QtCore.QRect(130, 80, 83, 24))
        self.pB_cancela.setObjectName(_fromUtf8("pB_cancela"))
        self.pB_cancela.clicked.connect(Dialog.reject)#self.sortir) #Dialog.reject)
        self.pB_accepta = QtGui.QPushButton(Dialog)
        self.pB_accepta.setGeometry(QtCore.QRect(230, 80, 83, 24))
        self.pB_accepta.setObjectName(_fromUtf8("pB_accepta"))
        
        
        self.pB_accepta.clicked.connect(self.canvi)
        self.pB_accepta.clicked.connect(Dialog.reject)
        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(160, 30, 281, 31))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.textEdit.setText(valor.text())
        #print("col = ",type(col),int(col)," i row =",type(row),int(row)," self.textEdit.toPlainText() =",self.textEdit.toPlainText())       
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 30, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def dniUi(self, Dialog, valor):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(479, 125)
        self.pB_cancela = QtGui.QPushButton(Dialog)
        self.pB_cancela.setGeometry(QtCore.QRect(130, 80, 83, 24))
        self.pB_cancela.setObjectName(_fromUtf8("pB_cancela"))
        self.pB_cancela.clicked.connect(Dialog.reject)#self.sortir) #Dialog.reject)
        self.pB_accepta = QtGui.QPushButton(Dialog)
        self.pB_accepta.setGeometry(QtCore.QRect(230, 80, 83, 24))
        self.pB_accepta.setObjectName(_fromUtf8("pB_accepta"))
        
        
        self.pB_accepta.clicked.connect(self.canvi)
        self.pB_accepta.clicked.connect(Dialog.reject)
        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(160, 30, 281, 31))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.textEdit.setText(valor)
        #print("col = ",type(col),int(col)," i row =",type(row),int(row)," self.textEdit.toPlainText() =",self.textEdit.toPlainText())       
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 30, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Canvi de valor", None))
        self.pB_cancela.setText(_translate("Dialog", "Cancel·la", None))
        self.pB_accepta.setText(_translate("Dialog", "Accepta", None))
        self.label.setText(_translate("Dialog", "Valor a canviar", None))

