from tkinter import *
from PIL import Image ,ImageTk
from tkinter import ttk
import mysql.connector as mc
from tkinter import messagebox
class checkin:
    def __init__(self,root):
        self.root=root
        self.root.title('Welcome to Check-inn page')
        self.root.configure(background="white")
        self.root.geometry('1313x650+0+0')
        self.root.resizable(False,False)
        self.total_amount=0
        self.total1_amount=StringVar()
        #database variable
        self.e_name =StringVar()
        self.e_phn=StringVar()
        self.e_email =StringVar()
        self.e_roomtype =StringVar()
        self.e_rent =StringVar()
        self.e_paytype =StringVar()
        self.e_days=StringVar()
        self.e_totalrent=StringVar()
        
        self.cus_name=StringVar()
        self.cus_mblno=StringVar()
        self.cus_email=StringVar()
        self.cus_nodays=StringVar()
        self.rooms_rate=StringVar()
        var=StringVar()
        var1=StringVar()
        var2=StringVar()
        self.rate=StringVar()
        total=StringVar()
        self.py=StringVar()
        
        
        self.rooms=['General','Delux','Full Delux','Joint']
        self.rooms_rate=['2000','3000','4000','5000']
        self.pay=['By Cash','By Credit/Debit Card']
        
        # MAIN FRAME FOR ROOT===========================
        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
        self.Frame1.configure(relief=RAISED)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(background="white")
        self.Frame1.configure(width=925)
        # image label
        img1=Image.open("checkin1.jpg")
        img1=img1.resize((1313,650),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lbl1_img=Label(self.Frame1,image=self.photoimg1)
        lbl1_img.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)

        l1=Label(self.root,text='WELCOME TO NANDHINI HOTEL',bg='black',fg='yellow',relief=RAISED,font=('Franklin Gothic Medium',30,'bold'))
        l1.place(x=0,y=0,width=1313,height=40)
        
        def submit():
            self.textarea.delete(1.0,END)
            self.total_amount=(str(int(self.e4.get())*int(self.e6.get())))
            self.textarea.insert(END,"\t Welcome to Hotel")
            self.textarea.insert(END,f"\nCustomer Name:{self.e1.get()}")
            self.textarea.insert(END,f"\nCustomer Number:{self.e3.get()}")
            self.textarea.insert(END,f"\nCustomer Email:{self.e2.get()}")
            self.textarea.insert(END,f"\nCustomer RoomType:{self.e5.get()}")
            self.textarea.insert(END,f"\n Per day Room Rent:{self.e6.get()}")
            self.textarea.insert(END,f"\n PaymentType:{self.e7.get()}")
            self.textarea.insert(END,f"\n How many Days Stay:{self.e4.get()}")
            self.textarea.insert(END,f"\nCustomer Total rent:{self.total_amount}")
            self.textarea.insert(END,"\n====================================")
            self.textarea.insert(END,"\n Thankyou for ur Booking")
            self.textarea.insert(END,"\n==================================")

            self.bill_data=self.textarea.get(1.0,END)
            f1=open("bill.txt",'w+')
            f1.write(self.bill_data)
            f1.close()
            
            
            self.e_name =self.e1.get()
            self.e_phn=self.e3.get()
            self.e_email =self.e2.get()
            self.e_roomtype =self.e5.get()
            self.e_rent =self.e6.get()
            self.e_paytype =self.e7.get()
            self.e_days=self.e4.get()
            self.e_totalrent=self.total_amount
            dbc = mc.connect(host="localhost",user="root", password="",database="hotelmanage")
            c = dbc.cursor()
            c.execute("insert into client3(name,phnno,email,roomtype,rent,paytype,days,totalrent) values('"+self.e_name+"', '"+self.e_phn+"', '"+self.e_email+"', '"+self.e_roomtype+"', '"+self.e_rent+"', '"+self.e_paytype+"', '"+self.e_days+"', '"+self.e_totalrent+"')")
            dbc.close()
            
        def clear():
            self.textarea.delete(1.0,END)
            self.cus_name.set("")
            self.cus_mblno.set("")
            self.cus_email.set("")
            self.total_amount=0
            var2.set('')
            submit()
        #def out():
         #   obj5=thankyou1(root)
            
            
            
        
            
            
            

        
        # customer Frame
        cust_Frame=LabelFrame(self.Frame1,text="Customer Details",font=('times new roman',17,'bold'),bg='#5DADE2',fg='black')
        cust_Frame.place(x=25,y=290,width=450,height=310)

        self.l1=Label(cust_Frame,text='Enter Name',bg='#5DADE2',fg='black',font=('times',15,'bold'))
        self.l1.grid(row=0,column=2)

        self.e1=Entry(cust_Frame,bg='white',textvariable=self.cus_name,fg='black',font=('times',15,'bold'))
        self.e1.grid(row=0,column=6)
        
        self.l2=Label(cust_Frame,text='Enter Email',bg='#5DADE2',fg='black',font=('times',15,'bold'))
        self.l2.grid(row=2,column=2)

        self.e2=Entry(cust_Frame,bg='white',textvariable=self.cus_email,fg='black',font=('times',15,'bold'))
        self.e2.grid(row=2,column=6)
        
        self.l3=Label(cust_Frame,text='Enter Number',bg='#5DADE2',fg='black',font=('times',15,'bold'))
        self.l3.grid(row=3,column=2)

        self.e3=Entry(cust_Frame,bg='white',textvariable=self.cus_mblno,fg='black',font=('times',15,'bold'))
        self.e3.grid(row=3,column=6)
        
        self.l4=Label(cust_Frame,text='Enter No.of Days',bg='#5DADE2',fg='black',font=('times',15,'bold'))
        self.l4.grid(row=4,column=2)

        self.e4=Entry(cust_Frame,bg='white',fg='black',font=('times',15,'bold'))
        self.e4.grid(row=4,column=6)
        def price(event=""):
            if self.e5.get()=="General":
                self.e6.config(value=self.rooms_rate)
                self.e6.current(0)
            if self.e5.get()=="Delux":
                self.e6.config(value=self.rooms_rate)
                self.e6.current(1)
            if self.e5.get()=="Full Delux":
                self.e6.config(value=self.rooms_rate)
                self.e6.current(2)    
            if self.e5.get()=="Joint":
                self.e6.config(value=self.rooms_rate)
                self.e6.current(3)    

        self.l5=Label(cust_Frame,text='Room Types',bg='#5DADE2',fg='black',font=('times',15,'bold'))
        self.l5.grid(row=5,column=2)

        self.e5=ttk.Combobox(cust_Frame,textvariable=var,values=self.rooms,font=('times',12,'bold'))
        self.e5.grid(row=5,column=6)
        self.e5.bind("<<ComboboxSelected>>",price)

        
        self.l6=Label(cust_Frame,text='Room amount',bg='#5DADE2',fg='black',font=('times',15,'bold'))
        self.l6.grid(row=6,column=2)

        self.e6=ttk.Combobox(cust_Frame,values=self.rooms_rate,font=('times',12,'bold'))
        self.e6.grid(row=6,column=6)
        
        self.l7=Label(cust_Frame,text='Payment Methods',bg='#5DADE2',fg='black',font=('times',15,'bold'))
        self.l7.grid(row=7,column=2)

        self.e7=ttk.Combobox(cust_Frame,textvariable=var2,values=self.pay,font=('times',12,'bold'))
        self.e7.grid(row=7,column=6)
        #buttons===========================================================================
        self.btn1=Button(cust_Frame,text='Submit',command=submit,bg='green',fg='white',font=('times',12,'bold'))
        self.btn1.grid(row=10,column=2)
        
        self.btn2=Button(cust_Frame,text='Clear',command=clear,bg='red',fg='black',font=('times',12,'bold'))
        self.btn2.grid(row=10,column=4)

        self.btn2=Button(cust_Frame,text='Exit',bg='white',command=self.root.destroy,fg='black',font=('times',12,'bold'))
        self.btn2.grid(row=10,column=6)
        # showing area
        RightLabelFrame=LabelFrame(self.Frame1,text="Customer Entering Details",font=('times new roman',15,'bold'),bg='white',fg='black')
        RightLabelFrame.place(x=770,y=290,width=470,height=310)

        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg='#5DADE2',fg='black',font=('times new roman',15,'bold'))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        
        


        root.mainloop()


if __name__ == '__main__':
    root=Tk()
    obj1=checkin(root)
    
