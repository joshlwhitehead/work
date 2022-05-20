from PyQt5 import QtCore, QtGui, QtWidgets
from davetool import DaveWindow

# run the file

app = QtWidgets.QApplication([])
daveWin = DaveWindow()
daveWin.show()
app.exec_()



