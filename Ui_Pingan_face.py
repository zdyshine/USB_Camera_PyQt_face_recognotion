# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\0-比赛\Pingan_face\Pingan_face.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 477)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.Camer_label = QtWidgets.QLabel(self.centralWidget)
        self.Camer_label.setGeometry(QtCore.QRect(50, 80, 291, 311))
        self.Camer_label.setObjectName("Camer_label")
        self.camera_pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.camera_pushButton.setGeometry(QtCore.QRect(380, 110, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Jenson Pro Lt Disp")
        font.setPointSize(11)
        self.camera_pushButton.setFont(font)
        self.camera_pushButton.setObjectName("camera_pushButton")
        self.info_pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.info_pushButton.setGeometry(QtCore.QRect(380, 310, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Jenson Pro Lt Disp")
        font.setPointSize(11)
        self.info_pushButton.setFont(font)
        self.info_pushButton.setObjectName("info_pushButton")
        self.name_label = QtWidgets.QLabel(self.centralWidget)
        self.name_label.setGeometry(QtCore.QRect(550, 140, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Jenson Pro Lt Disp")
        font.setPointSize(11)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        self.sex_label = QtWidgets.QLabel(self.centralWidget)
        self.sex_label.setGeometry(QtCore.QRect(550, 190, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Jenson Pro Lt Disp")
        font.setPointSize(11)
        self.sex_label.setFont(font)
        self.sex_label.setObjectName("sex_label")
        self.age_label = QtWidgets.QLabel(self.centralWidget)
        self.age_label.setGeometry(QtCore.QRect(550, 240, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Jenson Pro Lt Disp")
        font.setPointSize(11)
        self.age_label.setFont(font)
        self.age_label.setObjectName("age_label")
        self.id_label = QtWidgets.QLabel(self.centralWidget)
        self.id_label.setGeometry(QtCore.QRect(550, 290, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Jenson Pro Lt Disp")
        font.setPointSize(11)
        self.id_label.setFont(font)
        self.id_label.setObjectName("id_label")
        self.recognition_pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.recognition_pushButton.setGeometry(QtCore.QRect(380, 210, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Jenson Pro Lt Disp")
        font.setPointSize(11)
        self.recognition_pushButton.setFont(font)
        self.recognition_pushButton.setObjectName("recognition_pushButton")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Camer_label.setText(_translate("MainWindow", "TextLabel"))
        self.camera_pushButton.setText(_translate("MainWindow", "打开摄像头"))
        self.info_pushButton.setText(_translate("MainWindow", "信息采集"))
        self.name_label.setText(_translate("MainWindow", "姓 名"))
        self.sex_label.setText(_translate("MainWindow", "性 别"))
        self.age_label.setText(_translate("MainWindow", "年 龄"))
        self.id_label.setText(_translate("MainWindow", "工 号"))
        self.recognition_pushButton.setText(_translate("MainWindow", "人脸识别"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

