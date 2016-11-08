# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Alta.ui'
#
# Created: Mon Sep 29 10:59:11 2014
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from Nom import Ui_Nom
import sqlite3 as lite
import sys

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

class Ui_Alta(object):
    def afegir( self, camps):
        print ("afegeixo camps")
        #fallen els accents, mirar per què i com solucionar-ho
        camps = (str(self.lEdni.text()), str(self.lEnom.text()), str(self.lEcognoms.text()), str(self.lEdireccio.text()), str(self.lEpoble.text()), float(self.lEcompraactual.text()), float(self.lEcompraAcumulada.text()))
        print(camps)
        dni=self.lEdni.text()
        
        nom=self.lEnom.text()
        nom=nom.encode('utf-8')
        cognoms=self.lEcognoms.text()
        cognoms=cognoms.encode('utf-8')
        direccio=self.lEdireccio.text()
        direccio=direccio.encode('utf-8')
        poble=self.lEpoble.text()
        poble=poble.encode('utf-8')
        compraactual=self.lEcompraactual.text()
        compraactual=compraactual.encode('utf-8')
        compraAcumulada=self.lEcompraAcumulada.text()
        compraAcumulada=compraAcumulada.encode('utf-8')
        camps = ( str(dni), str(nom), str(cognoms), str(direccio), str(poble), float(compraactual), float(compraAcumulada))
        print("utf8 (bytes)'%s', '%s', '%s', '%s', '%s', %d, %d" % camps)
        camps = (str(dni), str(nom.decode('utf-8')), str(cognoms.decode('utf-8')), str(direccio.decode('utf-8')), str(poble.decode('utf-8')), float(compraactual), float(compraAcumulada))
        print("utf8 (decode) '%s', '%s', '%s', '%s', '%s', %d, %d" % camps)
        con = lite.connect('clients.db')
        with con:
            cur = con.cursor()
            #print("arriba?");
            
            #print ("abans insert = \"INSERT INTO clients  VALUES( NULL, '%s', '%s', '%s', '%s', '%s', %f, %f);" % camps)
            print(repr(camps))            
            cursor= con.cursor()
            cursor.execute("select exists(select * from clients where dni =%s)" % dni)
            result= cursor.fetchall()
            print(result)
            if(result ==[(0,)]):
            
                cur.execute("INSERT INTO clients  VALUES( (SELECT max(Id) FROM clients)+1,'%s', '%s', '%s', '%s', '%s', %f, %f);" % camps)            
                c = con.cursor()
                select_pos_score = 'SELECT * FROM clients'
                c.execute(select_pos_score)
                #for row in c:
                #    print (row)
                if cur:
                    cur.close()
            else:
                print("existeix!!")
                Dialog = QtGui.QDialog()
                uidni = Ui_Nom()
                uidni.dniUi(Dialog, self.lEdni.text())
                Dialog.exec_()
                nouvalor=uidni.canvi()
                print(nouvalor)
                
                cursor= con.cursor()
                cursor.execute("select exists(select * from clients where dni =%s)" % nouvalor)
                result= cursor.fetchall()
                print(result)
                if(result ==[(0,)]):
                    camps=(str(nouvalor), str(nom.decode('utf-8')), str(cognoms.decode('utf-8')), str(direccio.decode('utf-8')), str(poble.decode('utf-8')), float(compraactual), float(compraAcumulada))
                    print(camps)
                    cur.execute("INSERT INTO clients  VALUES( (SELECT max(Id) FROM clients)+1,'%s', '%s', '%s', '%s', '%s', %f, %f);" % camps)            
                    c = con.cursor()
                    select_pos_score = 'SELECT * FROM clients'
                    c.execute(select_pos_score)
                    for row in c:
                        print (row)
                    if cur:
                        cur.close()
                else:
                    
                    QtGui.QMessageBox.warning(None,"NO es pot afegir", "El client NO  es pot  afegir!! el dni %s ja existeix" % str(nouvalor),QtGui.QMessageBox.Ok)
                    
    def missatge(self):
        reply = QtGui.QMessageBox.question(self, 'Error en el registre',
             "Registre NO insertart", QtGui.QMessageBox.Yes)

        if (reply == QtGui.QMessageBox.Yes):
             event.accept()
    def reinicia( self ):
        self.lEdni.setText("")
        self.lEnom.setText("")
        self.lEcognoms.setText("")
        self.lEdireccio.setText("")
        self.lEpoble.setText("")
        self.lEcompraactual.setText("")
        self.lEcompraAcumulada.setText("")
    def setupUi(self, Alta):
        Alta.setObjectName(_fromUtf8("Alta"))
        Alta.resize(307, 331)
        self.lEdni = QtGui.QLineEdit(Alta)
        self.lEdni.setGeometry(QtCore.QRect(120, 10, 113, 20))
        self.lEdni.setObjectName(_fromUtf8("lEdni"))
        
        
        self.lEnom = QtGui.QLineEdit(Alta)
        self.lEnom.setGeometry(QtCore.QRect(120, 40, 113, 20))
        self.lEnom.setObjectName(_fromUtf8("lEnom"))
        self.label = QtGui.QLabel(Alta)
        self.label.setGeometry(QtCore.QRect(20, 40, 81, 16))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.lEcognoms = QtGui.QLineEdit(Alta)
        self.lEcognoms.setGeometry(QtCore.QRect(120, 70, 113, 20))
        self.lEcognoms.setObjectName(_fromUtf8("lEcognoms"))
        self.label_2 = QtGui.QLabel(Alta)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 81, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lEdireccio = QtGui.QLineEdit(Alta)
        self.lEdireccio.setGeometry(QtCore.QRect(120, 100, 113, 20))
        self.lEdireccio.setObjectName(_fromUtf8("lEdireccio"))
        self.label_3 = QtGui.QLabel(Alta)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 81, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lEpoble = QtGui.QLineEdit(Alta)
        self.lEpoble.setGeometry(QtCore.QRect(120, 130, 113, 20))
        self.lEpoble.setObjectName(_fromUtf8("lEpoble"))
        self.label_4 = QtGui.QLabel(Alta)
        self.label_4.setGeometry(QtCore.QRect(20, 130, 81, 16))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lEcompraactual = QtGui.QLineEdit(Alta)
        self.lEcompraactual.setGeometry(QtCore.QRect(120, 160, 113, 20))
        self.lEcompraactual.setObjectName(_fromUtf8("lEcompraactual"))
        self.label_5 = QtGui.QLabel(Alta)
        self.label_5.setGeometry(QtCore.QRect(0, 160, 101, 20))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lEcompraAcumulada = QtGui.QLineEdit(Alta)
        self.lEcompraAcumulada.setGeometry(QtCore.QRect(120, 190, 113, 20))
        self.lEcompraAcumulada.setObjectName(_fromUtf8("lEcompraAcumulada"))
        self.label_6 = QtGui.QLabel(Alta)
        self.label_6.setGeometry(QtCore.QRect(20, 190, 81, 16))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.pB_afegir = QtGui.QPushButton(Alta)
        self.pB_afegir.setGeometry(QtCore.QRect(110, 220, 161, 51))
        self.pB_afegir.setObjectName(_fromUtf8("pB_afegir"))
        #afegeixo
        self.pB_afegir.clicked.connect(self.afegir) #afegeixo
        self.pB_afegir.clicked.connect(Alta.reject) #i tanco per obligar a refrescar
        #fi afegir
        self.pB_inicial = QtGui.QPushButton(Alta)
        self.pB_inicial.setGeometry(QtCore.QRect(120, 280, 121, 24))
        self.pB_inicial.setObjectName(_fromUtf8("pB_inicial"))
        #reinici de camps
        self.pB_inicial.clicked.connect(self.reinicia)
        #fi reinici
        self.pB_tancar = QtGui.QPushButton(Alta)
        self.pB_tancar.setGeometry(QtCore.QRect(20, 220, 83, 61))
        self.pB_tancar.setObjectName(_fromUtf8("pB_tancar"))
        #tancar
        self.pB_tancar.clicked.connect(Alta.reject) #l'event de tancar, ha d'anar a la finestra!
        #fi tancar
        
        self.label_7 = QtGui.QLabel(Alta)
        self.label_7.setGeometry(QtCore.QRect(20, 10, 81, 16))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))

        self.retranslateUi(Alta)
        QtCore.QMetaObject.connectSlotsByName(Alta)

    def retranslateUi(self, Alta):
        Alta.setWindowTitle(_translate("Alta", "Dialog", None))
        self.label.setText(_translate("Alta", "Nom", None))
        self.label_2.setText(_translate("Alta", "Cognoms", None))
        self.label_3.setText(_translate("Alta", "Direcció", None))
        self.label_4.setText(_translate("Alta", "Poble", None))
        self.label_5.setText(_translate("Alta", "Compra actual", None))
        self.label_6.setText(_translate("Alta", "Acumulat", None))
        self.pB_afegir.setText(_translate("Alta", "Afegir", None))
        self.pB_inicial.setText(_translate("Alta", "Reiniciar camps", None))
        self.pB_tancar.setText(_translate("Alta", "Tornar", None))
        self.label_7.setText(_translate("Alta", "DNI", None))

