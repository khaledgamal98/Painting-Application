from PyQt5.QtWidgets import *
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon, QImage, QPainter, QPen, QBrush
from PyQt5.QtCore import Qt, QPoint
class Painting(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400,400,600,600)
        self.setMinimumHeight(200)
        self.setMinimumWidth(200)
        self.setMaximumHeight(800)
        self.setMaximumWidth(800)
        self.centeringWindow()
        self.setWindowTitle("Painting Application")
        self.setIcon() #method To put a window icon
        self.layout()
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)
        self.drawing = False
        self.brushSize = 2
        self.brushColor = Qt.black
        self.lastPoint = QPoint()
        color1 = QPushButton(self)
        color1.setGeometry(200, 150, 50, 50)
        color1.setStyleSheet("border-radius : 25;border : 2px solid black;background-color:white")
        color1.move(550,0)
        color1.clicked.connect(self.whiteColor)
        color2=QPushButton(self)
        color2.setGeometry(200, 150, 50, 50)
        color2.setStyleSheet("border-radius : 25;border : 2px solid black;background-color:black")
        color2.move(500, 0)
        color2.clicked.connect(self.blackColor)
        color3=QPushButton(self)
        color3.setGeometry(200, 150, 50, 50)
        color3.setStyleSheet("border-radius : 25;border : 2px solid black;background-color:blue")
        color3.clicked.connect(self.blueColor)
        color3.move(550,50)
        color4=QPushButton(self)
        color4.setGeometry(200,150,50,50)
        color4.setStyleSheet("border-radius : 25;border : 2px solid black;background-color:red")
        color4.move(500,50)
        color4.clicked.connect(self.redColor)
        color5=QPushButton(self)
        color5.setGeometry(200,150,50,50)
        color5.setStyleSheet("border-radius:25;border:2px solid black;background-color:green")
        color5.move(550,100)
        color5.clicked.connect(self.greenColor)
        color6=QPushButton(self)
        color6.setGeometry(200,150,50,50)
        color6.setStyleSheet("border-radius:25;border:2px solid black;background-color:yellow")
        color6.move(500,100)
        color6.clicked.connect(self.yellowColor)
        self.button1=QPushButton(self)
        self.button1.resize(100, 50)
        self.button1.move(0,0)
        self.button1.setIcon(QtGui.QIcon("erase.png"))
        self.button1.clicked.connect(self.whiteColor)
        self.button2 = QPushButton(self)
        self.button2.resize(100, 50)
        self.button2.move(0, 50)
        self.button2.setIcon(QtGui.QIcon("painting.png"))
        self.button2.clicked.connect(self.blackColor)
        self.button3 = QPushButton(self)
        self.button3.resize(100, 50)
        self.button3.move(0,100)
        self.button3.setIcon(QtGui.QIcon("save.png"))
        self.button3.clicked.connect(self.save)
        self.button2 = QPushButton(self)
        self.button2.resize(100, 50)
        self.button2.move(0, 150)
        self.button2.setIcon(QtGui.QIcon("clear.png"))
        self.button2.clicked.connect(self.clear)
    def setIcon(self):
        self.setWindowIcon(QtGui.QIcon("Icon.png"))
    def whiteColor(self):
        self.brushColor=Qt.white
    def blackColor(self):
        self.brushColor=Qt.black
    def blueColor(self):
        self.brushColor=Qt.blue
    def redColor(self):
        self.brushColor=Qt.red
    def greenColor(self):
        self.brushColor=Qt.green
    def yellowColor(self):
        self.brushColor=Qt.yellow
    def centeringWindow(self):
        window_geometery = self.frameGeometry()  # Geometery of the main window
        center_point = QDesktopWidget().availableGeometry().center()  # center point of the screen
        window_geometery.moveCenter(center_point)  # move window's(rectangle) center point to the screen center point
        self.move(window_geometery.topLeft())  # top left of rectangle becomes top left of window
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()
            # print(self.lastPoint)

    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):

        if event.button() == Qt.LeftButton:
            self.drawing = False

    def paintEvent(self, event):
        canvasPainter = QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())
    def save(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                  "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")

        if filePath == "":
            return
        self.image.save(filePath)

    def clear(self):
        self.image.fill(Qt.white)
        self.update()



QApplication_object=QApplication([])
Painting=Painting()
Painting.show()
QApplication_object.exec_()
sys.exit()

