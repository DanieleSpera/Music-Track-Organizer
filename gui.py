#Libraries
import sys
from os import path
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication,QGridLayout,QLabel,QFileDialog, QDirModel, QStatusBar, QHBoxLayout, QProgressDialog
from PyQt5.QtCore import Qt, QCoreApplication, QDir
from PyQt5.QtGui import  QCursor

#Scripts
from SongBpmPlacer import Place

class StartPage(QWidget):
    
    def __init__(self):
        super().__init__()
        self.sourcePath = '' 
        self.destinationPath =''
        self.initUI()
        
    def initUI(self):
        #SOURCE BUTTON
        #Setting Labels & Buttons
        sourcePathLb = QLabel(self.sourcePath, self)
        loadPath1Btn =  QPushButton('Cartella Sorgente', self)
        #Click Action
        loadPath1Btn.setCursor(QCursor(Qt.PointingHandCursor))#pointer on btn
        loadPath1Btn.clicked.connect(lambda:sourcePathLb.setText(self.ChangeSourceLb()))

        #DESTINATION BUTTON
        destinationPathLb = QLabel(self.destinationPath, self)
        loadPath2Btn =  QPushButton('Cartella Destinazione', self)
        #Click Action
        loadPath2Btn.setCursor(QCursor(Qt.PointingHandCursor))#pointer on btn
        loadPath2Btn.clicked.connect(lambda:destinationPathLb.setText(self.ChangeDestinationLb()))

        #START BUTTON
        startBtn = QPushButton('Run', self)
        startBtn.setCursor(QCursor(Qt.PointingHandCursor))#pointer on btn
        startBtn.clicked.connect(self.startPlacer)

        #FOOTER
        self.statusBar = QStatusBar()
        self.statusBar.showMessage("Ready")

        #RENDER GRID
        grid = QGridLayout(self)
        #1  Row
        grid.addWidget(sourcePathLb,0,0)
        grid.addWidget(loadPath1Btn,0,2)
        #2  Row
        grid.addWidget(destinationPathLb,1,0)
        grid.addWidget(loadPath2Btn,1,2)
        #3  Row
        grid.addWidget(startBtn,2,0,1,3)
        #4  Row
        grid.addWidget(self.statusBar,3,0,1,3)

        #Widget Setting
        self.setGeometry(300, 300, 500, 100)
        self.setWindowTitle('Quit button')
        self.setStyleSheet("""
            QWidget {
                border-radius: 10px;
                background-color: #343838;
                color:white
                }
            QPushButton {
                padding:10px;
                border-radius: 10px;
                background-color:#00B4CC;
                color:black
            }
        """)
        self.show()
 
    #BUTTON ACTIONS
        #Source
    def ChangeSourceLb(self):
        fname = QDir.toNativeSeparators(QFileDialog.getExistingDirectory(self, 'Open file', '/home'))
        self.sourcePath = fname
        return str(fname)

        #Destination
    def ChangeDestinationLb(self):
        fname = QDir.toNativeSeparators(QFileDialog.getExistingDirectory(self, 'Open file', '/home'))
        self.destinationPath = fname
        return str(fname)

        #Run
    def startPlacer(self):
        #check empty fields
        if (self.sourcePath == "") or (self.destinationPath==""):
            self.statusBar.showMessage("Controllare di aver selezionato le cartelle")    
            return
        #check different dir
        if self.sourcePath == self.destinationPath:
            self.statusBar.showMessage("Selezionare due cartelle diverse")    
            return

        #wait status
        self.statusBar.showMessage("Elaborazione...Attendere il processo potrebbe richiedere diversi  minuti")
        self.setEnabled(False)

        Place(self.sourcePath,self.destinationPath)

        #ready status
        self.setEnabled(True)
        self.statusBar.showMessage("Processo finito")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StartPage()
    sys.exit(app.exec_())


