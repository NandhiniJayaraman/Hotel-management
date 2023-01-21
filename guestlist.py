from tkinter import *
from PIL import Image ,ImageTk
from tkinter import ttk
import mysql.connector as mc
class guest():
    def __init__(self,root):
        self.root=root
        self.root.title('Welcome to GuestList')
        self.root.configure(background="white")
        self.root.geometry('750x600+70+70')
        self.root.resizable(False,False)
        
        img2=Image.open("c3.jpeg")
        img22=img2.resize((750,600),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img22)

        lbl2_img=Label(self.root,image=self.photoimg2)
        lbl2_img.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
        
        l=Label(self.root,text='WELCOME TO NANDHINI HOTEL',bg='black',fg='yellow',relief=RAISED,bd=3,font=('Franklin Gothic Medium',30,'bold'))
        l.place(x=0,y=0,width=750,height=40)
        
        def showlist():
            self.textarea.delete(1.0,END)
            self.textarea.insert(END,"Guest Name--\tGuest Mobile No")
            self.textarea.insert(END,"\n=====================================")
            dbc = mc.connect(host="localhost",user="root", password="",database="hotelmanage")
            c = dbc.cursor()
            c.execute("select name,phnno from client3")
            output=c.fetchall()
            for i in output:
                self.textarea.insert(END,f"\n {i}")
                self.textarea.insert(END,"\n===================================")
            dbc.close()
            self.details=self.textarea.get(1.0,END)
            f=open('guest.txt','w+')
            f.write('\n Show Avaliable Guest List \n')
            f.write(self.details)
            
        # button
        btn1=Button(self.root,text='Check Guest List',command=showlist,bg='green',fg='white',font=('Franklin Gothic Medium',19,'bold'))
        btn1.place(x=200,y=490,width=230,height=50)

        btn1=Button(self.root,text='Exit',command=self.root.destroy,bg='green',fg='white',font=('Franklin Gothic Medium',19,'bold'))
        btn1.place(x=500,y=490,width=230,height=50)
       
        # showing area
        RightLabelFrame=LabelFrame(self.root,text="Show Guest List",font=('Franklin Gothic Medium',19,'bold'),bg='yellow',fg='black')
        RightLabelFrame.place(x=100,y=100,width=500,height=350)

        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg='#F8F9F9',fg='black',font=('times new roman',15,'bold'))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)       



        root.mainloop()





if __name__ == '__main__':
    root=Tk()
    obj2=guest(root)
