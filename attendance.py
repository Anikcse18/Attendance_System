from tkinter import *
from tkinter import ttk, Label
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2  #computer vison machine learning algorithm
from tkinter import filedialog
import csv
import os


mydata=[]
class Attendace:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recognition System")

        # First_Image
        img = Image.open("/Users/istiakjaved/PycharmProjects/AdvanceAttendenceSystem/Software Image/St_Banner.png")
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        first_label = Label(self.root, image=self.photoimg)
        first_label.place(x=0, y=0, width=500, height=130)

        # Second Image
        img1 = Image.open(
            "/Users/istiakjaved/PycharmProjects/AdvanceAttendenceSystem/Software Image/St_Banner_Middel.png")
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        first_label = Label(self.root, image=self.photoimg1)
        first_label.place(x=500, y=0, width=500, height=130)

        # Third_Image
        img2 = Image.open("/Users/istiakjaved/PycharmProjects/AdvanceAttendenceSystem/Software Image/St_Banner.png")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        first_label = Label(self.root, image=self.photoimg2)
        first_label.place(x=1000, y=0, width=500, height=130)

        # Background Image

        img3 = Image.open("/Users/istiakjaved/PycharmProjects/AdvanceAttendenceSystem/Software Image/St_Background.jpg")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_image = Label(self.root, image=self.photoimg3)
        bg_image.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_image, text="Attendance Dashoboard",
                          font=("times new roman", 35, "bold"), bg="#B1E0B8", fg="#CB6CE6")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bg_image, bd=2,bg="#B1E0B8")
        main_frame.place(x=0, y=42, width=1480, height=790)



        # Left label Frame

        Left_frame = LabelFrame(main_frame, bd=2, bg="#B1E0B8", relief=RIDGE, text="Attendance Details",
                                font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=700, height=550)

        img_left = Image.open("Software Image/att-Details.png")
        img_left = img_left.resize((690, 130), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        first_label = Label(Left_frame, image=self.photoimg_left)
        first_label.place(x=5, y=0, width=690, height=130)


        #inside left frame

        left_inside_frame = Frame(Left_frame, bd=2, bg="#B1E0B8")
        left_inside_frame.place(x=0, y=130, width=695, height=400)

        #Attendence _ ID
        AttendanceId_label = Label(left_inside_frame, text="Attendance ID:", font=("times new roman", 13, "bold"),
                                bg="#B1E0B8")

        AttendanceId_label.grid(row=0, column=0, padx=6, pady=4, sticky=W)

        AttendanceId__entry = ttk.Entry(left_inside_frame, width=20,
                                    font=("times new roman", 13, "bold"))
        AttendanceId__entry.grid(row=0, column=1, padx=6, pady=4, sticky=W)

        #Roll
        Roll_label = Label(left_inside_frame, text="Roll:", font=("times new roman", 13, "bold"),
                                   bg="#B1E0B8")
        Roll_label.grid(row=0, column=2, padx=6, pady=4)

        Roll_entry = ttk.Entry(left_inside_frame, width=20,
                                        font=("times new roman", 13, "bold"))
        Roll_entry.grid(row=0, column=3, pady=4)



        #attendance Name

        attendanceName_label = Label(left_inside_frame, text="Name:", font=("times new roman", 13, "bold"),
                                  bg="#B1E0B8")
        attendanceName_label.grid(row=1, column=0, padx=6, pady=4, sticky=W)

        attendanceName_entry = ttk.Entry(left_inside_frame, width=20,
                                      font=("times new roman", 13, "bold"))
        attendanceName_entry.grid(row=1, column=1, padx=6, pady=4)

        # dept Name

        Dept_label = Label(left_inside_frame, text="Department:", font=("times new roman", 13, "bold"),
                                     bg="#B1E0B8")
        Dept_label.grid(row=1, column=2)

        Dept_entry = ttk.Entry(left_inside_frame, width=20,
                                         font=("times new roman", 13, "bold"))
        Dept_entry.grid(row=1, column=3, pady=4)

        # time

        time_label = Label(left_inside_frame, text="Time:", font=("times new roman", 13, "bold"),
                           bg="#B1E0B8")
        time_label.grid(row=2, column=0,padx = 6, pady=4)

        time_entry = ttk.Entry(left_inside_frame, width=20,
                               font=("times new roman", 13, "bold"))
        time_entry.grid(row=2, column=1,  padx = 6, pady=4)

        # Date

        Date_label = Label(left_inside_frame, text="Date:", font=("times new roman", 13, "bold"),
                           bg="#B1E0B8")
        Date_label.grid(row=2, column=2)

        Date_entry = ttk.Entry(left_inside_frame, width=20,
                               font=("times new roman", 13, "bold"))
        Date_entry.grid(row=2, column=3, padx=3)


        #Attendance

        attendance_Status_label = Label(left_inside_frame, text="Status: ", font=("times new roman", 12, "bold"), bg="#B1E0B8")
        attendance_Status_label.grid(row=3, column=0, padx=8, sticky=W)

        attendance_Status_label = ttk.Combobox(left_inside_frame,
                                      font=("times new roman", 12, "bold"), state="readonly")

        attendance_Status_label["values"] = ("Select Status", "Present", "Absent")
        attendance_Status_label.current(0)
        attendance_Status_label.grid(row=3, column=1, padx=8, pady=13)

        # buttonframe
        btn_frame = Frame(left_inside_frame, bd=2, bg="#B1E0B8", relief=RIDGE)
        btn_frame.place(x=0, y=350, width=686, height=30)

        import_btn = Button(btn_frame, text="Import CSV", command = self.importCSv,width=19, bg="red", fg="Black",
                          font=("times new roman", 13, "bold"))
        import_btn.grid(row=0, column=0, padx=1)

        Export_btn = Button(btn_frame, text="Export CSV", width=19, bg="red", fg="Black",
                            font=("times new roman", 13, "bold"))
        Export_btn.grid(row=0, column=1, padx=1)

        update_btn = Button(btn_frame, text="Update", width=19, bg="red", fg="Black",
                            font=("times new roman", 13, "bold"))
        update_btn.grid(row=0, column=2, padx=1)

        reset_btn = Button(btn_frame, text="Reset",  width=19, bg="red", fg="Black",
                           font=("times new roman", 13, "bold"))
        reset_btn.grid(row=0, column=3, padx=1)




        # Right label Frame

        Right_frame = LabelFrame(main_frame, bd=2, bg="#B1E0B8", relief=RIDGE, text="Student Details",
                                 font=("times new roman", 12, "bold"))
        Right_frame.place(x=725, y=10, width=700, height=550)

        # Table left frame

        Table_inside_frame = Frame(Right_frame, bd=2, bg="#B1E0B8")
        Table_inside_frame.place(x=5, y=5, width=690, height=400)

        #======Scroll BAr=======
        scroll_x = ttk.Scrollbar(Table_inside_frame,orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_inside_frame, orient=VERTICAL)
        self.Attendancetable = ttk.Treeview(Table_inside_frame,colum = ("ID","ROLL","NAME","DEPARTMENT","TIME","DATE","Attendance_Status"),xscrollcommand = scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command = self.Attendancetable.xview)
        scroll_y.config(command = self.Attendancetable.yview)

        self.Attendancetable.heading("ID",text = "Attendance ID")
        self.Attendancetable.heading("ROLL", text="Roll")

        self.Attendancetable.heading("NAME", text="Name")
        self.Attendancetable.heading("DEPARTMENT", text="Department")

        self.Attendancetable.heading("TIME", text="Time")
        self.Attendancetable.heading("DATE", text="Date")
        self.Attendancetable.heading("Attendance_Status",text = "Attendance Status")

        self.Attendancetable["show"] = "headings"

        self.Attendancetable.column("ID", width=100)
        self.Attendancetable.column("ROLL", width=100)
        self.Attendancetable.column("DEPARTMENT", width=100)
        self.Attendancetable.column("NAME", width=100)
        self.Attendancetable.column("TIME", width=100)
        self.Attendancetable.column("DATE", width=100)
        self.Attendancetable.column("Attendance_Status", width=100)


        self.Attendancetable.pack(fill=BOTH,expand = 1)


    #===========Featch data
    def featch_data(self,rows):
        self.Attendancetable.delete(*self.Attendancetable.get_children())
        for i in rows:
            self.Attendancetable.insert(" ",END,values=1)

    def importCSv(self):
        global mydata
        fln = filedialog.askopenfilename(initialdir = os.getcwd(), title = "Open CSV", filetypes = (("CSV File","*.csv"),("ALL File","*.*")),parent = self.root )
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.featch_data(mydata)

















if __name__ == "__main__":
    root = Tk()
    obj = Attendace(root)
    root.mainloop()