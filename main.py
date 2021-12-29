from PySide2.QtWidgets import QApplication
from mainwindow import MainWindow

# Only needed for access to command line arguments
import sys

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # You need one (and only one) QApplication instance per application.
    # Pass in sys.argv to allow command line arguments for your app.
    # If you know you won't use command line arguments QApplication([]) works too.
    app = QApplication(sys.argv)

    # Create a Qt widget, which will be our window.
    window = MainWindow()
    window.show()  # IMPORTANT!!!!! Windows are hidden by default.

    # Start the event loop.
    app.exec_()

    # Your application won't reach here until you exit and the event
    # loop has stopped.


