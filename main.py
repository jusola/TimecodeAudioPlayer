import sys
import os


from PySide2.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader

class DeviceSelector(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = QUiLoader().load("deviceselector.ui")
        self.ui.show()
        self.closebutton = self.ui.findChild(QPushButton, "dialogCloseButton")
        self.closebutton.clicked.connect(self.ui.close)

class TAPmain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = QUiLoader().load("form.ui")
        self.ui.show()
        self.initSettingsButton()

    def initSettingsButton(self):
        self.button = self.ui.findChild(QPushButton, "selectDevicesButton")
        self.button.clicked.connect(self.openDeviceSelector)
    
    def openDeviceSelector(self):
        self.devselector = DeviceSelector()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = TAPmain()
    sys.exit(app.exec_())
