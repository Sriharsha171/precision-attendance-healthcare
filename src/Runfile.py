import tkinter as tk
from tkinter import Message ,Text
import cv2,os
import shutil
import csv
import cv2
import face_recognition
import numpy as np
import pandas as pd
import sqlite3
import train_faces as knntrain
import numpy as np
import pandas as pd
import sqlite3 
#import datetime
import time
from PIL import Image,ImageStat
from tkinter import *
from datetime import datetime
import incamera as ic
import outcamera as oc
import testdb as viewat
import docsched_db as viewsc 

conn = sqlite3.connect('doctor.db') 
  
# Creating a cursor object using the  
# cursor() method 
cursor = conn.cursor() 

window = tk.Tk()

window.title("Face_Recogniser")


window.configure(background='black')
bg=PhotoImage(file="1.png")
Label1=Label(window,image=bg)
Label1.place(x=0,y=0)


window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

message = tk.Label(window, text="Healthcare Attendance-System" ,bg="white"  ,fg="red"  ,width=50  ,height=3,font=('times', 30, 'italic bold underline')) 

message.place(x=200, y=20)
lbbel3 = tk.Label(window, text="Real Time Implementation:",width=30  ,height=2  ,fg="black"  ,bg="yellow" ,font=('times', 15, ' bold ') ) 
lbbel3.place(x=70, y=250)
bg1=PhotoImage(file="2.png")
Label2=Label(window,image=bg1)
Label2.place(x=150,y=300)

lbl = tk.Label(window, text="Enter ID",width=20  ,height=2  ,fg="black"  ,bg="yellow" ,font=('times', 15, ' bold ') ) 
lbl.place(x=400, y=200)

txt = tk.Entry(window,width=20  ,bg="yellow" ,fg="black",font=('times', 15, ' bold '))
txt.place(x=700, y=215)

lbl2 = tk.Label(window, text="Enter Name",width=20  ,fg="black"  ,bg="yellow"    ,height=2 ,font=('times', 15, ' bold ')) 
lbl2.place(x=400, y=300)

txt2 = tk.Entry(window,width=20  ,bg="yellow"  ,fg="black",font=('times', 15, ' bold ')  )
txt2.place(x=700, y=315)



lbl3 = tk.Label(window, text="Notification : ",width=20  ,fg="black"  ,bg="yellow"  ,height=2 ,font=('times', 15, ' bold underline ')) 
lbl3.place(x=400, y=400)

message = tk.Text(window, bg="yellow"  ,fg="black"  ,width=30  ,height=2,font=('times', 15, ' bold ')) 
message.place(x=700, y=400)
scrollbar = tk.Scrollbar(window, command=message.yview)
scrollbar.place(x=1000, y=400, height=40)

# Configure the Text widget to use the scrollbar
message.config(yscrollcommand=scrollbar.set)


 
def clear():
    txt.delete(0, 'end')
    txt2.delete(0, 'end')        
    res = ""
    message.delete(0.0,'end')


    
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False
 
def TakeImages():
    co=['Id']
    df=pd.read_csv("./PersonDetatils/PersonDetails.csv",names=co)
    
    namess = df['Id']
    ides=[]

    #print'Id:'
    #print namess
    
    Id=(txt.get())
    
    ides=Id
    #print 'Id='
    #print ides
    name=(txt2.get())
    
    estest=0
    if ides in namess:
        estest=1
    else:
        estest=0
    #print estest
    if (estest==0):
        if(is_number(Id) and name.isalpha()):
            cam = cv2.VideoCapture(0)
            #harcascadePath = "haarcascade_frontalface_default.xml"
            #detector=cv2.CascadeClassifier(harcascadePath)
            sampleNum=0
            img_counter = 0
            DIR=f"./Dataset/{name}_{ides}"
            try:
                os.mkdir(DIR)
                print("Directory " , name ,  " Created ") 
            except FileExistsError:
                print("Directory " , name ,  " already exists")
                img_counter = len(os.listdir(DIR1))
            while(True):
                ret, frame = cam.read()
                cv2.imshow("Video", frame)
                if not ret:
                    break
                k = cv2.waitKey(1)
                if k%256 == 27:
                    # ESC pressed
                    print("Escape hit, closing...")
                    break
                elif k%256 == 32:
                    # SPACE pressed
                    img_name = f"./Dataset/{name}_{ides}/opencv_frame_{img_counter}.png"
                    cv2.imwrite(img_name, frame)
                    print("{} written!".format(img_name))
                    img_counter += 1
            cam.release()
            cv2.destroyAllWindows() 
            res = "Images Saved for ID : " + Id +" Name : "+ name
            row = [Id , name]
            with open('./PersonDetatils/PersonDetails.csv','a+') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(row)
            csvFile.close()
            message.insert('end',res)
        else:
            if(is_number(Id)):
                res = "Enter Alphabetical Name"
                message.insert('end',res)
            if(name.isalpha()):
                res = "Enter Numeric Id"
                message.insert('end',res)
        
    else:
        res = "Already Id Exist"
        message.insert('end',res)

   
