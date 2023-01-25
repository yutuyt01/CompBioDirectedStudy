import sys
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *



class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(400,400)
        self.setWindowTitle("Py-CRIT")
        self.button = button = QPushButton(icon=QIcon('C:\Comp Bio\pyTitle.png'))
        self.button.setIconSize(QSize(550,550))
        self.button.clicked.connect(self.onClick)
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        container = QWidget()
        container.setLayout(layout)
        self.Tissue = QComboBox()
        self.setCentralWidget(container)
        

    def onClick(self):
        #self.Tissue = QComboBox()
        self.Tissue.addItems(['Brain','Heart','Lung'])
        font = QFont('Arial',50)
        self.Tissue.setFont(font)
        self.Tissue.activated.connect(self.current_text)
        layout = QVBoxLayout()
        layout.addWidget(self.Tissue)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    
    def current_text(self):
        ctext = self.Tissue.currentText()
        if ctext == 'Heart':
            print('you chose heart!')
        if ctext == 'Lung':
            print('you chose lung!')
        if ctext == 'Brain':
            print('you chose brain!')

        

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())