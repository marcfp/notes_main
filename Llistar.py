# -*- coding: utf-8 -*-
 
# Form implementation generated from reading ui file 'Llistar.ui'
#
# Created: Tue Sep  2 19:13:26 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

 
from PyQt4 import QtCore, QtGui, QtSql
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


class Ui_Llista(QtGui.QWidget):
   
    def __init__(self):
        QtGui.QWidget.__init__(self)
        #self.setWindowTitle("QTableWidget Cell Click")
        #self.setRowCount(3)
        #self.setColumnCount(3)
    
    #@QtCore.pyqtSlot(int, int) # prevents executing following function twice http://stackoverflow.com/questions/16367090/python-pyqt-qtablewidget-get-cell-value-based-on-header-string-and-selected-r
    #def cell_was_clicked(self, item, item2):        
        #row=str(item)        
        #print("row=",row)       
        #col=str(item2)
        #print("col=",col)
        #QtGui.QMessageBox.information(self,"QTableWidget Cell Click",	"Row: "+row+" | Column: "+col) #mostra informació
       
    def llista( self): #these sources shows values from sqlite into python prompt
        #print ("Llisto camps")        
        con = lite.connect('clients.db')
        with con:
            cur = con.cursor()
            #print("arriba?");                
            select_pos_score = 'SELECT * FROM clients'
            cur.execute(select_pos_score)            
            for (Id, Dni, Nom, Cognoms, Direccio, Poble, Compra_actual, Acumulat) in cur.fetchall():
                print (Id, Dni, Nom, Cognoms, Direccio, Poble, Compra_actual, Acumulat)           
            if cur:
                cur.close()    

    def cellchanged(self):
        #print("cell changed")
        col = self.Llistat.currentColumn()
        #print("columna = ",col)
        row = self.Llistat.currentRow()
        #print("fila = ",row)        
        valor = self.Llistat.item(row,col)
        #print("valor = ",valor.text())
        #print ("creo finestra Nom")
        Dialog = QtGui.QDialog()
        if(col==1):
            uidni = Ui_Nom()
            uidni.setupUi(Dialog, self.Llistat.item(row,col), col, row, self.Llistat)
            Dialog.exec_()
            nouvalor=uidni.canvi()
            identificador=self.Llistat.item(row,0)
            self.Llistat.setItem(row,1,QtGui.QTableWidgetItem(nouvalor))
            con = lite.connect('clients.db')
            with con:
                cur = con.cursor()
                #print("arriba update?");
                
                
                select_update="update clients set dni='{0}' where id='{1}'".format(nouvalor,identificador.text()) 
                #print(select_update)                
                cur.execute(select_update)
        if(col==2):
            uinom = Ui_Nom()
            uinom.setupUi(Dialog, self.Llistat.item(row,col), col, row, self.Llistat)
            Dialog.exec_()
            nouvalor=uinom.canvi()
            identificador=self.Llistat.item(row,0)
            
            #print("identificador =",identificador.text())                
            #print("update clients set nom='{0}' where id='{1}'".format(nouvalor,identificador.text()))
            
            self.Llistat.setItem(row,2,QtGui.QTableWidgetItem(nouvalor))
            con = lite.connect('clients.db')
            with con:
                cur = con.cursor()
                #print("arriba update?");
                
                
                select_update="update clients set nom='{0}' where id='{1}'".format(nouvalor,identificador.text()) 
                #print(select_update)                
                cur.execute(select_update)
        if(col==3):
            uicognom = Ui_Nom()
            uicognom.setupUi(Dialog, self.Llistat.item(row,col), col, row, self.Llistat)
            Dialog.exec_()
            nouvalor=uicognom.canvi()
            identificador=self.Llistat.item(row,0)
            #print("identificador =",identificador.text())
            self.Llistat.setItem(row,3,QtGui.QTableWidgetItem(nouvalor))
            #print("update clients set cognoms='{0}' where id='{1}'".format(nouvalor,identificador.text()))
            con = lite.connect('clients.db')
            with con:
                cur = con.cursor()
                #print("arriba update?");
                
                
                select_update="update clients set cognoms='{0}' where id='{1}'".format(nouvalor,identificador.text()) 
                #print(select_update)                
                cur.execute(select_update)
        if(col==4):
            uidireccio = Ui_Nom()
            uidireccio.setupUi(Dialog, self.Llistat.item(row,col), col, row, self.Llistat)
            Dialog.exec_()
            nouvalor=uidireccio.canvi()
            identificador=self.Llistat.item(row,0)
            #print("identificador =",identificador.text())
            self.Llistat.setItem(row,4,QtGui.QTableWidgetItem(nouvalor))
            #print("update clients set direccio='{0}' where id='{1}'".format(nouvalor,identificador.text()))
            con = lite.connect('clients.db')
            with con:
                cur = con.cursor()
                #print("arriba update?");
                
                
                select_update="update clients set direccio='{0}' where id='{1}'".format(nouvalor,identificador.text()) 
                #print(select_update)                
                cur.execute(select_update)
        if(col==5):
            uipoble = Ui_Nom()
            uipoble.setupUi(Dialog, self.Llistat.item(row,col), col, row, self.Llistat)
            Dialog.exec_()
            nouvalor=uipoble.canvi()
            identificador=self.Llistat.item(row,0)
            #print("identificador =",identificador.text())
            self.Llistat.setItem(row,5,QtGui.QTableWidgetItem(nouvalor))
            #print("update clients set Poble='{0}' where id='{1}'".format(nouvalor,identificador.text()))
            con = lite.connect('clients.db')
            with con:
                cur = con.cursor()
                #print("arriba update?");
                
                
                select_update="update clients set Poble='{0}' where id='{1}'".format(nouvalor,identificador.text()) 
                #print(select_update)                
                cur.execute(select_update)
        #falta valor actual i actualitzar valor acumulat amb el valor actual
        if(col==6):
            #print("he d'actualitzar el valor acumulat a la base de dades sumant'hi el valor actual últim entrat")
            uivalor = Ui_Nom()
            uivalor.setupUi(Dialog, self.Llistat.item(row,col), col, row, self.Llistat)
            Dialog.exec_()
            nouvalor=uivalor.canvi()
            identificador=self.Llistat.item(row,0)
            #print("identificador =",identificador.text())
            #print("nouvalor=",nouvalor)
            #self.Llistat.setItem(row,6,QtGui.QTableWidgetItem(nouvalor))
            acumulat=self.Llistat.item(row,7)
            #print("acumulat =",acumulat.text())
            valor=float(nouvalor)+float(acumulat.text())#suma valors
            #print("valor final =",valor)           
            #print("update clients set compra_actual='{0}',acumulat='{1}' where id='{2}'".format(nouvalor,valor,identificador.text()))
            con = lite.connect('clients.db')
            with con:
                cur = con.cursor()               
                self.Llistat.setItem(row,6,QtGui.QTableWidgetItem(nouvalor))                
                self.Llistat.setItem(row,7,QtGui.QTableWidgetItem(format(valor)))                
                select_update="update clients set compra_actual='{0}',acumulat='{1}' where id='{2}'".format(nouvalor,valor,identificador.text()) 
                #print(select_update)                
                cur.execute(select_update)
                
    def setupUi(self, Llista):
       
 
        self.pB_tancar = QtGui.QPushButton(Llista)
        self.pB_tancar.setGeometry(QtCore.QRect(20, 490, 83, 61))
        self.pB_tancar.setObjectName(_fromUtf8("pB_tancar"))
        self.pB_tancar.clicked.connect(Llista.reject)
        self.Llistat = QtGui.QTableWidget(Llista)        
        #self.Llistat.cellClicked.connect(self.cell_was_clicked)
        self.Llistat.setWindowTitle("Mostra els clients entrats")
        self.Llistat.resize(700, 250)
        self.Llistat.setColumnCount(8)
   
        self.Llistat.setHorizontalHeaderLabels(("Id", "Dni", "Nom", "Cogom", "Carrer", "Població", "Import Actual", "Import Acumulat"))
        #print("abans =",self.Llistat.rowCount())  
        #print ("Llisto camps al carregar")        
        con = lite.connect('clients.db')
        with con:                                        
            cur = con.cursor()
            sqlqry = "SELECT * FROM clients ;"
 
            try:
                 cur.execute(sqlqry)
            except sqlite3.Error:
 
                QMessageBox.about(self, "Error fetching %s"%name, "Error")
            self.Llistat.setRowCount(0)

            for row, form in enumerate(cur):            
                self.Llistat.insertRow(row)
                #print("form =",form, "  row = ",row)
                for column in enumerate(form):
                    num,col = column
                    #print(" num = ",num," Col = ",col,"self.Llistat.columnCount() =",self.Llistat.columnCount() ) #, str(item),  form =",form, " form =",form, "                    
                    LlistaItem = QtGui.QTableWidgetItem()
                    if(num==1 or num == 2 or num ==3 or num == 4 ):                    
                        LlistaItem.setText(str(col))
                        self.Llistat.setItem(self.Llistat.rowCount()-1, num, LlistaItem)
                    else:
                        LlistaItem.setText(str(col))                    
                        if(num==7 or num==0):
                            flags = QtCore.Qt.ItemFlags()                                                
                            flags != QtCore.Qt.ItemIsEnabled
                            LlistaItem.setFlags(flags)
                        self.Llistat.setItem(self.Llistat.rowCount()-1, num, LlistaItem)
                        
               
            if cur:
                cur.close()
               
        self.Llistat.resizeColumnsToContents()        

        self.Llistat.cellClicked.connect(self.cellchanged)
        #print("després ",self.Llistat.rowCount())
        #self.pB_modificar = QtGui.QPushButton(Llista)
        #self.pB_modificar.setGeometry(QtCore.QRect(140, 400, 83, 61))
        #self.pB_modificar.setObjectName(_fromUtf8("pB_modificar"))
       
        #mostro la llista PER CONSOLA
        #self.pB_modificar.clicked.connect(self.llista)        
        self.retranslateUi(Llista)
        QtCore.QMetaObject.connectSlotsByName(Llista)
       
    def retranslateUi(self, Llista):
        Llista.setWindowTitle(_translate("Llista", "Llista de Clients", None))
        self.pB_tancar.setText(_translate("Llista", "Tornar", None))
        #self.pB_modificar.setText(_translate("Llista", "Llistar", None))
