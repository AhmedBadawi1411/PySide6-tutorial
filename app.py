from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from ui.main_window import MainWindow

import sys #Only need for access command line args

#we need one and only one instance for QApplication per application

app = QApplication(sys.argv)

#after creating application instance we need to create application window
window = MainWindow()

#by default windows are hidden
window.show()

#and finally start app event loop
app.exec()