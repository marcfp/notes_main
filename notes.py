# -*- coding: iso-8859-15 -*-
import sys
from PyQt4 import QtGui, QtCore
from notesmain import Ui_Notes

import sys
import signal


        
def main():

    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Notes()
    ui.setupUi(Dialog, app)
    Dialog.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
