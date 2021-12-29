from PySide2.QtWidgets import QMainWindow, QMessageBox
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow

from apscheduler.schedulers.qt import QtScheduler

from snap7_controller import Snap7


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.scheduler = QtScheduler()
        self.scheduler.add_job(self.read_data, 'interval', seconds=1)

        self.plc = Snap7("192.168.0.254", 0, 0)
        self.__connect()

        self.ui.pushButton_get_nombre.clicked.connect(self.get_nombre)


    def __connect(self):
        status = self.plc.connect()
        if status:
            QMessageBox.information(self, "Info", "Successful Connection")
            self.scheduler.start()
        else:
            QMessageBox.information(self, "Info", "Fail Connection")

    @Slot()
    def get_nombre(self):
        s = ""
        if self.plc.status:
            db, offset, size = 2, 2, 12
            s = self.plc.read_plc_string(db, offset, size)

        self.ui.lineEdit_nombre.setText(s)

    def read_data(self):
        db, offset, size = 2, 16, 2
        value = self.plc.read_plc_int(db, offset, size)
        self.ui.lcdNumber.display(value)
