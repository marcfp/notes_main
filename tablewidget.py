from PyQt4.QtGui import * 
from PyQt4.QtCore import * 
import sys

def main():  
    app = QApplication(sys.argv)
    table = QTableWidget()
    
    table.setWindowTitle("Show Tooltip On QTableWidget Column Header")
    table.resize(400, 250)
    table.setColumnCount(3)
    
    table.setHorizontalHeaderLabels("HEADER 1,HEADER 2,HEADER 3")
    
    table.horizontalHeaderItem(0).setToolTip("Column 1 ")
    table.horizontalHeaderItem(1).setToolTip("Column 2 ")
    table.horizontalHeaderItem(2).setToolTip("Column 3 ")
    
    table.show()
    return app.exec_()

if __name__ == '__main__':
    main()
