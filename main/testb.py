import sys
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *



class Window(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.resize(400,400)
        self.setWindowTitle("Py-CRIT")
        self.button = button = QPushButton(icon=QIcon('C:\Comp Bio\pyTitle.png'))
        self.button.setIconSize(QSize(550,550))
        self.button.clicked.connect(self.onClick)
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)


    def onClick(self, parent=None):
        Tissue = QComboBox()
        Tissue.addItems(['brain','heart','lung'])
        Tissue.show()

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())