import os
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from Student import student
from Face_Recognitation import face_recognitation
from train import Train
import subprocess
from attendance import Attendace

class Face_Recognition_System:

    # # ===========Function Buttons==========
    def student_details_btn(self):
        self.new_window = Toplevel(self.root)
        self.app = student(self.new_window)

    def train_date_btn(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def open_image_btn(self):
        subprocess.Popen(["open", 'data'])

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = face_recognitation(self.new_window)

    def attendance_date_btn(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendace(self.new_window)

    #===========Main Code============

    def __init__(self,root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recognition System")


        # First_Image
        img = Image.open("Software Image/B-1.png")
        img = img.resize((500,130),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        first_label =  Label(self.root,image = self.photoimg)
        first_label.place(x=0,y=0,width = 500, height = 130)

        # Second Image
        img1 = Image.open("Software Image/M-1.png")
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        first_label = Label(self.root, image=self.photoimg1)
        first_label.place(x=500, y=0, width=500, height=130)

        # Third_Image
        img2 = Image.open("Software Image/B-1.png")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        first_label = Label(self.root, image=self.photoimg2)
        first_label.place(x=1000, y=0, width=500, height=130)

        #Background Image

        img3 = Image.open("Software Image/Background.png")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_image = Label(self.root, image=self.photoimg3)
        bg_image.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_image,text = "DASHBOARD", font=("times new roman",35,"bold"),bg = "#B1E0B8",fg="#001C57")
        title_lbl.place(x=0,y=0,width = 1530 , height = 45 )



        #student_Image
        img4 = Image.open("Software Image/Btn-1.png")
        img4 = img4.resize((220, 220), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_image,image = self.photoimg4,command = self.student_details_btn,cursor="hand2")
        b1.place(x = 200,y=100,width=220,height=220)


        #Caption
        b1_1 = Button (bg_image, text = "STUDENTS DETAILS",command = self.student_details_btn,cursor="hand2", font=("times new roman",18,"bold"),bg = "#FAF9F6",fg="#571945")
        b1_1.place(x=200, y=320, width=220, height=40)



        # Face_detaction_Image
        img5 = Image.open("Software Image/Btn-2.png")
        img5 = img5.resize((220, 220), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_image, image=self.photoimg5, cursor="hand2",command = self.face_data)
        b1.place(x=500, y=100, width=220, height=220)

        # Caption
        b1_1 = Button(bg_image, text="FACE DETECTOR", cursor="hand2", font=("times new roman", 18, "bold"),command = self.face_data, bg="#FAF9F6",
                    fg="#571945")
        b1_1.place(x=500, y=320, width=220, height=40)



        # Attendence_Image
        img6 = Image.open("Software Image/Btn-3.png")
        img6 = img6.resize((220, 220), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_image, image=self.photoimg6, cursor="hand2",command =self.attendance_date_btn)
        b1.place(x=800, y=100, width=220, height=220)

        # Caption
        b1_1 = Button(bg_image, text="ATTENDANCE", cursor="hand2",command =self.attendance_date_btn,font=("times new roman", 18, "bold"), bg="#FAF9F6",
                    fg="#571945")
        b1_1.place(x=800, y=320, width=220, height=40)

        # Support_Image
        img7 = Image.open("Software Image/Btn-4.png")
        img7 = img7.resize((220, 220), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_image, image=self.photoimg7, cursor="hand2")
        b1.place(x=1100, y=100, width=220, height=220)

        # Caption
        b1_1 = Button(bg_image, text="SUPPORT", cursor="hand2", font=("times new roman", 18, "bold"), bg="#FAF9F6",
                    fg="#571945")
        b1_1.place(x=1100, y=320, width=220, height=40)

        # Train_Image
        img8 = Image.open("Software Image/Btn-5.png")
        img8 = img8.resize((220, 220), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_image, image=self.photoimg8, cursor="hand2",command = self.train_date_btn)
        b1.place(x=200, y=380, width=220, height=220)

        # Caption
        b1_1 = Button(bg_image, text="TRAIN DATA", cursor="hand2",command = self.train_date_btn, font=("times new roman", 18, "bold"), bg="#FAF9F6",
                    fg="#571945")
        b1_1.place(x=200, y=600, width=220, height=40)



        # Photos_Image
        img9 = Image.open("Software Image/Btn-6.png")
        img9 = img9.resize((220, 220), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_image, image=self.photoimg9, cursor="hand2",command = self.open_image_btn)
        b1.place(x=500, y=380, width=220, height=220)

        # Caption
        b1_1 = Button(bg_image, text="PHOTOS", cursor="hand2",command = self.open_image_btn,font=("times new roman", 18, "bold"), bg="#FAF9F6",
                    fg="#571945")
        b1_1.place(x=500, y=600, width=220, height=40)



        # Developer
        img10 = Image.open("Software Image/Btn-7.png")
        img10 = img10.resize((220, 220), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_image, image=self.photoimg10, cursor="hand2")
        b1.place(x=800,y=380, width=220, height=220)

        # Caption
        b1_1 = Button(bg_image, text="DEVELOPER", cursor="hand2", font=("times new roman", 18, "bold"), bg="#FAF9F6",
                    fg="#571945")
        b1_1.place(x=800, y=600, width=220, height=40)



        # Exits
        img11 = Image.open("Software Image/Btn-9.png")
        img11 = img11.resize((220, 220), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_image, image=self.photoimg11, cursor="hand2")
        b1.place(x=1100, y=380, width=220, height=220)

        # Caption
        b1_1 = Button(bg_image, text="EXIT", cursor="hand2", font=("times new roman", 18, "bold"), bg="#FAF9F6",
                    fg="#571945")
        b1_1.place(x=1100, y=600, width=220, height=40)




if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
