from tkinter import *
from PIL import Image ,ImageTk
from tkinter import ttk
import mysql.connector as mc
from tkinter import messagebox
class checkout1():
    def __init__(self,root):
        self.root1=root
        self.root1.title('Welcome to CheckOut')
        self.root1.configure(background="white")
        self.root1.geometry('750x600+70+70')
        self.root1.resizable(False,False)
        self.name=StringVar()
        
        img3=Image.open("search.jpg")
        img11=img3.resize((750,600),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img11)

        lbl3_img=Label(self.root1,image=self.photoimg3)
        lbl3_img.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
        
        l1=Label(self.root1,text='WELCOME TO NANDHINI HOTEL',bg='black',fg='yellow',relief=RAISED,font=('Franklin Gothic Medium',30,'bold'))
        l1.place(x=0,y=0,width=750,height=40)
        
        def out():
            dbc = mc.connect(host="localhost",user="root", password="",database="hotelmanage")
            c = dbc.cursor()
            i_name=self.name.get()
            c.execute("select name from client3")
            output=c.fetchall()
            c.execute("delete from client3 where name='"+i_name+"'")                
            messagebox.showinfo(' Thank You ',self.name.get()+ ' Return Back ',parent=self.root1)
            #elif output != i_name:
            # messagebox.showerror('OOPS', self.name.get()+ '  Invalid Guest ')
            dbc.commit()
            #dbc.close()  
    
        # button
        l=Label(self.root1,text='WELCOME TO NANDHINI HOTEL',bg='black',fg='yellow',relief=RAISED,font=('Franklin Gothic Medium',30,'bold'))
        l.place(x=0,y=0,width=750,height=40)
        
        l1=Label(self.root1,text='Enter Customer Name',bg='white',fg='black',font=('times new roman',15,'bold'))
        l1.place(x=250,y=320,width=200,height=45)
        
        e1=Entry(self.root1,bg='white',fg='black',textvariable=self.name,font=('times new roman',15,'bold'))
        e1.place(x=500,y=320,width=200,height=45)
        
        btn1=Button(self.root1,text='Check OUT',command=out,bg='red',fg='white',font=('times new roman',15,'bold'))
        btn1.place(x=300,y=390,width=190,height=50)

        btn1=Button(self.root1,text='Exit',command=self.root1.destroy,bg='red',fg='white',font=('times new roman',15,'bold'))
        btn1.place(x=500,y=390,width=190,height=50)
       

        root.mainloop()





if __name__ == '__main__':
    root=Tk()
    obj3=checkout1(root)
