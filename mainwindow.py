from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import Slot
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
        return \
            QMessageBox.information(self, "Info", "Successful Connection") if status else \
            QMessageBox.information(self, "Info", "Fail Connection")

    @Slot()
    def get_nombre(self) -> str:
        s = ""
        if self.plc.status:
            db, offset, size = 2, 2, 12
            s = self.plc.read_plc_string(db, offset, size)
            return s
        return s
