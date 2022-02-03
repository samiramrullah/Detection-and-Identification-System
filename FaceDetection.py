##Importing the libraries
from tkinter import *
import cv2
import numpy as np
import face_recognition
import os
import pyttsx3
import pickle
from datetime import datetime
import pymongo
from pymongo import MongoClient
import matplotlib.pyplot as plt
import tkinter as tk

class Detection:
    def __init__(self,root):
        ##Path were pre-existing image is saved
        path = "C:/Users/samir/PycharmProjects/Automatic_attendence/image_attendence"
        images = []
        Person_name = []
        mylist = os.listdir(path)
        print(mylist)
        for cl in mylist:
            current_image = cv2.imread(f'{path}/{cl}')
           # cv2.imshow(current_image)
            images.append(current_image)
            Person_name.append(os.path.splitext(cl)[0])
            print(Person_name)

        def Attendence(name):
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            client = pymongo.MongoClient()
            db = client['Mydb']
            mycoll = db['try']
            db = client['Image_Encodings']
            mycoll = db['Image_refrence']
            record = {name: dt_string}
            mycoll.insert_one(record)


        for cl in mylist:
            current_image = cv2.imread(f'{path}/{cl}')
            images.append(current_image)
            Person_name.append(os.path.splitext(cl)[0])
        #print(Person_name)

        def setnames():
            path1 = 'D:/TRY/try/New_Image'
            mylist1 = os.listdir(path1)
            for cl in mylist1:
                current_image = cv2.imread(f'{path1}/{cl}')
                images.append(current_image)
                Person_name.append(os.path.splitext(cl)[0])
            print(Person_name)

        def Encodings(images):
            encodelist = []
            for img in images:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                encode_image = face_recognition.face_encodings(img)[0]
                encodelist.append(encode_image)
            return encodelist
        def encoding_pickel():
            encoding_pic=Encodings(images)
            file='encode.pkl'
            fileobj=open(file,'wb')
            pickle.dump(encoding_pic,fileobj)
            fileobj.close()
            print('Images Encoded')


        #encoding_pickel()
        font = cv2.FONT_HERSHEY_SIMPLEX
        vid = cv2.VideoCapture(0)

        while True:
            frame, img = vid.read()
            store_image=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            image_resize = cv2.resize(img, (0, 0), None, 0.25, 0.25)
            image_resize = cv2.cvtColor(image_resize, cv2.COLOR_BGR2RGB)
            face_location_current = face_recognition.face_locations(image_resize)
            encode_image_resize = face_recognition.face_encodings(image_resize, face_location_current)
            file_open='encode.pkl'
            file_open_obj=open(file_open,'rb')
            encodelist_forknownfaces=pickle.load(file_open_obj)

            for encoded_face, location in zip(encode_image_resize, face_location_current):
                mathes = face_recognition.compare_faces(encodelist_forknownfaces, encoded_face)
                face_distance = face_recognition.face_distance(encodelist_forknownfaces, encoded_face)
                ##print(face_distance)
                min_dist = np.argmin(face_distance)

                if mathes[min_dist]:
                    name = Person_name[min_dist].upper()
                    #print(name)
                    y1, x2, y2, x1 = location
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                    print(name)
                    cv2.putText(img, name, (x1 + 6, y2 - 6), font, 1, (255, 255, 255), 2)
                    engine = pyttsx3.init()
                    engine.say("This is "+ str(name))
                    engine.runAndWait()
                    Attendence(name)
                    # Attendence(name)
                else:

                    var='The face is unknown'
                    engine = pyttsx3.init()
                    engine.say(var)
                    engine.runAndWait()
                    #cv2.putText(img,var,(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),5)
                    wish=input("Do you want to enter details (y/N)")
                    if wish.upper()=='Y':
                       name=input("Enter the name of the person ")
                       formatim='.jpg'
                       final=name+formatim
                       plt.imshow(img)
                       choice=input("Do you want to take save this or take another image (Y/N) ")
                       if choice.upper()=='Y':
                         path = 'D:/TRY/try/New_Image'
                         cv2.imwrite(os.path.join(path, final), img)
                         setnames()
                         encoding_pickel()
                        #after encoding move this image to folder where other photo are stored and makee it empty for next entry
                       else:
                         pass
                    else:
                        pass


            cv2.imshow('image', img)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        vid.release()
        cv2.destroyAllWindows()