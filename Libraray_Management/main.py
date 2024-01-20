from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from datetime import datetime , timedelta

class LibraryManagementSystem:
    def _init_(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1233x839+0+0")
        self.member_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.bookname_var=StringVar()
        self.bookauthor_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.fine_var=StringVar()
        
        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)
        
        frame=Frame(self.root,bd=12,relief=RIDGE,padx=10,bg="powder blue")
        frame.place(x=0,y=130,width=1281,height=350)
        
        DataFrameLeft=LabelFrame(frame,text="Library Member Information",bg="powder blue",fg="black",bd=10,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=7,width=720,height=310)
        
        lblMembers=Label(DataFrameLeft,bg="powder blue",fg="black",bd=10,text="MEMBER",font=("arial",12,"bold"),padx=6,pady=4)
        lblMembers.grid(row=0,column=0,sticky=W)
        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,state="readyonly",font=("arial",12,"bold"),width=18)
        comMember['value']=("ADMIN","LECTURER","STUDENT")
        comMember.grid(row=0,column=1)
        
        lblSAP_ID=Label(DataFrameLeft,bg="powder blue",fg="black",bd=10,text="SAP ID",font=("arial",12,"bold"),padx=2,pady=4)
        lblSAP_ID.grid(row=1,column=0,sticky=W)
        txtSAP_ID=Entry(DataFrameLeft,textvariable=self.id_var,font=("arial",12,"bold"),width=20)
        txtSAP_ID.grid(row=1,column=1)
        
        lblFirstName=Label(DataFrameLeft,bg="powder blue",fg="black",bd=10,text="FIRSTNAME",font=("arial",12,"bold"),padx=2,pady=4)
        lblFirstName.grid(row=2,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,textvariable=self.firstname_var,font=("arial",12,"bold"),width=20)
        txtFirstName.grid(row=2,column=1)
        
        lblLastName=Label(DataFrameLeft,bg="powder blue",fg="black",bd=10,text="LASTNAME",font=("arial",12,"bold"),padx=2,pady=4)
        lblLastName.grid(row=3,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,textvariable=self.lastname_var,font=("arial",12,"bold"),width=20)
        txtLastName.grid(row=3,column=1)
        
        lblMobile=Label(DataFrameLeft,bg="powder blue",fg="black",bd=10,text="MOBILE NO",font=("arial",12,"bold"),padx=2,pady=4)
        lblMobile.grid(row=4,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,textvariable=self.mobile_var,font=("arial",12,"bold"),width=20)
        txtMobile.grid(row=4,column=1)
        
        lblBookId=Label(DataFrameLeft,bg="powder blue",fg="black",bd=10,text="BOOK ID",font=("arial",12,"bold"),padx=6)
        lblBookId.grid(row=5,column=0,sticky=W)
        txtBookId=Entry(DataFrameLeft,textvariable=self.bookid_var,font=("arial",12,"bold"),width=20)
        txtBookId.grid(row=5,column=1)
        
        lblBookName=Label(DataFrameLeft,bg="powder blue",fg="black",bd=10,text="BOOK NAME",font=("arial",12,"bold"),padx=6,pady=4)
        lblBookName.grid(row=0,column=2,sticky=W)
        txtBookName=Entry(DataFrameLeft,textvariable=self.bookname_var,font=("arial",12,"bold"),width=20)
        txtBookName.grid(row=0,column=3)
        
        lblBookAuthor=Label(DataFrameLeft,bg="powder blue",fg="black",bd=10,text="BOOK AUTHOR",font=("arial",12,"bold"),padx=6,pady=4)
        lblBookAuthor.grid(row=1,column=2,sticky=W)
        txtBookAuthor=Entry(DataFrameLeft,textvariable=self.bookauthor_var,font=("arial",12,"bold"),width=20)
        txtBookAuthor.grid(row=1,column=3)
        
        lblDateBorrowed=Label(DataFrameLeft,bg="powder blue",fg="black",bd=10,text="BORROWED DATE",font=("arial",12,"bold"),padx=6,pady=4)
        lblDateBorrowed.grid(row=2,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,textvariable=self.dateborrowed_var,font=("arial",12,"bold"),width=20)
        txtDateBorrowed.grid(row=2,column=3)
        
        lblDateDue=Label(DataFrameLeft,bg="powder blue",fg="black",bd=10,text="DUE DATE",font=("arial",12,"bold"),padx=6,pady=4)
        lblDateDue.grid(row=3,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,textvariable=self.datedue_var,font=("arial",12,"bold"),width=20)
        txtDateDue.grid(row=3,column=3)
        
        lblDaysOnBook=Label(DataFrameLeft,bg="powder blue",fg="black",bd=10,text="DAYS ON BOOK",font=("arial",12,"bold"),padx=6,pady=4)
        lblDaysOnBook.grid(row=4,column=2,sticky=W)
        txtDaysOnBook=Entry(DataFrameLeft,textvariable=self.daysonbook_var,font=("arial",12,"bold"),width=20)
        txtDaysOnBook.grid(row=4,column=3)
        
        lblLateFine=Label(DataFrameLeft,bg="powder blue",fg="black",bd=10,text="LATE FINE",font=("arial",12,"bold"),padx=6,pady=4)
        lblLateFine.grid(row=5,column=2,sticky=W)
        txtLateFine=Entry(DataFrameLeft,textvariable=self.fine_var,font=("arial",12,"bold"),width=20)
        txtLateFine.grid(row=5,column=3)
        
        DataFrameRight=LabelFrame(frame,text="Book Details",bg="powder blue",fg="black",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameRight.place(x=740,y=7,width=500,height=310)
        
        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=25,height=14,padx=15,pady=2)
        self.txtBox.grid(row=0,column=2)
        
        listScrollbbar=Scrollbar(DataFrameRight)
        listScrollbbar.grid(row=0,column=1,sticky=W)
        
        listBooks=['Python Programming','Data Structures and Algorithms in Python','Operating System Concepts','Modern Operating Systems','Database System Concepts','Database Management Systems','Introduction to Algorithms','The C Programming Language','Computer Networks by Andrew S.','Rich Dad Poor Dad','Harry Potter-1','Harry Potter-2','Harry Potter-3','Harry Potter-4','Harry Potter-5','Harry Potter-6','Harry Potter-7(part1)','Harry Potter-7(part2)']        
        
        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if(x=="Python Programming"):
                self.bookid_var.set("BKID5454")
                self.bookname_var.set("Python Programming")
                self.bookauthor_var.set("JOHN ZELLE")
                
                d1=datetime.now()
                d3=d1+timedelta(days=7)
                self.dateborrowed_var.set(d1.date())
                self.datedue_var.set(d3.date())
                self.daysonbook_var.set("7")
                self.fine_var.set("10")
            
            elif(x=="Data Structures and Algorithms in Python"):
                self.bookid_var.set("BKID5396")
                self.bookname_var.set("Data Structures and Algorithms in Python")
                self.bookauthor_var.set("MICHEAL T.")
                d1=datetime.now()
                d3=d1+timedelta(days=7)
                self.dateborrowed_var.set(d1.date())
                self.datedue_var.set(d3.date())
                self.daysonbook_var.set("7")
                self.fine_var.set("10")
                
            elif(x=="Operating System Concepts"):
                self.bookid_var.set("BKID4853")
                self.bookname_var.set("Operating System Concepts")
                self.bookauthor_var.set("GREG GANGE")
                d1=datetime.now()
                d3=d1+timedelta(days=7)
                self.dateborrowed_var.set(d1.date())
                self.datedue_var.set(d3.date())
                self.daysonbook_var.set("7")
                self.fine_var.set("10")
            
            elif(x=="Modern Operating Systems"):
                self.bookid_var.set("BKID4373")
                self.bookname_var.set("Modern Operating Systems")
                self.bookauthor_var.set("ANDREW S.")
                d1=datetime.now()
                d3=d1+timedelta(days=7)
                self.dateborrowed_var.set(d1.date())
                self.datedue_var.set(d3.date())
                self.daysonbook_var.set("7")
                self.fine_var.set("10")
            
            elif(x=="Database Management Systems"):
                self.bookid_var.set("BKID5765")
                self.bookname_var.set("Database Management Systems")
                self.bookauthor_var.set("RAMAKRISHAN.")
                d1=datetime.now()
                d3=d1+timedelta(days=7)
                self.dateborrowed_var.set(d1.date())
                self.datedue_var.set(d3.date())
                self.daysonbook_var.set("7")
                self.fine_var.set("10")
                
            elif (x=="Introduction to Algorithms"):
                self.bookid_var.set("BKID9845")
                self.bookname_var.set("Introduction to Algorithms")
                self.bookauthor_var.set("THOMAS H.")
                d1=datetime.now()
                d3=d1+timedelta(days=7)
                self.dateborrowed_var.set(d1.date())
                self.datedue_var.set(d3.date())
                self.daysonbook_var.set("7")
                self.fine_var.set("10")
                
            elif (x=="Data Structures and Algorithms Made Easy"):
                self.bookid_var.set("BKID4438")
                self.bookname_var.set("Data Structures and Algorithms Made Easy")
                self.bookauthor_var.set("NARASIMHA K.")
                d1=datetime.now()
                d3=d1+timedelta(days=7)
                self.dateborrowed_var.set(d1.date())
                self.datedue_var.set(d3.date())
                self.daysonbook_var.set("7")
                self.fine_var.set("10")
                
            elif (x=="The C Programming Language"):
                self.bookid_var.set("BKID4673")
                self.bookname_var.set("The C Programming Language")
                self.bookauthor_var.set("BRIAN W.")
                d1=datetime.now()
                d3=d1+timedelta(days=7)
                self.dateborrowed_var.set(d1.date())
                self.datedue_var.set(d3.date())
                self.daysonbook_var.set("7")
                self.fine_var.set("10")
                
            elif (x=="Computer Networks"):
                self.bookid_var.set("BKID5553")
                self.bookname_var.set("Computer Networks")
                self.bookauthor_var.set("DAVID J.")
                d1=datetime.now()
                d3=d1+timedelta(days=7)
                self.dateborrowed_var.set(d1.date())
                self.datedue_var.set(d3.date())
                self.daysonbook_var.set("7")
                self.fine_var.set("10")
                
            elif (x=="Harry Potter-1"):
                self.bookid_var.set("BKID4383")
                self.bookname_var.set("Harry Potter-1")
                self.bookauthor_var.set("J.K.ROWLING")
                d1=datetime.now()
                d3=d1+timedelta(days=7)
                self.dateborrowed_var.set(d1.date())
                self.datedue_var.set(d3.date())
                self.daysonbook_var.set("7")
                self.fine_var.set("10")
                
            elif (x=="Harry Potter-2"):
                self.bookid_var.set("BKID4384")
                self.bookname_var.set("Harry Potter-2")
                self.bookauthor_var.set("J.K.ROWLING")
                d1=datetime.now()
                d3=d1+timedelta(days=7)
                self.dateborrowed_var.set(d1.date())
                self.datedue_var.set(d3.date())
                self.daysonbook_var.set("7")
                self.fine_var.set("10")
               
            elif (x=="Harry Potter-3"):
                self.bookid_var.set("BKID4385")
                self.bookname_var.set("Harry Potter-3")
                self.bookauthor_var.set("J.K.ROWLING")
                d1=datetime.now()
                d3=d1+timedelta(days=7)
                self.dateborrowed_var.set(d1.date())
                self.datedue_var.set(d3.date())
                self.daysonbook_var.set("7")
                self.fine_var.set("10")
                
            elif (x=="Harry Potter-4"):
                self.bookid_var.set("BKID4386")
                self.bookname_var.set("Harry Potter-4")
                self.bookauthor_var.set("J.K.ROWLING")
                d1=datetime.now()
                d3=d1+timedelta(days=7)
                self.dateborrowed_var.set(d1.date())
                self.datedue_var.set(d3.date())
                self.daysonbook_var.set("7")
                self.fine_var.set("10")
                
            elif (x=="Harry Potter-5"):
                self.bookid_var.set("BKID4387")
                self.bookname_var.set("Harry Potter-5")
                self.bookauthor_var.set("J.K.ROWLING")
                d1=datetime.now()
                d3=d1+timedelta(days=7)
                self.dateborrowed_var.set(d1.date())
                self.datedue_var.set(d3.date())
                self.daysonbook_var.set("7")
                self.fine_var.set("10")
                
            elif (x=="Harry Potter-6"):
                self.bookid_var.set("BKID4388")
                self.bookname_var.set("Harry Potter-6")
                self.bookauthor_var.set("J.K.ROWLING")
                d1=datetime.now()
                d3=d1+timedelta(days=7)
                self.dateborrowed_var.set(d1.date())
                self.datedue_var.set(d3.date())
                self.daysonbook_var.set("7")
                self.fine_var.set("10")
                
            elif (x=="Harry Potter-7(part1)"):
                self.bookid_var.set("BKID4389")
                self.bookname_var.set("Harry Potter-7(part1)")
                self.bookauthor_var.set("J.K.ROWLING")
                d1=datetime.now()
                d3=d1+timedelta(days=7)
                self.dateborrowed_var.set(d1.date())
                self.datedue_var.set(d3.date())
                self.daysonbook_var.set("7")
                self.fine_var.set("10")
                
            elif (x=="Harry Potter-7(part2)"):
                self.bookid_var.set("BKID4390")
                self.bookname_var.set("Harry Potter-7(part2)")
                self.bookauthor_var.set("J.K.ROWLING")
                d1=datetime.now()
                d3=d1+timedelta(days=7)
                self.dateborrowed_var.set(d1.date())
                self.datedue_var.set(d3.date())
                self.daysonbook_var.set("7")
                self.fine_var.set("10")                
               
            elif (x=="Rich Dad Poor Dad"):
                self.bookid_var.set("BKID4390")
                self.bookname_var.set("Rich Dad Poor Dad")
                self.bookauthor_var.set("J.K.ROWLING")
                d1=datetime.now()
                d3=d1+timedelta(days=7)
                self.dateborrowed_var.set(d1.date())
                self.datedue_var.set(d3.date())
                self.daysonbook_var.set("7")
                self.fine_var.set("10")   
          
        listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=13)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=5,pady=2)
        listScrollbbar.config(command=listBox.yview)
        
        for item in listBooks:
            listBox.insert(END , item)
            
        Framebutton=Frame(self.root,bd=10,relief=RIDGE,padx=0,bg="powder blue")
        Framebutton.place(x=0,y=480,width=1280,height=50)
        
        btnAddData=Button(Framebutton,command=self.add_data,text="Add Data",font=("arial",12,"bold"),bg="blue",fg="white",width=23,height=1)
        btnAddData.grid(row=0,column=0)
        
        btnAddData=Button(Framebutton,command=self.showData,text="Show Data",font=("arial",12,"bold"),bg="blue",fg="white",width=24)
        btnAddData.grid(row=0,column=1)
        
        btnAddData=Button(Framebutton,command=self.updateData,text="Update",font=("arial",12,"bold"),bg="blue",fg="white",width=25)
        btnAddData.grid(row=0,column=2)
        
        btnAddData=Button(Framebutton,command=self.deleteData,text="Delete",font=("arial",12,"bold"),bg="blue",fg="white",width=24)
        btnAddData.grid(row=0,column=3)
        
        btnAddData=Button(Framebutton,command=self.resetData,text="Reset",font=("arial",12,"bold"),bg="blue",fg="white",width=25)
        btnAddData.grid(row=0,column=4)
        
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=10,bg="powder blue")
        FrameDetails.place(x=0,y=530,width=1280,height=120)
    
        Table_frame=Frame(FrameDetails,bd=2,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=-10,y=0,width=1255,height=95)
        
        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
    
        self.library_table=ttk.Treeview(Table_frame,column=("Membertype","SAP_ID","FirstName","LastName","Mobileno","BookID","BookName","BookAuthor","DateBorrowed","DateDue","DaysOnBook","Fine"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)
    
        self.library_table.heading("Membertype",text="Member Type:")
        self.library_table.heading("SAP_ID",text="SAP ID:")
        self.library_table.heading("FirstName",text="First Name:")
        self.library_table.heading("LastName",text="Last Name:")
        self.library_table.heading("Mobileno",text="Mobile No:")
        self.library_table.heading("BookID",text="Book ID:")
        self.library_table.heading("BookName",text="Book Name:")
        self.library_table.heading("BookAuthor",text="Book Author:")
        self.library_table.heading("DateBorrowed",text="Borrowed Date:")
        self.library_table.heading("DateDue",text="Due Date:")
        self.library_table.heading("DaysOnBook",text="Days On Book:")
        self.library_table.heading("Fine",text="Late Fine:")
        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)
        
        self.library_table.column("Membertype",width=120)
        self.library_table.column("SAP_ID",width=120) 
        self.library_table.column("FirstName",width=150)
        self.library_table.column("LastName",width=150)
        self.library_table.column("Mobileno",width=120)
        self.library_table.column("BookID",width=120)
        self.library_table.column("BookName",width=150)
        self.library_table.column("BookAuthor",width=120)
        self.library_table.column("DateBorrowed",width=120)
        self.library_table.column("DateDue",width=120)
        self.library_table.column("DaysOnBook",width=120)
        self.library_table.column("Fine",width=120)
        
        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)
        
    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="libdata")
        my_cursor=conn.cursor()
        query="insert into library values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(self.member_var.get(),self.id_var.get(),self.firstname_var.get(),self.lastname_var.get(),self.mobile_var.get(),self.bookid_var.get(),self.bookname_var.get(),self.bookauthor_var.get(),self.dateborrowed_var.get(),self.datedue_var.get(),self.daysonbook_var.get(),self.fine_var.get())
        my_cursor.execute(query)
        conn.commit()
        self.fetch_data()
        self.resetData()
        conn.close()
        messagebox.showinfo("Success","Data Has Been Inserted Successfully")
        
        
    def updateData(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="libdata")
        my_cursor=conn.cursor()
        query="update library set Membertype=%s, FirstName=%s, LastName=%s, Mobileno=%s, BookID=%s, BookName=%s,BookAuthor =%s,DateBorrowed=%s, DateDue=%s, Daysoverdue=%s, Fine=%s where SAP_ID=%s"
        value=(self.member_var.get(),self.firstname_var.get(),self.lastname_var.get(),self.mobile_var.get(),self.bookid_var.get(),self.bookname_var.get(),self.bookauthor_var.get(),self.dateborrowed_var.get(),self.datedue_var.get(),self.daysonbook_var.get(),self.fine_var.get(),self.id_var.get())
        my_cursor.execute(query,value)  
        conn.commit()
        self.fetch_data() 
        self.resetData()
        conn.close()
        messagebox.showinfo("Success","Data Has Been Updated")
        
       
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="libdata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']
        self.member_var.set(row[0]),
        self.id_var.set(row[1]),
        self.firstname_var.set(row[2]),
        self.lastname_var.set(row[3]),
        self.mobile_var.set(row[4]),
        self.bookid_var.set(row[5]),
        self.bookname_var.set(row[6]),
        self.bookauthor_var.set(row[7]),
        self.dateborrowed_var.set(row[8]),
        self.datedue_var.set(row[9]),
        self.daysonbook_var.set(row[10]),
        self.fine_var.set(row[11])
      
    def showData(self):
        self.txtBox.insert(END,"Member: \t"+self.member_var.get()+"\n")
        self.txtBox.insert(END,"SAP ID: \t"+self.id_var.get()+"\n")
        self.txtBox.insert(END,"First Name: \t"+self.firstname_var.get()+"\n")
        self.txtBox.insert(END,"Last Name: \t"+self.lastname_var.get()+"\n")
        self.txtBox.insert(END,"Mobile: \t"+self.mobile_var.get()+"\n")
        self.txtBox.insert(END,"Book ID: \t"+self.bookid_var.get()+"\n")
        self.txtBox.insert(END,"Book Name: \t"+self.bookname_var.get()+"\n")
        self.txtBox.insert(END,"Book Author: \t"+self.bookauthor_var.get()+"\n")
        self.txtBox.insert(END,"Borrowed Date: \t"+self.dateborrowed_var.get()+"\n")
        self.txtBox.insert(END,"Due Date: \t"+self.datedue_var.get()+"\n")
        self.txtBox.insert(END,"Days On Book: \t"+self.daysonbook_var.get()+"\n")
        self.txtBox.insert(END,"Late Fine: \t"+self.fine_var.get()+"\n")
        
    def resetData(self):
        self.member_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.bookname_var.set(""),
        self.bookauthor_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook_var.set(""),
        self.fine_var.set(""),
        self.txtBox.delete("1.0",END)
        
    def deleteData(self):
        if self.id_var.get()=="" or self.bookid_var.get()=="":
            messagebox.showerror("Error","First Select The Member")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="libdata")
            my_cursor=conn.cursor()
            query="delete from library where SAP_ID=%s"
            value=(self.id_var.get(),)
            my_cursor.execute(query,value)
            conn.commit()
            self.fetch_data() 
            self.resetData()
            conn.close()
            messagebox.showinfo("Success","Data Has Been Deleted") 
                
if __name__ == '_main_': 
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()