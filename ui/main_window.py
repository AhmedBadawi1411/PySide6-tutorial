from PySide6.QtWidgets import QMainWindow, QPushButton
from PySide6.QtCore import QSize

class MainWindow(QMainWindow) :
        
        def __init__(self):
                super().__init__()
                
                self.setWindowTitle("My First App")
                self .setFixedSize(QSize(400,300))
                
                #We can also use setMinimumSize() and .setMaximumSize()
                
                self.btn = QPushButton("Hello PySide6")
                self.btn.setMaximumSize(QSize(100, 45))
                self.btn.setCheckable(True)
                self.btn.clicked.connect(MainButtonBehaviors.onButtonClicked)
                self.btn.clicked.connect(MainButtonBehaviors.onButtonToggled)
                
                self.setCentralWidget(self.btn)

class MainButtonBehaviors:
        def onButtonClicked():
                print("Clicked")
                
        def onButtonToggled(checked):
                print("Checked?", checked)