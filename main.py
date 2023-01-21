from tkinter import *
from PIL import Image ,ImageTk
from checkinn import checkin
from guestlist import guest
from checkout import checkout1
from searchlist import search
class HOTEL_MANAGEMENT:
    def __init__(self,root):
        self.root=root
        self.root.geometry("963x749+0+0")
        self.root.title("HOTEL MANAGEMENT")
        self.root.configure(background="white")
        self.root.resizable(False,False)

        def click():
            t2=Toplevel(self.root)
            obj1=checkin(t2)
        def guest1():
            t3=Toplevel(self.root)
            obj2=guest(t3)
        def check1():
            t4=Toplevel(self.root)
            obj3=checkout1(t4)
        def search1():
            t5=Toplevel(self.root)
            obj4=search(t5)
            
        

        # MAIN FRAME FOR ROOT===========================
        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
        self.Frame1.configure(relief=RAISED)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(background="white")
        self.Frame1.configure(width=925)
        # image label
        img=Image.open("bgh.jpg")
        img=img.resize((1313,650),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        lbl_img=Label(self.Frame1,image=self.photoimg)
        lbl_img.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)

        self.lbl1 = Label(self.Frame1,text='WELCOME',bg='#9CA7F8',fg='black',font=('arial',35,'bold'))
        self.lbl1.place(x=330, y=40, height=50, width=250)
        # button 
        self.Button2 = Button(self.Frame1,text='1.CHECK INN',command=click,font=('times',30,'bold'),bg='#9EA6DC',fg='black')
        self.Button2.place(relx=0.18, rely=0.17, height=70, width=566)
    

        self.Button3 = Button(self.Frame1)
        self.Button3 = Button(self.Frame1,text='2.SHOW GUEST LIST',command=guest1,font=('times',30,'bold'),bg='#9EA6DC',fg='black')
        self.Button3.place(relx=0.18, rely=0.33, height=70, width=566)


        self.Button4 = Button(self.Frame1)
        self.Button4 = Button(self.Frame1,text='3.CHECK OUT',command=check1,font=('times',30,'bold'),bg='#9EA6DC',fg='black')
        self.Button4.place(relx=0.18, rely=0.47, height=70, width=566)

        self.Button5 = Button(self.Frame1)
        self.Button5 = Button(self.Frame1,text='4.GET INFO OF ANY GUEST',command=search1,font=('times',30,'bold'),bg='#9EA6DC',fg='black')
        self.Button5.place(relx=0.18, rely=0.61, height=70, width=566)

        self.Button6 = Button(self.Frame1)
        self.Button6 = Button(self.Frame1,text='5.EXIT',command=root.destroy,font=('times',30,'bold'),bg='#9EA6DC',fg='black')
        self.Button6.place(relx=0.18, rely=0.77, height=70, width=566)
        root.mainloop()


if __name__ == '__main__':
    root=Tk()
    GUEST=HOTEL_MANAGEMENT(root)



