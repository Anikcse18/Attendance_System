from tkinter import *
from tkinter import ttk, Label
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2                      #computer vison machine learning algorithm


class student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recognition System")


        #============Veriable================
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_yar = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_nid = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()




        # First_Image
        img = Image.open("/Users/istiakjaved/PycharmProjects/AdvanceAttendenceSystem/Software Image/St_Banner.png")
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        first_label = Label(self.root, image=self.photoimg)
        first_label.place(x=0, y=0, width=500, height=130)

        # Second Image
        img1 = Image.open("/Users/istiakjaved/PycharmProjects/AdvanceAttendenceSystem/Software Image/St_Banner_Middel.png")
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

        title_lbl = Label(bg_image, text="STUDENT MANAGEMENT SYSTEM",
                          font=("times new roman", 35, "bold"), bg="#B1E0B8", fg="#CB6CE6")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bg_image,bd=2)
        main_frame.place(x=0,y=42,width=1480,height = 790)


        # Left label Frame

        Left_frame = LabelFrame(main_frame,bd=2,bg="#B1E0B8",relief = RIDGE,text = "SignUp",font=("times new roman",12,"bold") )
        Left_frame.place(x=10,y=10,width=700,height=550)

        #Left_label_Image
        img_left = Image.open("/Users/istiakjaved/PycharmProjects/AdvanceAttendenceSystem/Software Image/Signup.png")
        img_left = img_left.resize((690, 130), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        first_label = Label(Left_frame, image=self.photoimg_left)
        first_label.place(x=5, y=0, width=690, height=130)

        # Current_Course
        current_course = LabelFrame(Left_frame,bd=2,bg="#B1E0B8",relief = RIDGE,text = "Current Course Info",font=("times new roman",12,"bold"))
        current_course.place(x=5,y=125,width=690,height=130)


        #Department
        dep_label = Label(current_course,text="Department",font=("times new roman",12,"bold"),bg = "#B1E0B8")
        dep_label.grid(row=0,column=0,padx=7,sticky=W)

        dep_combo = ttk.Combobox(current_course, textvariable = self.var_dep, font=("times new roman",12,"bold") ,state="readonly")

        dep_combo["values"] =("Select Department","CSE","ECE","EEE","Civil","ME","PME","BME")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=5,pady=13,sticky=W)

        #Course

        course_label = Label(current_course, text="Course", font=("times new roman", 12, "bold"), bg="#B1E0B8")
        course_label.grid(row=0, column=2, padx=7, sticky=W)

        course_label = ttk.Combobox(current_course, textvariable = self.var_course,font=("times new roman", 12, "bold"), state="readonly")

        course_label["values"] = ("Select Course", "Project and Thesis", "Embedded System", "Mobile Computing", "Neural Network", "Pattern Recognition", "Pattern Recognition", "Embedded System Lab")
        course_label.current(0)
        course_label.grid(row=0, column=3, padx=5, pady=13, sticky=W)


        # Year
        year_label = Label(current_course, text="Year", font=("times new roman", 12, "bold"), bg="#B1E0B8")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_label = ttk.Combobox(current_course,textvariable = self.var_yar, font=("times new roman", 12, "bold"), state="readonly")

        year_label["values"] = ("Select Year", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25", "2026-27","2027-29")
        year_label.current(0)
        year_label.grid(row=1, column=1, padx=5, pady=13, sticky=W)

        # Semester
        semester_label = Label(current_course, text="Semester", font=("times new roman", 12, "bold"), bg="#B1E0B8")
        semester_label.grid(row=1, column=2, padx=8, sticky=W)

        semester_label = ttk.Combobox(current_course, textvariable = self.var_semester, font=("times new roman", 12, "bold"), state="readonly")

        semester_label["values"] = ( "Select Semester","Spring","Fall")
        semester_label.current(0)
        semester_label.grid(row=1, column=3, padx=5, pady=13, sticky=W)

        # Studen Information
        class_student_info = LabelFrame(Left_frame, bd=2, bg="#B1E0B8", relief=RIDGE, text="Student Information",
                                    font=("times new roman", 12, "bold"))
        class_student_info.place(x=5, y=255, width=690, height=275)

        #StudenId

        StudentId_label = Label(class_student_info, text="Student ID:", font=("times new roman", 13, "bold"), bg="#B1E0B8")
        StudentId_label.grid(row=0, column=0, padx=6, pady=4,sticky=W)

        studentId_entry =ttk.Entry(class_student_info,textvariable = self.var_std_id, width = 20, font=("times new roman", 13, "bold"))
        studentId_entry.grid(row=0,column=1,padx=6,pady=4, sticky=W)

        #studentName

        StudentName_label = Label(class_student_info, text="Student Name:", font=("times new roman", 13, "bold"), bg="#B1E0B8")
        StudentName_label.grid(row=0, column=2, padx=6,pady=4,sticky=W)

        StudentName_entry = ttk.Entry(class_student_info,textvariable = self.var_std_name, width=20, font=("times new roman", 13, "bold"))
        StudentName_entry.grid(row=0,column=3,padx=6, pady=4, sticky=W)

        #Class division
        class_div_label = Label(class_student_info, text="Class Section:", font=("times new roman", 13, "bold"),
                                  bg="#B1E0B8")
        class_div_label.grid(row=1, column=0, padx=6, pady=4, sticky=W)


        Div_label = ttk.Combobox(class_student_info, textvariable=self.var_div,
                                    font=("times new roman", 12, "bold"),state="readonly",width=22)

        Div_label["values"] = ("Select Section","A", "B", "Other")
        Div_label.current(0)
        Div_label.grid(row=1, column=1, padx=6, pady=4, sticky=W)

        # NID Number
        nid_num_label = Label(class_student_info, text="NID Number:", font=("times new roman", 13, "bold"),
                                bg="#B1E0B8")
        nid_num_label.grid(row=1, column=2, padx=6, pady=4, sticky=W)

        nid_num_entry = ttk.Entry(class_student_info,textvariable = self.var_nid, width=20, font=("times new roman", 13, "bold"))
        nid_num_entry.grid(row=1, column=3, padx=6, pady=4, sticky=W)

        # Gender

        gender_label = Label(class_student_info, text="Gender:", font=("times new roman", 13, "bold"),
                             bg="#B1E0B8")
        gender_label.grid(row=2, column=0, padx=6, pady=4, sticky=W)


        gender_label = ttk.Combobox(class_student_info, textvariable=self.var_gender, font=("times new roman", 12, "bold"),
                                  state="readonly",width = 22)

        gender_label["values"] = ("Male", "Female", "Other")
        gender_label.current(0)
        gender_label.grid(row=2, column=1, padx=6, pady=4, sticky=W)


        # DoB

        dob_lavel = Label(class_student_info, text="DOB:", font=("times new roman", 13, "bold"),
                             bg="#B1E0B8")
        dob_lavel.grid(row=2, column=2, padx=6, pady=4, sticky=W)

        dob_entry = ttk.Entry(class_student_info,textvariable = self.var_dob, width=20, font=("times new roman", 13, "bold"))
        dob_entry.grid(row=2, column=3, padx=6, pady=4, sticky=W)


        #Address
        address_label = Label(class_student_info, text="Address:", font=("times new roman", 13, "bold"),
                             bg="#B1E0B8")
        address_label.grid(row=4, column=0, padx=6, pady=4, sticky=W)
        address_entry = ttk.Entry(class_student_info,textvariable = self.var_address, width=20, font=("times new roman", 13, "bold"))
        address_entry.grid(row=4, column=1, padx=6, pady=4, sticky=W)

        # TeacherName
        teacher_name_label = Label(class_student_info, text="Teacher Name:", font=("times new roman", 13, "bold"),
                              bg="#B1E0B8")
        teacher_name_label.grid(row=4, column=2, padx=6, pady=4, sticky=W)
        teacher_name_entry = ttk.Entry(class_student_info,textvariable = self.var_teacher, width=20, font=("times new roman", 13, "bold"))
        teacher_name_entry.grid(row=4, column=3, padx=6, pady=4, sticky=W)

        #Email
        email_label = Label(class_student_info, text="Email:", font=("times new roman", 13, "bold"),
                              bg="#B1E0B8")
        email_label.grid(row=3, column=0, padx=6, pady=4, sticky=W)

        email_entry = ttk.Entry(class_student_info,textvariable = self.var_email, width=20, font=("times new roman", 13, "bold"))
        email_entry.grid(row=3, column=1, padx=6, pady=4, sticky=W)


        # Phone Number
        gender_label = Label(class_student_info, text="Phone No:", font=("times new roman", 13, "bold"),
                             bg="#B1E0B8")
        gender_label.grid(row=3, column=2, padx=6, pady=4, sticky=W)
        gender_entry = ttk.Entry(class_student_info,textvariable = self.var_phone, width=20, font=("times new roman", 13, "bold"))
        gender_entry.grid(row=3, column=3, padx=6, pady=4, sticky=W)



 #=========Radio Button=============>
        #radioButtons_Photo Sample_YES

        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_info,variable = self.var_radio1,text="Take Photo Sample",value = "Yes")
        radiobtn1.grid(row=6,column=0)

        # radioButtons_Photo Sample_No

        radiobtn2 = ttk.Radiobutton(class_student_info,variable = self.var_radio1, text="No Photo Sample", value="No")
        radiobtn2.grid(row=6, column=1)





        #btn frame TakeUpdate photo
        btn_frame = Frame(class_student_info, bd=2, bg="#B1E0B8", relief=RIDGE)
        btn_frame.place(x=0, y=193, width=686, height=30)


        # buttonframe

        save_btn = Button(btn_frame,text="Save",command = self.add_deta, width=19,bg="red",fg="Black",font=("times new roman", 13, "bold"))
        save_btn.grid(row=0,column=0,padx=1)

        update_btn = Button(btn_frame, text="Update",command = self.update_data, width=19, bg="red", fg="Black", font=("times new roman", 13, "bold"))
        update_btn.grid(row=0, column=1,padx=1)

        delete_btn = Button(btn_frame, text="Delete",command = self.delete_data, width=19, bg="red", fg="Black", font=("times new roman", 13, "bold"))
        delete_btn.grid(row=0, column=2,padx=1)

        reset_btn = Button(btn_frame, text="Reset",command = self.reset_data, width=19, bg="red", fg="Black", font=("times new roman", 13, "bold"))
        reset_btn.grid(row=0, column=3,padx=1)

        # btn frame TakeUpdate photo
        btn_frame1 = Frame(class_student_info, bd=2, bg="#B1E0B8", relief=RIDGE)
        btn_frame1.place(x=0, y=223, width=686, height=30)




        # #Photo Button Take

        take_photo_btn = Button(btn_frame1,command = self.generate_dataset, text="Take photo Sample", width=43, bg="Red", fg="Red",
                           font=("times new roman", 13, "bold"))
        take_photo_btn.grid(row=1, column=0,padx=3)



        update_photo_btn = Button(btn_frame1, text="Update photo Sample", width=43, bg="Red", fg="Green",
                                font=("times new roman", 13, "bold"))
        update_photo_btn.grid(row=1, column=1,padx=3)






        # Right label Frame

        Right_frame = LabelFrame(main_frame,bd=2,bg="#B1E0B8",relief = RIDGE,text = "Student Details",font=("times new roman",12,"bold") )
        Right_frame.place(x=725,y=10,width=700,height=550)

        img_right = Image.open("/Users/istiakjaved/PycharmProjects/AdvanceAttendenceSystem/Software Image/Details.png")
        img_right = img_right.resize((690, 130), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        first_label = Label(Right_frame, image=self.photoimg_right)
        first_label.place(x=5, y=0, width=690, height=130)


        # ---------Search Systems Frame---------

        search_frame_info = LabelFrame(Right_frame, bd=2, bg="#B1E0B8", relief=RIDGE, text="Search",
                                        font=("times new roman", 12, "bold"))
        search_frame_info.place(x=5, y=125, width=690, height=70)


        # search label
        search_label1 = Label(search_frame_info, text="Search By:", font=("times new roman", 14, "bold"),
                             bg="#B1E0B8")
        search_label1.grid(row=0, column=0, padx=2, pady=8, sticky=W)

        search_label = ttk.Combobox(search_frame_info, font=("times new roman", 12, "bold"), state="readonly")

        search_label["values"] = ("Select", "Roll", "Phone Number")
        search_label.current(0)
        search_label.grid(row=0, column=1, padx=10, pady=8, sticky=W)

        search_entry = ttk.Entry(search_frame_info, width=20, font=("times new roman", 13, "bold"))
        search_entry.grid(row=0, column=2, padx=6, pady=4, sticky=W)


        search_btn = Button(search_frame_info, text="Search", width=12, bg="red", fg="Black",
                            font=("times new roman", 13, "bold"))
        search_btn.grid(row=0, column=3,padx=5)

        ShowAll_btn = Button(search_frame_info, text="Show All", width=12, bg="red", fg="Black",
                           font=("times new roman", 13, "bold"))
        ShowAll_btn.grid(row=0, column=4,padx=5)



        # -------Table Frame--------

        table_frame = Frame(Right_frame, bd=2, bg="#B1E0B8", relief=RIDGE)
        table_frame.place(x=5, y=198, width=690, height=330)

        scroll_x = ttk.Scrollbar(table_frame,orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)



        # scrollBarsection

        self.student_table = ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","nid","gender","dob","email","phone","address","teacher","photo"),xscrollcommand = scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side = RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)



        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student Id")
        self.student_table.heading("name", text="Name")

        self.student_table.heading("nid", text="Nid")
        self.student_table.heading("gender", text="Gender")

        self.student_table.heading("div", text="Division")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="Photo Status")
        self.student_table["show"] = "headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=150)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("nid", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=150)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=150)
        self.student_table.column("photo", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_Cursor)
        self.featch_data()


    #=========Function delceration=============

    def add_deta(self):
        if self.var_dep.get() == "Select Department" or self.var_yar =="Select Year" or self.var_course == "Select course" or self.var_std_name.get() == "" or self.var_std_id.get()=="" or self.var_nid.get()=="" or self.var_phone.get() =="":
            messagebox.showerror("Error","Opps! \n All fields are required",parent = self.root)
        else:
            try:
                 conn = mysql.connector.connect(host="localhost",username="root",password="110113@mysql",database="face_recognizer")
                 my_cursor = conn.cursor()
                 my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                     self.var_dep.get(),
                                     self.var_course.get(),
                                     self.var_yar.get(),
                                     self.var_semester.get(),
                                     self.var_std_id.get(),
                                     self.var_std_name.get(),
                                     self.var_div.get(),
                                     self.var_nid.get(),
                                     self.var_gender.get(),
                                     self.var_dob.get(),
                                     self.var_email.get(),
                                     self.var_phone.get(),
                                     self.var_address.get(),
                                     self.var_teacher.get(),
                                     self.var_radio1.get()
                                 ))
                 conn.commit()
                 self.featch_data()
                 conn.close()
                 messagebox.showinfo("Success","Congratulations \n Student Details Has Been Added Successfully",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


    # =============Featch data (Student Tables)=================

    def featch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="110113@mysql",
                                       database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #==================Get Data ==================
    def get_Cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_yar.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_nid.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    #===========Update Function=======

    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_yar == "Select Year" or self.var_course == "Select course" or self.var_std_name.get() == "" or self.var_std_id.get() == "" or self.var_nid.get() == "" or self.var_phone.get() == "":
            messagebox.showerror("Error", "Opps! \n All fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update","Attention! \n Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="110113@mysql",database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Nid=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s, Address=%s,Teacher=%s,Photosample=%s where Student_Id=%s",(

                                    self.var_dep.get(),
                                    self.var_course.get(),
                                    self.var_yar.get(),
                                    self.var_semester.get(),
                                    self.var_std_name.get(),
                                    self.var_div.get(),
                                    self.var_nid.get(),
                                    self.var_gender.get(),
                                    self.var_dob.get(),
                                    self.var_email.get(),
                                    self.var_phone.get(),
                                    self.var_address.get(),
                                    self.var_teacher.get(),
                                    self.var_radio1.get(),
                                    self.var_std_id.get()
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Done\nSuccessfully Updated",parent = self.root)
                conn.commit()
                self.featch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent = self.root)


    #============= Delet Function==============

    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student Id Must Be Requried",parent = self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page","Do you want to delete this student?",parent = self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="110113@mysql",
                                                   database="face_recognizer")
                    my_cursor = conn.cursor()

                    sql="delete from student where Student_Id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.featch_data()
                conn.close()
                messagebox.showinfo("Delete","Congratulations \n Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent = self.root)


    #=================Reset Function=========================
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_yar.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set("Select Section"),
        self.var_nid.set(""),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")




    # =============Gemnerate Photo Sampla=======================
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_yar == "Select Year" or self.var_course == "Select course" or self.var_std_name.get() == "" or self.var_std_id.get() == "" or self.var_nid.get() == "" or self.var_phone.get() == "":
            messagebox.showerror("Error", "Opps! \n All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="110113@mysql",
                                               database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id +=1
                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Nid=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s, Address=%s,Teacher=%s,Photosample=%s where Student_Id=%s",(

                                            self.var_dep.get(),
                                            self.var_course.get(),
                                            self.var_yar.get(),
                                            self.var_semester.get(),
                                            self.var_std_name.get(),
                                            self.var_div.get(),
                                            self.var_nid.get(),
                                            self.var_gender.get(),
                                            self.var_dob.get(),
                                            self.var_email.get(),
                                            self.var_phone.get(),
                                            self.var_address.get(),
                                            self.var_teacher.get(),
                                            self.var_radio1.get(),
                                            self.var_std_id.get()==id+1
                    ))
                conn.commit()
                self.featch_data()
                self.reset_data()
                conn.close()

                #==============Load imgae redefine data on face frontal from open cv=====

                face_classifier = cv2.CascadeClassifier("/Users/istiakjaved/PycharmProjects/AdvanceAttendenceSystem/haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #ScallingFactor = 1.3
                    #Minimum Neighbor = 5
                    for (x,y,w,h) in faces:
                        face_cropped = img[y:y+h,x:x+w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret,my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id +=1
                        face = cv2.resize(face_cropped(my_frame),(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path = "/Users/istiakjaved/PycharmProjects/AdvanceAttendenceSystem/data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Croped Face",face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()

                messagebox.showinfo("Result","Successfully data sets complet !")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent = self.root)


if __name__ == "__main__":
    root = Tk()
    obj = student(root)
    root.mainloop()

