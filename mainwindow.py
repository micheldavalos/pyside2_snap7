from PySide6.QtWidgets import QMainWindow, QMessageBox
from ui_mainwindow import Ui_MainWindow
from snap7_controller import Snap7

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        ui = Ui_MainWindow()
        ui.setupUi(self)

        self.plc = Snap7("192.168.0.254", 0, 0)
        self.__connect()

    def __connect(self):
        status = self.plc.connect()
        if status:
            QMessageBox.information(self, "Info", "Successful Connection")
