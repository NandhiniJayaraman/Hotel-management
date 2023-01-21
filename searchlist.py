from tkinter import *
from PIL import Image ,ImageTk
from tkinter import ttk
import mysql.connector as mc
from tkinter import messagebox
class search():
    def __init__(self,root):
        self.root=root
        self.root.title('Welcome to Search Guest List')
        self.root.configure(background="white")
        self.root.geometry('750x600+70+70')
        self.root.resizable(False,False)
        self.name1=StringVar()
        
        
        img4=Image.open("search1.jpg")
        img41=img4.resize((750,600),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img41)

        lbl4_img=Label(self.root,image=self.photoimg4)
        lbl4_img.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
        
        def search():
            self.textarea.delete(1.0,END)
            self.textarea.insert(END,"Guest Name-\tGuest Mobile No-\tRoom Type-\tTotal Rent")
            self.textarea.insert(END,"\n===========================================")
            dbc = mc.connect(host="localhost",user="root", password="",database="hotelmanage")
            c = dbc.cursor()
            s_name=self.name1.get()
            c.execute("select name,phnno,roomtype,totalrent from client3 where name='"+s_name+"'")
            output=c.fetchall()
            for i in output:
                self.textarea.insert(END,f"\n{i}")
            dbc.close()
        # button

        l1=Label(self.root,text='Enter Customer Name',bg='#F39C12',fg='black',font=('Franklin Gothic Medium',19,'bold'))
        l1.place(x=110,y=140,width=260,height=45)
        
        e1=Entry(self.root,bg='#F39C12',fg='black',textvariable=self.name1,font=('Franklin Gothic Medium',19,'bold'))
        e1.place(x=390,y=140,width=260,height=45)
        
        btn1=Button(self.root,text='Search Guest',command=search,bg='green',fg='white',font=('Franklin Gothic Medium',15,'bold'))
        btn1.place(x=150,y=490,width=190,height=50)

        btn1=Button(self.root,text='Exit',command=self.root.destroy,bg='green',fg='white',font=('Franklin Gothic Medium',15,'bold'))
        btn1.place(x=350,y=490,width=190,height=50)

        # showing area
        RightLabelFrame=LabelFrame(self.root,text="Search Guest List",font=('Franklin Gothic Medium',19,'bold'),bg='white',fg='black')
        RightLabelFrame.place(x=100,y=230,width=550,height=150)

        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg='#45F3E6',fg='black',font=('Franklin Gothic Medium',15,'bold'))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)
       

        root.mainloop()





if __name__ == '__main__':
    root=Tk()
    obj4=search(root)
