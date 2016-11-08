from PyQt4.QtGui import * 
from PyQt4.QtCore import * 
import sys

def main():  
    app 	= QApplication(sys.argv)
    table 	= QTableWidget()
    tableItem 	= QTableWidgetItem()
    
    table.setWindowTitle("Set QWidget for Entire QTableWidget Column")
    table.resize(400, 250)
    table.setRowCount(4)
    table.setColumnCount(3)
    
    table.setHorizontalHeaderLabels("HEADER 1;HEADER 2;HEADER 3;HEADER 4")

    table.setItem(0,0, QTableWidgetItem("ITEM u_u"))
    table.setItem(0,1, QTableWidgetItem("ITEM 1_2"))
    
    table.setItem(1,0, QTableWidgetItem("ITEM 2_1"))
    table.setItem(1,1, QTableWidgetItem("ITEM 2_2"))
    
    table.setItem(2,0, QTableWidgetItem("ITEM 3_1"))
    table.setItem(2,1, QTableWidgetItem("ITEM 3_2"))
    
    table.setItem(3,0, QTableWidgetItem("ITEM 4_1"))
    table.setItem(3,1, QTableWidgetItem("ITEM 4_2"))

    #Add Widget to the rightmost Element of First Row
    table.setItem(0,2,tableItem)
    
    #Add QPushButton to the rightmost QTableWidgetItem on first row
    table.setCellWidget(0,2, QPushButton("Cell Widget"));
    
    #Span Right-Most Item of First Row Here
    table.setSpan(0,2,table.rowCount(),1);
    table.show()
    return app.exec_()

if __name__ == '__main__':
    main()
