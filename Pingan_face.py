# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
点击，打开摄像头（多线程 ），或者显示失败
点击，开始识别：能识别，显示信息，不能识别，信息采集
点击，信息采集，添加新人信息（数据库或者动态数组）
"""
from PyQt5 import  QtGui,  QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Ui_Pingan_face import Ui_MainWindow
from Open_Camera import CameraThread
#from Add_person import Add_Person


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.Camera = CameraThread()
        #self.Add = Add_Person()   
        
    def OpenCamera(self):
        if not self.Camera.isRunning():
            self.Camera.start()
            self.camera_pushButton.setText('关闭摄像头')
        else:
            self.Camera.Stop_Video()
            self.camera_pushButton.setText('打开摄像头')
            #self.Camer_label.setPixmap(QPixmap.fromImage())  #设置图片还原
    
    def Fresh_Camera(self, show_pic):
        self.Camer_label.setScaledContents(True) #图片自适应大小
        self.Camer_label.setPixmap(QPixmap.fromImage(show_pic))
    
    def Un_Open(self):
        QtWidgets.QMessageBox.warning(self, '警告',  '打开摄像头失败')
    
    
    @pyqtSlot()
    def on_camera_pushButton_clicked(self):
        self.OpenCamera()
        self.Camera.CameraFram.connect(self.Fresh_Camera)
        self.Camera.OpenVideoFlage.connect(self.Un_Open)

        
    
    @pyqtSlot()
    def on_recognition_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_info_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
        
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
