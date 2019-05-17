from Ui_Pingan_face import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import QImage
import os
from skimage import io
import csv
import numpy as np
import pandas as pd
import dlib

class Add_Person(QThread, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
        self.facerec = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")

    def get_feature(self,  img_path):
        img = cv2.imread(img_path)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        dets = self.detector(img_gray, 1)
        if(len(dets)!=0):
            shape = predictor(img_gray, dets[0])
            face_descriptor = self.facerec.compute_face_descriptor(img_gray, shape)
        else:
            face_descriptor = 0
            print("no face")
        return face_descriptor
        
    def write_into_csv(self, path_pic,  name):
        path_csv = './infor.csv'
        #第一列是name 第二列是特征
        infor = []
        infor.append(name)
        csvfile =  open(path_csv, "a", newline="") 
        writer = csv.writer(csvfile)
        features = self.get_feature(path_pic)
        infor.append(features)
        #获取csv文件长度、把新的特征写到长度+1的位置上
        if features ==0:
            print('None') #警告 特征为0
        else:
            writer.writerow(infor)
            
    #def compute_distance(self):
        
