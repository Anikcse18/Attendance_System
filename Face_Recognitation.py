from tkinter import *
from tkinter import ttk, Label
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2                      #computer vison machine learning algorithm
from time import strftime
from datetime import datetime


class face_recognitation:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="Face Recognition",
                          font=("times new roman", 35, "bold"), bg="#E6EEEE", fg="#001C57")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        #Left_First Images
        top_img1 = Image.open("Software Image/facer1.1.png")
        top_img1 = top_img1.resize((500, 500), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(top_img1)

        first_label_1 = Label(self.root, image=self.photoimg1)
        first_label_1.place(x=500, y=100, width=500, height=500)


        #button

        b1_1 = Button(root,text="Face Recognition", cursor="hand2", font=("times new roman", 20, "bold"), bg="blue",command = self.face_recognization,
                      fg="#571945")

        b1_1.place(x=500, y=600, width=500, height=50)

        # Attendence Sheet

    def mark_attendence(self,n,i,d):
        with open("Attendacesheet.csv","r+",newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry=line.split((','))
                name_list.append(entry[0])
            if (i not in name_list) and (n not in name_list) and (d not in name_list):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%y")
                dtstring = now.strftime("%H:%M:%S")
                f.writelines(f"\n{n},{i},{d},{dtstring},{d1},present")






        #==========Face Recognization==============
    def face_recognization(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            coord = []
            for (x,y,w,h)in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict = clf.predict(gray_image[y:y+h,x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="110113@mysql",
                                                   database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("select Name from student where Student_Id=" +str(id))
                n = my_cursor.fetchone()
                n ="+".join(n)

                my_cursor.execute("select Student_Id from student where Student_Id=" + str(id))
                i = my_cursor.fetchone()

                i ="+".join(i)

                my_cursor.execute("select Dep from student where Student_Id=" + str(id))
                d = my_cursor.fetchone()

                d ="+".join(d)

                if confidence>77:

                    cv2.putText(img,f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img,f"Student Id:{i}",(x,y-55),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}", (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendence(n,i,d)

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 3)
                coord = [x,y,w,y]

            return coord
        def recognige(img,clf,faceCascade):
            coord = draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)
        while True:
            ret,img=video_cap.read()
            img = recognige(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognization",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()



if __name__ == "__main__":
    root = Tk()
    obj = face_recognitation(root)
    root.mainloop()
