self.pB_tancar = QtGui.QPushButton(Llista)
        self.pB_tancar.setGeometry(QtCore.QRect(20, 490, 83, 61))
        self.pB_tancar.setObjectName(_fromUtf8("pB_tancar"))
        self.pB_tancar.clicked.connect(Llista.reject)
        Llistat = QtGui.QTableWidget(Llista)
        LlistaItem = QtGui.QTableWidgetItem()
       
        Llistat.setWindowTitle("Mostra els clients entrats")
        Llistat.resize(700, 250)
        Llistat.setColumnCount(7)
   
        Llistat.setHorizontalHeaderLabels("Id, Nom, Cogom, Carrer, Població, Import Actual, Import Acumulat".split(","))
           
        print ("Llisto camps al carregar")        
        con = lite.connect('clients.db')
        with con:                      
            c = con.cursor()
            select_pos_score = 'SELECT * FROM clients'
            c.execute(select_pos_score)
            i=1
            Llistat.setItem(0, 0, QtGui.QTableWidgetItem("00"))                
            Llistat.setItem(0, 1, QtGui.QTableWidgetItem("01"))                
            Llistat.setItem(0, 2, QtGui.QTableWidgetItem("02"))                
            Llistat.setItem(1, 0, QtGui.QTableWidgetItem("10"))                
            Llistat.setItem(1, 1, QtGui.QTableWidgetItem("11"))                
            Llistat.setItem(1, 2, QtGui.QTableWidgetItem("12"))                
            Llistat.setItem(2, 0, QtGui.QTableWidgetItem("20"))                
            Llistat.setItem(2, 1, QtGui.QTableWidgetItem("21"))                
            Llistat.setItem(2, 2, QtGui.QTableWidgetItem("22"))                
            if 0: #for row in c:                
                (columna0)=row[0]                                
                print(i)                
                Llistat.setItem(0, 0, QtGui.QTableWidgetItem(row[0]))                
                (columna1)=row[1]                
                Llistat.setItem(i, 2, QtGui.QTableWidgetItem(row[1]))
                (columna2)=row[2]                
                Llistat.setItem(i, 3, QtGui.QTableWidgetItem(row[2]))
                (columna3)=row[3]                
                Llistat.setItem(i, 4, QtGui.QTableWidgetItem(row[3]))
                (columna4)=row[4]                
                Llistat.setItem(i, 5, QtGui.QTableWidgetItem(row[4]))
                (columna5)=row[5]                
                Llistat.setItem(i, 6, QtGui.QTableWidgetItem(row[5]))
                (columna6)=row[6]                
                Llistat.setItem(i, 7, QtGui.QTableWidgetItem(row[6]))
                #self.Llista.resizeColumnsToContents();              
                print(columna0,",", columna1,",", columna2,",", columna3,",", columna4,",", columna5,",", columna6)
                i=i+1
   
 
        #self.Llista.resizeColumnsToContents();
        Llistat.show()
 
       
        self.pB_modificar = QtGui.QPushButton(Llista)
        self.pB_modificar.setGeometry(QtCore.QRect(140, 400, 83, 61))
        self.pB_modificar.setObjectName(_fromUtf8("pB_modificar"))
       
        #mostro la llista
        self.pB_modificar.clicked.connect(self.llista)        
        self.retranslateUi(Llista)
        QtCore.QMetaObject.connectSlotsByName(Llista)