def TrainImages():
    knntrain.trainer()
    res = "Trained Successfully"
    message.insert('end',res)
def TrackImages():
    print("In Camera Started")
    cam = cv2.VideoCapture(0)
    recognized_name = ic.identify_faces(cam)  # Get the recognized name from the camera
    if recognized_name:
        show_schedule_popup(recognized_name)  # Show the schedule pop-up for the recognized name
def TrackoutImages():
    print("Out Camera Started")
    cam = cv2.VideoCapture(0)# change 0 to 1 for usb camera
    #'rtsp://eswar:eswar@192.168.1.14:8080/h264_ulaw.sdp'
    oc.identify_faces(cam)
def Viewatendance():
    docname = txt2.get().strip()  # Remove extra spaces
    if not docname:  # If docname is empty, pass None to fetch all attendance
        docname = None

    my_conn = sqlite3.connect('doctor.db')
    my_cursor = my_conn.execute("SELECT * FROM attendance")

    for student in my_cursor:
        print("Student:", student)

    viewat.process(docname)  # Pass None if no name is provided

def show_schedule_popup(doctor_name):
    my_conn = sqlite3.connect('hospital.db')
    
    # Query to retrieve patients for the specified doctor
    my_cursor = my_conn.execute("""
        SELECT patients.patient_name, patients.appointment_time 
        FROM patients
        JOIN doctors ON patients.doctor_id = doctors.doctor_id
        WHERE doctors.doctor_name = ?;
    """, (doctor_name,))
    
    # Iterate through the result and print each patient
    for patient in my_cursor:
        print(f"Patient: {patient[0]}")
    viewsc.proc("Dr. "+doctor_name)

    
def viewsched():
    doctor_name = txt2.get()  # Get the doctor's name from the input field
    my_conn = sqlite3.connect('hospital.db')
    
    # Query to retrieve patients for the specified doctor
    my_cursor = my_conn.execute("""
        SELECT patients.patient_name, patients.appointment_time 
        FROM patients
        JOIN doctors ON patients.doctor_id = doctors.doctor_id
        WHERE doctors.doctor_name = ?;
    """, (doctor_name,))
    
    # Iterate through the result and print each patient
    for patient in my_cursor:
        print(f"Patient: {patient[0]}")
    viewsc.proc("Dr. "+doctor_name)
    
        
            
                
                






  
clearButton = tk.Button(window, text="Clear", command=clear  ,fg="red"  ,bg="yellow"  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
clearButton.place(x=1010, y=200)
  
takeImg = tk.Button(window, text="Take Images", command=TakeImages  ,fg="red"  ,bg="yellow"  ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
takeImg.place(x=210, y=500)

trainImg = tk.Button(window, text="Train Images", command=TrainImages  ,fg="red"  ,bg="yellow"  ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
trainImg.place(x=210, y=600)
trackImg = tk.Button(window, text="Start In camera", command=TrackImages  ,fg="red"  ,bg="yellow"  ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
trackImg.place(x=510, y=500)
trackImg1 = tk.Button(window, text="Start Out camera", command=TrackoutImages  ,fg="red"  ,bg="yellow"  ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
trackImg1.place(x=510, y=600)
trackImg2 = tk.Button(window, text="View Attendance", command=Viewatendance  ,fg="red"  ,bg="yellow"  ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
trackImg2.place(x=810, y=500)

quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg="red"  ,bg="yellow"  ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
quitWindow.place(x=810, y=600)
sched_button = tk.Button(
    window, text="Doctor's Schedule", command=viewsched,
    fg="red", bg="yellow", width=20, height=2,
    activebackground="Red", font=('times', 15, 'bold')
)
sched_button.place(x=100, y=400)

 
window.mainloop()
