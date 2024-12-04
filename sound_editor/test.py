from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QCheckBox, QFileDialog
import sys
from PySide2.QtCore import Qt

class SoundEditorController(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Settings")
        self.setGeometry(300,300,500,400)

        #self.uploadSoundFile()
        self.layout = QVBoxLayout()
        self.createCheckBox()
        self.setButton()
        self.setLayout(self.layout)
        self.show()

    def setButton(self):
        btn1 = QPushButton("Select Audio File", self)
        btn1.clicked.connect(self.uploadSoundFile)
        self.layout.addWidget(btn1)

    def uploadSoundFile(self):
        fbar = QFileDialog()
        fbar.setNameFilter("select file (*.mp3 *.wav)")
        fbar.exec_()
        self.output = fbar.selectedFiles()
        print(self.output)



    def createCheckBox(self):
        self.label = QLabel("", self)

        check = QCheckBox("RenderSound", self)
        check.stateChanged.connect(self.checkBoxChange)

        self.layout.addWidget(check)
        self.layout.addWidget(self.label)


    def checkBoxChange(self, state):
        if state == Qt.Checked:
            self.label.setText("RenderSound is enabled")

        else:
            self.label.setText("RenderSound is disabled")


myapp = QApplication(sys.argv)
window = SoundEditorController()

myapp.exec_()
sys.exit()
#print(self.output)