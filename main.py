from PyQt5 import QtWidgets
from design import Ui_MainWindow  # импорт нашего сгенерированного файла с именем label
import sys
 
 
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
 
 
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
 
sys.exit(app.exec())