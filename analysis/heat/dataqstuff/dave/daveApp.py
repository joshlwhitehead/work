from PyQt5 import QtCore, QtGui, QtWidgets
from davetool import Dave_Window


# run the file

app = QtWidgets.QApplication([])
daveWin = Dave_Window(False)
daveWin.show()
app.exec_()
