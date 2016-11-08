from PyQt4.QtCore import *
from PyQt4.QtGui  import *
import sys

#############Define MyTableWidget Class Here ############
class MyTableWidget(QTableWidget):
##-----------------------------------------  
    def __init__(self):
        QTableWidget.__init__(self)
        self.setWindowTitle("QTableWidget Item Click")
        self.setRowCount(1)
        self.setColumnCount(2)
        self.setItem(0,0,QTableWidgetItem("Item 1"))
        self.setItem(0,1,QTableWidgetItem("Item 2"))
    
    
##-----------------------------------------    
    @pyqtSlot('QTableWidgetItem')
    def slotItemClicked(self,item):
        QMessageBox.information(self, "QTableWidget Cell Click", "Text: "+item.text())
##########End of Class Definition ################## 

def main():
    app = QApplication(sys.argv)
    window = MyTableWidget()
    window.itemClicked.connect(window.slotItemClicked)
    window.show() 
    return app.exec_()
 
if __name__ == '__main__': 
    main() 
 

