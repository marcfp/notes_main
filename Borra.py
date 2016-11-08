# -*- coding: utf-8 -*-
 
# Form implementation generated from reading ui file 'Llistar.ui'
#
# Created: Tue Sep  2 19:13:26 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

 
from PyQt4 import QtCore, QtGui, QtSql
#from Nom import Ui_Nom
import sqlite3 as lite
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


class Ui_Borra(QtGui.QWidget):
   
    def __init__(self):
        QtGui.QWidget.__init__(self)
      
    def llista( self): #these sources shows values from sqlite into python prompt
        #print ("Llisto camps")        
        con = lite.connect('clients.db')
        with con:
            cur = con.cursor()
            #print("arriba?");                
            select_pos_score = 'SELECT * FROM clients'
            cur.execute(select_pos_score)            
            for (Id, Nom, Cognoms, Direccio, Poble, Compra_actual, Acumulat) in cur.fetchall():
                print (Id, Dni, Nom, Cognoms, Direccio, Poble, Compra_actual, Acumulat)           
            if cur:
                cur.close()    
    def borrar(self):
        """Handler for the SIGINT signal."""
        #sys.stderr.write('\r')
        resposta = QtGui.QMessageBox.question(None, '', "Segur que vols BORRAR-ME ?",
                                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
                                QtGui.QMessageBox.No)
        if  (resposta== QtGui.QMessageBox.Yes):            
            print("Si Borra!!!")
            self.cellchanged(self)
            
    def cellchanged(self,self2):
        
        col = self2.Borra.currentColumn()
        
        row = self2.Borra.currentRow()
        
        valor = self2.Borra.item(row,col)
        
        if(col==0):
            print("borra per Id")
            con = lite.connect('clients.db')
            with con:
                cur = con.cursor()
                #print("arriba?");                
                select_pos_score = 'DELETE  FROM clients WHERE id={0}'.format(valor.text())
                #print(select_pos_score)
                cur.execute(select_pos_score)
        if(col==1):
            print("borra per DNI")
            con = lite.connect('clients.db')
            with con:
                cur = con.cursor()
                #print("arriba?");                
                select_pos_score = 'DELETE  FROM clients WHERE dni="{0}"'.format(valor.text())
                #print(select_pos_score)
                cur.execute(select_pos_score)     
        if(col==2):
            print("borra per Nom")
            con = lite.connect('clients.db')
            with con:
                cur = con.cursor()
                #print("arriba?");                
                select_pos_score = 'DELETE  FROM clients WHERE nom="{0}"'.format(valor.text())
                #print(select_pos_score)
                cur.execute(select_pos_score)     
        if(col==3):
            print("borra per Cognom")
            con = lite.connect('clients.db')
            with con:
                cur = con.cursor()
                #print("arriba?");                
                select_pos_score = 'DELETE  FROM clients WHERE cognoms="{0}"'.format(valor.text())
                #print(select_pos_score)
                cur.execute(select_pos_score)     
        if(col==4):
            print("borra per Carrer")
            con = lite.connect('clients.db')
            with con:
                cur = con.cursor()
                #print("arriba?");                
                select_pos_score = 'DELETE  FROM clients WHERE direccio="{0}"'.format(valor.text())
                #print(select_pos_score)
                cur.execute(select_pos_score)     
        if(col==5):
            print("borra per Població")
            con = lite.connect('clients.db')
            with con:
                cur = con.cursor()
                #print("arriba?");                
                select_pos_score = 'DELETE  FROM clients WHERE poble="{0}"'.format(valor.text())
                #print(select_pos_score)
                cur.execute(select_pos_score)     
        if(col==6):
            print("borra per Import Actual")
            con = lite.connect('clients.db')
            with con:
                cur = con.cursor()
                #print("arriba?");                
                select_pos_score = 'DELETE FROM clients WHERE Compra_actual={0}'.format(valor.text())
                #print(select_pos_score)
                cur.execute(select_pos_score)     
        if(col==7):
            print("borra per Import Acumulat")
            con = lite.connect('clients.db')
            with con:
                cur = con.cursor()
                #print("arriba?");                
                select_pos_score = 'DELETE FROM clients WHERE Acumulat={0}'.format(valor.text())
                #print(select_pos_score)
                cur.execute(select_pos_score)     
        self.Borra.removeRow(row)
    def setupUi(self, Llista):
       
 
        self.pB_tancar = QtGui.QPushButton(Llista)
        self.pB_tancar.setGeometry(QtCore.QRect(20, 490, 83, 61))
        self.pB_tancar.setObjectName(_fromUtf8("pB_tancar"))
        self.pB_tancar.clicked.connect(Llista.reject)
        self.Borra = QtGui.QTableWidget(Llista)        
        #self.Borra.cellClicked.connect(self.cell_was_clicked)
        self.Borra.setWindowTitle("Borra clients ")
        self.Borra.resize(700, 250)
        self.Borra.setColumnCount(8)
   
        self.Borra.setHorizontalHeaderLabels(("Id", "Dni", "Nom", "Cogom", "Carrer", "Població", "Import Actual", "Import Acumulat"))
        #print("abans =",self.Borra.rowCount())  
        #print ("Llisto camps al carregar")        
        con = lite.connect('clients.db')
        with con:                                        
            cur = con.cursor()
            sqlqry = "SELECT * FROM clients ;"
 
            try:
                 cur.execute(sqlqry)
            except sqlite3.Error:
 
                QMessageBox.about(self, "Error fetching %s"%name, "Error")
            self.Borra.setRowCount(0)

            for row, form in enumerate(cur):            
                self.Borra.insertRow(row)
                #print("form =",form, "  row = ",row)
                for column in enumerate(form):
                    num,col = column
                    #print(" num = ",num," Col = ",col,"self.Borra.columnCount() =",self.Borra.columnCount() ) #, str(item),  form =",form, " form =",form, "                    
                    LlistaItem = QtGui.QTableWidgetItem()
                    if(num==1 or num == 2 or num ==3 or num == 4 ):                    
                        LlistaItem.setText(str(col))
                        self.Borra.setItem(self.Borra.rowCount()-1, num, LlistaItem)
                    else:
                        LlistaItem.setText(str(col))                    
                        self.Borra.setItem(self.Borra.rowCount()-1, num, LlistaItem)                                        
               
            if cur:
                cur.close()
               
        self.Borra.resizeColumnsToContents()        

        self.Borra.cellClicked.connect(self.borrar)
        #print("després ",self.Borra.rowCount())
        #self.pB_modificar = QtGui.QPushButton(Llista)
        #self.pB_modificar.setGeometry(QtCore.QRect(140, 400, 83, 61))
        #self.pB_modificar.setObjectName(_fromUtf8("pB_modificar"))
       
        #mostro la llista PER CONSOLA
        #self.pB_modificar.clicked.connect(self.llista)        
        self.retranslateUi(Llista)
        QtCore.QMetaObject.connectSlotsByName(Llista)
       
    def retranslateUi(self, Llista):
        Llista.setWindowTitle(_translate("Llista", "Borra Clients", None))
        self.pB_tancar.setText(_translate("Llista", "Tornar", None))
        #self.pB_modificar.setText(_translate("Llista", "Llistar", None))
