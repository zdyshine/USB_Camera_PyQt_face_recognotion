from Ui_Pingan_face import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import QImage
import cv2
import dlib
import numpy as np
import face_recognition


class CameraThread(QThread, Ui_MainWindow):
    CameraFram = pyqtSignal(QImage)
    OpenVideoFlage = pyqtSignal(bool)
    
    def __init__(self):
        super().__init__()

    def run(self):
        
        self.Run_Camera = 1
        self.cap = cv2.VideoCapture(0) # 0是摄像头位置
        
        known_face_encodings = []
        know_face_names = []

        #预定义人脸特征
        zdy_img = face_recognition.load_image_file('zdy.jpg')
        zdy_face_encoding = face_recognition.face_encodings(zdy_img)[0]

        known_face_encodings.append(zdy_face_encoding)
        know_face_names.append('zdy')
        
        if (not self.cap.isOpened()):
            self.cap.open()
            self.cap.set(3, 500)
            self.cap.set(4, 600)
            
        elif (self.cap.isOpened()):
            while self.Run_Camera:
                ret,  self.img_read = self.cap.read()
                cv2.waitKey(1) #延时1s
                if ret !=None:
                    #考虑把图像缩小0.25来检测识别
                    h, w = self.img_read.shape[:2]
                    input_img = cv2.cvtColor(self.img_read, cv2.COLOR_BGR2RGB)
                    #gray_img = cv2.cvtColor(self.img_read, cv2.COLOR_BGR2GRAY)
                    
                    faces = face_recognition.face_locations(input_img)
                    face_encodings = face_recognition.face_encodings(input_img)
                    face_names =[]

                    for face_encoding in face_encodings:
                        matches = face_recognition.compare_faces(known_face_encodings,  face_encoding)
                        name = 'unknown'
                        
                        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                        
                        best_match_inxd = np.argmin(face_distances)
                        
                        if matches[best_match_inxd]:
                            name = know_face_names[best_match_inxd]
                            
                        face_names.append(name)

                    #绘框
                    for name, d in zip(face_names, faces):
                        x1, y1, x2, y2= d[0], d[1], d[2], d[3]
                        input_img = cv2.rectangle(input_img, (y2, x1), (y1, x2), (255, 0, 0), 2)
                        font = cv2.FONT_HERSHEY_DUPLEX
                        cv2.putText(input_img, name, (y2- 6, x2 + 6), font, 1.0, (255, 255, 255), 1)

                    show_pic = QImage(input_img.data,  w, h, QImage.Format_RGB888)
                    
                    if self.Run_Camera:
                        self.CameraFram.emit(show_pic)
                    else:
                        break
                    #time.sleep(0.005)
                else:
                    print('摄像头已打开')
            self.cap.release()
            self.quit()
        else:
            self.OpenVideoFlage.emit(self.cap.isOpened())
    
    def Stop_Video(self):
        self.Run_Camera = 0
        
            
        
    
#    def identify(self):
#        
#        
#    def save_img(self):
            
