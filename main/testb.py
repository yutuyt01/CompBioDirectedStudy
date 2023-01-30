import sys
import os
import pandas
from pandas import Series
from compare import compareClass
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
import gget


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
        self.Tissue.addItems(['adipose tissue','adrenal gland','parathyroid gland','atestis','bone marrow',
        'brain','breast','cervix','choroid plexus','endometrium','epididymis','esophagus','fallopian tube','gallbladder',
        'heart','intestine','kidney','liver','lung','lymphoid tissue','ovary','pancreas','pituitary gland','placenta','prostate',
        'retina','salivary gland','seminal vesicle','skeletal muscle','skin','smooth muscle','stomach','thyroid gland',
        'tounge','urinary bladder','vagina'])
        font = QFont('Arial',30)
        self.Tissue.setFont(font)
        self.Tissue.activated.connect(self.current_text)
        layout = QVBoxLayout()
        layout.addWidget(self.Tissue)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    
    def current_text(self):
        ctext = self.Tissue.currentText()
        if ctext == 'adipose tissue':
            compareTypes = compareClass("adipose_tissue.tsv")
            results = compareTypes.compare()
            text = results.size
            widget = QLabel('You found %d matches' %text)
            font = widget.font()
            font.setPointSize(60)
            widget.setFont(font)
            widget.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
            self.setCentralWidget(widget)
        if ctext == 'adrenal gland':
            compareTypes = compareClass("adrenal_gland.tsv")
            results = compareTypes.compare()
            print('you found',results.size,'matches!')
        if ctext == 'parathyroid gland':
            compareTypes = compareClass("aparathyroid_gland.tsv")
            results = compareTypes.compare()
            print('you found',results.size,'matches!')
        if ctext == 'atestis':
            compareTypes = compareClass("atestis.tsv")
            results = compareTypes.compare()
            print('you found',results.size,'matches!')
        if ctext == 'bone marror':
            compareTypes = compareClass("bone_marrow.tsv")
            results = compareTypes.compare()
            print('you found',results.size,'matches!')
        if ctext == 'brain':
            compareTypes = compareClass("brain.tsv")
            results = compareTypes.compare()
            print('you found',results.size,'matches!')       
        if ctext == 'breast':
            compareTypes = compareClass("breast.tsv")
            results = compareTypes.compare()
            print('you found',results.size,'matches!')
        if ctext == 'cervix':
            compareTypes = compareClass("cervix.tsv")
            results = compareTypes.compare()
            print('you found',results.size,'matches!')
        if ctext == 'choroid plexus':
            compareTypes = compareClass("choroid_plexus.tsv")
            results = compareTypes.compare()
            print('you found',results.size,'matches!')      
        if ctext == 'endometrium':
            compareTypes = compareClass("endometrium.tsv")
            results = compareTypes.compare()
            print('you found',results.size,'matches!')
        if ctext == 'epididymis':
            compareTypes = compareClass("epididymis.tsv")
            results = compareTypes.compare()
            print('you found',results.size,'matches!')
        if ctext == 'esophagus':
            compareTypes = compareClass("esophagus.tsv")
            results = compareTypes.compare()
            print('you found',results.size,'matches!')       
        if ctext == 'fallopian tube':
            compareTypes = compareClass("fallopian_tube.tsv")
            results = compareTypes.compare()
            print('you found',results.size,'matches!')
        if ctext == 'gallbladder':
            compareTypes = compareClass("gallbladder.tsv")
            results = compareTypes.compare()
            print('you found',results.size,'matches!')
        if ctext == 'heart':
            compareTypes = compareClass("heart.tsv")
            results = compareTypes.compare()
            print('you found',results.size,'matches!')       
        if ctext == 'intestine':
            compareTypes = compareClass("intestine.tsv")
            results = compareTypes.compare()
            print('you found',results.size,'matches!')
        if ctext == 'kidney':
            compareTypes = compareClass("kidney.tsv")
            results = compareTypes.compare()
            print('you found',results.size,'matches!')
        if ctext == 'liver':
            compareTypes = compareClass("liver.tsv")
            results = compareTypes.compare()
            print('you found',results.size,'matches!')       
        if ctext == 'lung':
            compareTypes = compareClass("lung.tsv")
            results = compareTypes.compare()
            print('you found',results.size,'matches!')
        if ctext == 'lymphoid tissue':
            compareTypes = compareClass("lymphoid_tissue.tsv")
            results = compareTypes.compare()
            print('you found',results.size,'matches!')
        if ctext == 'ovary':
            compareTypes = compareClass("ovary.tsv")
            results = compareTypes.compare()
            print('you found',results.size,'matches!')       
        if ctext == 'pancreas':
            compareTypes = compareClass("pancreas.tsv")
            results = compareTypes.compare()
            print('you found',results.size,'matches!')
        if ctext == 'pituitary gland':
            compareTypes = compareClass("pituitary_gland.tsv")
            results = compareTypes.compare()
            print('you found',results.size,'matches!')
        if ctext == 'placenta':
            compareTypes = compareClass("placenta.tsv")
            results = compareTypes.compare()
            print('you found',results.size,'matches!')       
        if ctext == 'prostate':
            compareTypes = compareClass("prostate.tsv")
            results = compareTypes.compare()
            print('you found',results.size,'matches!')
        if ctext == 'retina':
            compareTypes = compareClass("retina.tsv")
            results = compareTypes.compare()
            print('you found',results.size,'matches!')
        if ctext == 'salivary gland':
            compareTypes = compareClass("salivary_gland.tsv")
            results = compareTypes.compare()
            print('you found',results.size,'matches!') 
        if ctext == 'seminal vesicle':
            compareTypes = compareClass("seminal_vesicle.tsv")
            results = compareTypes.compare()
            print('you found',results.size,'matches!')
        if ctext == 'sekeletal muscle':
            compareTypes = compareClass("skeletal_muscle.tsv")
            results = compareTypes.compare()
            print('you found',results.size,'matches!')
        if ctext == 'skin':
            compareTypes = compareClass("skin.tsv")
            results = compareTypes.compare()
            print('you found',results.size,'matches!')
        if ctext == 'smooth muscle':
            compareTypes = compareClass("smooth_muscle.tsv")
            results = compareTypes.compare()
            print('you found',results.size,'matches!')
        if ctext == 'stomach':
            compareTypes = compareClass("stomach.tsv")
            results = compareTypes.compare()
            print('you found',results.size,'matches!')
        if ctext == 'thyroid gland':
            compareTypes = compareClass("thyroid_gland.tsv")
            results = compareTypes.compare()
            print('you found',results.size,'matches!') 
        if ctext == 'tongue':
            compareTypes = compareClass("tongue.tsv")
            results = compareTypes.compare()
            print('you found',results.size,'matches!')
        if ctext == 'urinary bladder':
            compareTypes = compareClass("urinary_bladder.tsv")
            results = compareTypes.compare()
            print('you found',results.size,'matches!')
        if ctext == 'vagina':
            compareTypes = compareClass("vagina.tsv")
            results = compareTypes.compare()
            print('you found',results.size,'matches!') 

        
        

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())