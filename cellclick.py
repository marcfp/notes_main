from PyQt4 import QtCore, QtGui
import sys

#############Define MyTableWidget Class Here ############
class MyTableWidget(QtGui.QTableWidget):
##-----------------------------------------  
    def __init__(self):
        QtGui.QTableWidget.__init__(self)
        self.setWindowTitle("QTableWidget Cell Click")
        self.setRowCount(3)
        self.setColumnCount(3)
    
    @QtCore.pyqtSlot(int, int) # prevents executing following function twice http://stackoverflow.com/questions/16367090/python-pyqt-qtablewidget-get-cell-value-based-on-header-string-and-selected-r
    def cell_was_clicked(self, item, item2):        
        row=str(item)        
        print("row=",row)       
        col=str(item2)
        print("col=",col)
        QtGui.QMessageBox.information(self,"QTableWidget Cell Click",	"Row: "+row+" | Column: "+col)

##########End of Class Definition ################## 


def main():
    app = QtGui.QApplication(sys.argv)
    #app.
    window = MyTableWidget()
    window.cellClicked.connect(window.cell_was_clicked)
    window.show() 
    return app.exec_()
 
if __name__ == '__main__': 
    main() 
