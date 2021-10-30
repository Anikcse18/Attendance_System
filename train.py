from tkinter import *
from tkinter import ttk, Label
from PIL import Image,ImageTk
from tkinter import messagebox
#import mysql.connector
import cv2                      #computer vison machine learning algorithm
import os
import numpy as np
import glob



class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="TRAIN DATA SET",
                          font=("times new roman", 35, "bold"), bg="#B1E0B8", fg="#CB6CE6")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        #Upper Image
        top_image = Image.open("Software Image/Train_UpperBanner_2.png")
        top_image = top_image.resize((1500, 200), Image.ANTIALIAS)
        self.phototop_image = ImageTk.PhotoImage(top_image)

        first_label = Label(self.root, image=self.phototop_image)
        first_label.place(x=0, y=45, width=1500, height=200)

        #Lower_image
        lower_image = Image.open("Software Image/Train_Lower_image_3.png")
        lower_image = lower_image.resize((1500,600), Image.ANTIALIAS)
        self.photolower_image = ImageTk.PhotoImage(lower_image)

        first_label = Label(self.root, image=self.photolower_image)
        first_label.place(x=0, y=245, width=1500, height=600)

        #button_Image
        b1_1 = Button(first_label, text="TRAIN DATA",command = self.train_classsifer, cursor="hand2", font=("times new roman", 35, "bold"), bg="#B1E0B8", fg="RED")

        b1_1.place(x=600, y=20, width=300, height=250)
#LPBH Algorithm

    def train_classsifer(self):
        data_dir=("data")

        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces = []
        ids = []
        for image in path:

            img = Image.open(image).convert('L')
            imageNp = np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)

            cv2.waitKey(1)==13

        ids = np.array(ids)

        #====================Train Classifier and save=========

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Traning Dataset Completed")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()


    #5th number videooo
