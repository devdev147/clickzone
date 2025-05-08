#GUI library
import tkinter as tk
from tkinter import *
from tkinter import ttk 
import tkinter.messagebox as tkmsgbox #for messagebox
from tkinter.messagebox import askokcancel, showinfo, WARNING

from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkcalendar import Calendar

import PIL.Image #to avoid namespace conflicts as image is a common name
from PIL import Image, ImageTk #for image resize

#for file upload and calender
import datetime
import os, shutil
from pathlib import Path

#MySQL connectivity
import pymysql
from pandastable import Table
#from pandastable.plugin import Plugin  #additional functionalities
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#====================================================================================
global imgdir
#imgdir="E:\\photos\\" #image folder
#imgdir="./pics/" #image folder --- relative path in python starts with / or ./ or ../
imgdir="pics/"
global r
#====================================================================================
#MySQL Connectivity
conn = pymysql.connect( host='localhost',
                        user='root',
                        password='',
                        db='ip2022',
                        cursorclass=pymysql.cursors.DictCursor
                        )
#====================================================================================
def executeSQLQuery(sql): #for all SQL queries except SELECT
   try:
      cursor = conn.cursor()
      cursor.execute(sql)
      conn.commit()
      msg = 1
      return msg
   except conn.Error as e:
      msg = "ERROR: "+str(e.args[0])+e.args[1]
      return msg

#====================================================================================
def updateARowInPandasTable(dispDFFRM, rowDataList, tblname=None): #rowDataList is a series
        try:
                frameUpdateTable = Toplevel()  #create a pop-up window
                frameUpdateTable.title("Update Table")
                frameUpdateTable.geometry()
                frameUpdateTable.configure(background='yellow')
                r = 0
                print(rowDataList)
                for colname in rowDataList.index:
                        #print(i,' -- ',rowDataList[colname])
                        Label(frameUpdateTable, text=colname, bg='yellow') \
                                                           .grid(row=r, column=1, padx=15, pady=5, sticky='E')
                        '''
                        e = Entry(frameUpdateTable)
                        e.grid(row=r, column=2, padx=15, pady=5)
                        e.insert(INSERT, rowDataList[colname])
                        '''
                        globals()[colname+'TXT'] = Entry(frameUpdateTable)
                        globals()[colname+'TXT'].grid(row=r, column=2, padx=15, pady=5)

                        if rowDataList[colname] is None:
                           globals()[colname+'TXT'].insert(INSERT, '')
                        else:
                           globals()[colname+'TXT'].insert(INSERT, rowDataList[colname])

                        r += 1
                def updateTableSubmitButtonClickEvent(rowDataList):
                        #pass
                        '''
                        for widget in frameUpdateTable.winfo_children():
                                print(widget)
                        '''
                        sqlstr = ''                                
                        for colname in rowDataList.index:
                                #print(globals()[colname+'TXT'].get())
                                if (globals()[colname+'TXT'].get() is None) | (globals()[colname+'TXT'].get()==''):
                                   sqlstr += colname+"=NULL"+","
                                else:
                                   sqlstr += colname+"='"+globals()[colname+'TXT'].get()+"',"
                        sqlstr = sqlstr[:-1] #remove last ',' from the string
                        sqlstr = 'update '+tblname+' set '+sqlstr+' where id='+globals()['idTXT'].get()
                        print(sqlstr)
                        msg = executeSQLQuery(sqlstr)
                        if msg==1:
                                msg = "Record updated in the database successfully."
                                tk.messagebox.showinfo("MESSAGE", msg, parent=frameUpdateTable)
                                #selectAllRec()
                                frameUpdateTable.destroy()
                                dispDFFRM.destroy()
                                selectAllRec(tblname)
                        else:
                                msg = "Record could not be updated."
                                tk.messagebox.showinfo("MESSAGE", msg, parent=frameUpdateTable)
                updateTableSubmitButton = Button(frameUpdateTable, text="Update", command=lambda: updateTableSubmitButtonClickEvent(rowDataList))
                updateTableSubmitButton.grid(row=r, column=2, padx=10, pady=10)
                #r += 1
                def deleteTableSubmitButtonClickEvent(rowDataList):
                        #pass
                        sqlstr = 'delete from '+tblname+' where id='+globals()['idTXT'].get()
                        msg = executeSQLQuery(sqlstr)
                        if msg==1:
                                msg = "Record deleted from the database successfully."
                                tk.messagebox.showinfo("MESSAGE", msg, parent=frameUpdateTable)
                                #selectAllRec()
                                frameUpdateTable.destroy()
                                dispDFFRM.destroy()
                                selectAllRec(tblname)
                        else:
                                msg = "Record could not be deleted."
                                tk.messagebox.showinfo("MESSAGE", msg, parent=frameUpdateTable)                              
                deleteTableSubmitButton = Button(frameUpdateTable, text="Delete", command=lambda: deleteTableSubmitButtonClickEvent(rowDataList))
                deleteTableSubmitButton.grid(row=r, column=3, padx=10, pady=10)
        except conn.Error as e:
                msg = "ERROR: "+str(e.args[0])+e.args[1]
                tk.messagebox.showinfo("MESSAGE", msg, parent=frameUpdateTable)
#====================================================================================
def displayPandasTable(df,tblname=None):
   dispDFFRM = Toplevel()
   dispDFFRM.title('My Python Project')
   w, h = dispDFFRM.winfo_screenwidth()-120, dispDFFRM.winfo_screenheight()-160
   dispDFFRM.geometry("%dx%d+50+30" % (w, h))  #width,height,left,top
   dispDFFRM.configure(background="#88cffa") #"light grey"
   pt = Table(dispDFFRM, dataframe=df, width=w-10,height=h-10, showtoolbar=True, showstatusbar=True)
   pt.show()
   pt.cellbackgr = 'orange'
   #click row label in pandastable to update or delete it
   def leftButtonClickEvent(event): #left-button click event handling
      rowclicked = pt.get_row_clicked(event)
      rowDataList = pt.model.df.loc[rowclicked] #Series
      updateARowInPandasTable(dispDFFRM, rowDataList, tblname)
   pt.rowheader.bind('<Button-1>',leftButtonClickEvent)

   widths = pt.columnwidths
   totalwidth = 0
   for c in widths:
      totalwidth += widths[c]
   #resize parent frame to the size of the pandastable    
   dispDFFRM.geometry("%dx%d+50+30" % (totalwidth+80, pt.rowheight*(pt.rows+4)))  #width,height,left,top

   
#====================================================================================  
def guiTable():
   #creating custom GUI table using Entry()
   for i in range(total_rows):
      for j in range(total_columns):
         e = Entry(root, width=20, fg='blue', font=('Arial',16,'bold'))
         e.grid(row=i, column=j)
         e.insert(END, lst[i][j])
#====================================================================================
def descQuery(table=None): #for "DESC tablename;" or "show columns from student;" SQL query
   try:
      if table==None:
         table='person'
      sql = "desc "+table
      cursor = conn.cursor()
      cursor.execute(sql)
      data = cursor.fetchall()
      #Column Names -  Field,Type,Null,Key,Default,Extra
      df=pd.DataFrame(data)
      displayPandasTable(df)
   except conn.Error as e:
      msg = "ERROR: "+str(e.args[0])+e.args[1]
      tk.messagebox.showinfo("MESSAGE", msg, parent=root)
#====================================================================================
def executeSelectQuery(sql=0): #for SELECT SQL query
   def display(sql,tblname=None):
      #Get column names
      #SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA='dbname' AND TABLE_NAME='tblname'
      try:
         #sql = "SELECT * FROM student"
         cursor = conn.cursor()
         cursor.execute(sql)
         '''
         result = cursor.fetchall()
         for row in result:
            #print(row['folio'],row['name'],row['house'],row['classsection'],str(row['dob']),row['marks']))
         '''
         data = cursor.fetchall()
         df=pd.DataFrame(data)
         displayPandasTable(df,tblname)
      except conn.Error as e:
         msg = "ERROR: "+str(e.args[0])+e.args[1]
         #tk.messagebox.showinfo("MESSAGE", msg, parent=root)
         tk.messagebox.showinfo("MESSAGE", msg, parent=frameSelectQuery)

   if sql==0:
        #tk.messagebox.showinfo("MESSAGE", "No query given...enter the one", parent=root) 
        r = 0 
        frameSelectQuery = Toplevel()
        frameSelectQuery.title("SELECT SQL Query")
        #frameSelectQuery.geometry("800x600+50+50")
        frameSelectQuery.geometry()
        frameSelectQuery.configure(background='light blue')
        r += 1
        tablenameLBL = Label(frameSelectQuery, text="Table Name", bg='light blue')
        tablenameLBL.grid(row=r, column=1, padx=10, pady=10, sticky=E)
        tablenameTXT = Text(frameSelectQuery, height=1, width=60)
        tablenameTXT.grid(row=r, column=2, padx=10, pady=10)
        tablenameTXT.insert(INSERT,'person')
        r += 1 
        def tableButtonClickEvent():
           tblname = tablenameTXT.get('1.0', END)
           sql = "select * from "+tblname
           display(sql,tblname) 
        tableButton = Button(frameSelectQuery, text="Submit Table Name", command=tableButtonClickEvent)
        tableButton.grid(row=r, column=2)
        r += 1
        Label(frameSelectQuery, text="OR", bg='light blue').grid(row=r, column=2, sticky=NSEW)
        r += 1
        def createQueryButtonClickEvent():
           sql = tablenameTXT.get('1.0', END)
           #sql = sql.replace("'","\'")
           #sql = sql.replace('"','\"')
           #print(sql)
           display(sql) 
        createQueryButton = Button(frameSelectQuery, text="Submit SQL Query", command=createQueryButtonClickEvent)
        createQueryButton.grid(row=r, column=2, padx=10, pady=10)
        frameSelectQuery.mainloop()
   else:
      display(sql)
#====================================================================================
def selectAllRec(tblname=None):

   try:
      if tblname==None:
         sql = "select * from person"
      else:
         sql = "select * from "+tblname
      cursor = conn.cursor()
      cursor.execute(sql)
      data = cursor.fetchall()
      #Column Names -  Field,Type,Null,Key,Default,Extra
      df=pd.DataFrame(data)
      #displayPandasTable(df)
      dispDFFRM = Toplevel()
      dispDFFRM.title('My Python Project')
      w, h = dispDFFRM.winfo_screenwidth()-120, dispDFFRM.winfo_screenheight()-160
      dispDFFRM.geometry("%dx%d+50+30" % (w, h))  #width,height,left,top
      dispDFFRM.configure(background="#88cffa") #"light grey"
      pt = Table(dispDFFRM, dataframe=df, width=w-10,height=h-10, showtoolbar=True, showstatusbar=True)
      pt.show()
      pt.cellbackgr = 'orange'
      #click row label in pandastable to update or delete it
      def leftButtonClickEvent(event): #left-button click event handling
         rowclicked = pt.get_row_clicked(event)
         rowDataList = pt.model.df.loc[rowclicked] #Series
         updateARowInPandasTable(dispDFFRM, rowDataList)
      pt.rowheader.bind('<Button-1>',leftButtonClickEvent)
   except conn.Error as e:
      msg = "ERROR: "+str(e.args[0])+e.args[1]
      tk.messagebox.showinfo("MESSAGE", msg, parent=root)

#====================================================================================
def Matplotlib():
   def plot():
      x = [2012,2013,2014,2015,2016]
      y = [45,56,23,78,42]
      plt.bar(x,y)
      plt.xlabel('X-Axis')
      plt.ylabel('Y-Axis')
      plt.xticks(x)
      plt.yticks(np.arange(0,101,10))
      plt.show()
   window = Tk()# the main Tkinter window
   window.title('Plotting in Tkinter')# setting the title
   window.geometry("500x500")# dimensions of the main window
   plot_button = Button(master = window, command = plot,height = 2, width = 10,text = "Plot")# button that displays the plot
   plot_button.pack()# place the button in main window
   window.mainloop()# run the gui
#====================================================================================
def MatplotlibGUI():
   from matplotlib.figure import Figure
   from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
   # plot function is created for 
   # plotting the graph in 
   # tkinter window
   def plot():
      fig = Figure(figsize = (5, 5), dpi = 100)# the figure that will contain the plot
      y = [i**2 for i in range(101)]# list of squares
      plot1 = fig.add_subplot(111)# adding the subplot
      plot1.plot(y)# plotting the graph
      canvas = FigureCanvasTkAgg(fig, master = window)
      canvas.draw()# creating the Tkinter canvas containing the Matplotlib figure
      canvas.get_tk_widget().pack()# placing the canvas on the Tkinter window
      toolbar = NavigationToolbar2Tk(canvas, window)# creating the Matplotlib toolbar
      toolbar.update()
      canvas.get_tk_widget().pack()# placing the toolbar on the Tkinter window
   window = Tk()# the main Tkinter window
   window.title('Plotting in Tkinter')# setting the title
   window.geometry("500x500")# dimensions of the main window
   plot_button = Button(master = window, command = plot,height = 2, width = 10,text = "Plot")# button that displays the plot
   plot_button.pack()# place the button in main window
   window.mainloop()# run the gui  

#====================================================================================
def outputframe(parentframe):
   #Data Display Frame
   bgcolor = 'blue'
   w, h = parentframe.winfo_screenwidth(), parentframe.winfo_screenheight()
   w=w*40/100
   h=h*70/100
   frameDisplayData = Toplevel()
   frameDisplayData.title("Data Display")
   frameDisplayData.geometry(("%dx%d+0+0")%(w,h))
   frameDisplayData.configure(background=bgcolor)
   r = 0
   #subframe #1 - Title
   titletext = "Personal Data Display Interface"
   titleLBL = Label(frameDisplayData, height=2, text=titletext, font='Helvetica 15 bold', bg="grey", fg="white")
   titleLBL.grid(row=r, column=0, columnspan=5, sticky='NEW')
   r += 1
   #subframe #2 - GUI
   bgcolor = 'green'
   frameDisplayDataGUI = Frame(frameDisplayData, width=w*80/100, bg=bgcolor)
   frameDisplayDataGUI.grid(row=1, column=0, columnspan=5, padx=10, pady=10, sticky='EW')
   frameDisplayData.grid_columnconfigure(1, weight=1)
   
   #GUI Controls
   r1 = 0
   Label(frameDisplayDataGUI, text="DATA DISPLAY", bg=bgcolor).grid(row=r1, column=0, columnspan=3, sticky='NEW')
   r1 += 1
   #Data Access - get data from database table
   #Person Name Pickup/Drop-down 
   try:
      sql = "SELECT distinct name FROM person"
      cursor = conn.cursor()
      cursor.execute(sql)
      data = cursor.fetchall()
      df=pd.DataFrame(data)
   except conn.Error as e:
      msg = "ERROR: "+str(e.args[0])+e.args[1]
      tk.messagebox.showinfo("MESSAGE", msg, parent=frameDisplayData)
   namevar = StringVar()
   namelookupvalues = df['name'].tolist()
   nameCBO = Combobox(frameDisplayDataGUI, name='namecbo', width=30, textvariable=namevar)
   nameCBO.grid(row=r1, column=1)
   nameCBO['values'] = namelookupvalues
   nameCBO.current(0)
   def nameCBOSelectedEvent(event, arg):
      #pass row and frame name to cbo event handler
      r1 = arg['row']
      #frameDisplayDataGUI = arg['frame']
      try:
         name = event.widget.get()
         sql = "SELECT * FROM person where name='"+name+"'"
         cursor = conn.cursor()
         cursor.execute(sql)
         data = cursor.fetchall()
         df=pd.DataFrame(data)
         r1 += 1
         #Name
         Label(frameDisplayDataGUI, text="Name", bg=bgcolor).grid(row=r1, column=0, sticky='NE')
         nameTXT = Entry(frameDisplayDataGUI, width=30)
         nameTXT.grid(row=r1, column=1, sticky='NW')   
         nameTXT.delete(0,END)
         nameTXT.insert(INSERT,df.iloc[0]['title']+" "+df.iloc[0]['name'])
         #image
         #imgdir="E:\\photos\\" #image folder
         global imgdir
         img=PIL.Image.open(imgdir+df.iloc[0]['pic'])
         img=img.resize((100,100))
         render=ImageTk.PhotoImage(img,master=frameDisplayDataGUI)
         imageFileLBL = Label(frameDisplayDataGUI)#, bg=bgcolor)
         imageFileLBL.grid(row=r1, column=2, rowspan=4, sticky='NW')          
         imageFileLBL.config(image=render)
         imageFileLBL.image = render
         r1 += 1      
         #Gender
         Label(frameDisplayDataGUI, text="Gender", bg=bgcolor).grid(row=r1, column=0, sticky='NE')
         genderTXT = Entry(frameDisplayDataGUI, width=30)
         genderTXT.grid(row=r1, column=1, sticky='NW')          
         genderTXT.delete(0,END)
         genderTXT.insert(INSERT,df.iloc[0]['gender'])
         r1 += 1
         #DOB
         Label(frameDisplayDataGUI, text="Date of Birth", bg=bgcolor).grid(row=r1, column=0, sticky='NE')
         dobTXT = Entry(frameDisplayDataGUI, width=30)
         dobTXT.grid(row=r1, column=1, sticky='NW')          
         dobTXT.delete(0,END)
         dobTXT.insert(INSERT,df.iloc[0]['dob'])
         r1 += 1
         #Hobbies
         Label(frameDisplayDataGUI, text="Hobbies", bg=bgcolor).grid(row=r1, column=0, sticky='NE')
         hobbyTXT = Entry(frameDisplayDataGUI, width=30)
         hobbyTXT.grid(row=r1, column=1, sticky='NW')          
         hobbyTXT.delete(0,END)
         hobbyTXT.insert(INSERT,df.iloc[0]['hobby'])

      except conn.Error as e:
         msg = "ERROR: "+str(e.args[0])+e.args[1]
         tk.messagebox.showinfo("MESSAGE", msg, parent=frameDisplayData)

   cboparam = {'row':r1,'frame':frameDisplayDataGUI}
   nameCBO.bind("<<ComboboxSelected>>", lambda event, arg=cboparam: nameCBOSelectedEvent(event,arg))

   #uniform padding for all controls on the frame 
   for widget in frameDisplayDataGUI.winfo_children():
      widget.grid(padx=10, pady=5)

#====================================================================================
def inputframe(parentframe):
        #Data Entry Frame
        bgcolor = 'yellow'
        w, h = parentframe.winfo_screenwidth(), parentframe.winfo_screenheight()
        w=w*40/100
        h=h*70/100
        frameInsertData = Toplevel()
        frameInsertData.title("Data Entry")
        frameInsertData.geometry(("%dx%d+0+0")%(w,h))
        frameInsertData.configure(background=bgcolor)
        #GUI Controls
        r = 0
        #subframe #1 - Title
        titletext = "Personal Data Entry Interface"
        titleLBL = Label(frameInsertData, height=2, text=titletext, font='Helvetica 15 bold', bg="grey")
        titleLBL.grid(row=r, column=0, columnspan=5, sticky='NEW')
        r += 1
        #subframe #2 - GUI
        bgcolor = 'green'
        frameInsertDataGUI = Frame(frameInsertData, width=w*80/100, bg=bgcolor)
        frameInsertDataGUI.grid(row=1, column=0, columnspan=5, padx=10, pady=10, sticky='EW')
        frameInsertData.grid_columnconfigure(1, weight=1)
        #
        r1 = 0
        Label(frameInsertDataGUI, text="DATA ENTRY", bg=bgcolor).grid(row=r1, column=0, columnspan=3, sticky='NEW')
        r1 += 1
        #Title drop-down
        Label(frameInsertDataGUI, text="Title", bg=bgcolor).grid(row=r1, column=0, sticky='NE')
        titleTXT = Text(frameInsertDataGUI, height=1, width=30)
        titleTXT.grid(row=r1, column=1, sticky='NW')
        titleTXT.configure(bg='light grey') 
        titleTXT.bind("<Key>", lambda a: "break") #disable typing in the widget
        lookupvals = ['Mr.','Ms.','Dr.']
        title = StringVar()
        titleCBO = Combobox(frameInsertDataGUI, name='titlecbo', width=30, textvariable=title)
        titleCBO['values'] = lookupvals
        titleCBO.grid(row=r1, column=2, sticky='NE')
        titleCBO.current(0)
        def cboSelectedEvent(event):
                txt = event.widget.get()
                titleTXT.delete('1.0', END)
                titleTXT.insert(INSERT, txt)
        titleCBO.bind("<<ComboboxSelected>>", cboSelectedEvent)
        r1 += 1
        #Name Text Field
        Label(frameInsertDataGUI, text="Name", bg=bgcolor).grid(row=r1, column=0, sticky='NE')
        #nameTXT = Entry(frameInsertDataGUI, width=35)
        nameTXT = Text(frameInsertDataGUI, height=1, width=30)
        nameTXT.grid(row=r1, column=1)
        #Hobby Checkboxes
        r1 += 1
        hobbyFRM = LabelFrame(frameInsertDataGUI, text="Hobbies", padx=15, pady=5)
        hobbyFRM.grid(row=r1, column=2, columnspan=3, sticky='NW')
        Label(frameInsertDataGUI, text="Hobby", bg=bgcolor).grid(row=r1, column=0, sticky='NE')
        hobbyTXT = Text(frameInsertDataGUI, height=3, width=30)
        hobbyTXT.grid(row=r1, column=1, sticky='NW')
        rTemp = 0
        hobby1 = tk.IntVar(value=1) #by default checked
        hobby2 = tk.IntVar(value=0)
        hobby3 = tk.IntVar(value=0)
        def hobbyChecked():
                hobby=''
                if hobby1.get()==1:
                        hobby += hobby1CHK['text']+","
                if hobby2.get()==1:
                        hobby += hobby2CHK['text']+","
                if hobby3.get()==1:
                        hobby += hobby3CHK['text']+","
                hobby = hobby[:-1]
                hobbyTXT.delete('1.0', END)
                hobbyTXT.insert(INSERT, hobby)
        hobby1CHK = Checkbutton(hobbyFRM, text='Reading', command=hobbyChecked, \
                      variable=hobby1, onvalue=1, offvalue=0, height=1)
        hobby1CHK.grid(row=rTemp, column=1, sticky=W)
        rTemp += 1
        hobby2CHK = Checkbutton(hobbyFRM, text='Writing', command=hobbyChecked, \
                      variable=hobby2, onvalue=1, offvalue=0, height=1)
        hobby2CHK.grid(row=rTemp, column=1, sticky=W)
        rTemp += 1
        hobby3CHK = Checkbutton(hobbyFRM, text="Swimming", command=hobbyChecked, \
                      variable=hobby3, onvalue=1, offvalue=0, height=1)
        hobby3CHK.grid(row=rTemp, column=1, sticky=W)
        #Gender radio buttons  
        r1 += 1
        Label(frameInsertDataGUI, text="Gender", bg=bgcolor).grid(row=r1, column=0, sticky='NE')
        genderTXT = Text(frameInsertDataGUI, height=1, width=30)
        genderTXT.grid(row=r1, column=1, sticky='NE')
        genderFRM = LabelFrame(frameInsertDataGUI, text="Gender", padx=15, pady=5)
        genderFRM.grid(row=r1, column=2, sticky="NW") #columnspan=5
        gender = StringVar()
        def genderRBTSelection(): 
                genderTXT.delete('1.0', END)
                genderTXT.insert(INSERT, gender.get())
        maleRBT = Radiobutton(genderFRM, text='Male', variable=gender, value='M', background="light blue", \
                              command=genderRBTSelection)
        maleRBT.grid(row=0, column=0)
        femaleRBT = Radiobutton(genderFRM, text='Female', variable=gender, value='F', background="light blue", \
                                command=genderRBTSelection)
        femaleRBT.grid(row=1, column=0)
        #Upload image file dialog
        r1 += 1
        Label(frameInsertDataGUI, text="Upload Image", bg=bgcolor).grid(row=r1, column=0, sticky='NE')
        imageFileTXT = Text(frameInsertDataGUI, height=1, width=30)
        imageFileTXT.grid(row=r1, column=1, sticky='NW')
        def imgFileUploadButtonEvent():
                #imgdir="E:\\photos\\" #image folder
                global imgdir
                fileName=filedialog.askopenfilename(parent=frameInsertDataGUI, \
                                                    initialdir="/", title="Select a file", \
                                                    filetype=(("jpeg","*.jpg"),("png","*.png")))
                path=Path(fileName)
                imageFileTXT.delete('1.0', END)
                imageFileTXT.insert(INSERT, path.name)
                shutil.copy(fileName,imgdir)
                img=PIL.Image.open(fileName)
                img=img.resize((100,100))
                render=ImageTk.PhotoImage(img,master=frameInsertDataGUI)
                imageFileLBL.config(image=render)
                imageFileLBL.image = render
        Button(frameInsertDataGUI, text="Image File Upload", command=imgFileUploadButtonEvent).grid(row=r1, column=2, sticky='NW')
        r1 += 1       
        imageFileLBL = Label(frameInsertDataGUI, bg=bgcolor)
        imageFileLBL.grid(row=r1, column=2, sticky='NW') 
        #Date of Birth Calendar dialog
        r1 += 1
        Label(frameInsertDataGUI, text="Date of Birth", bg=bgcolor).grid(row=r1, column=0, sticky='NE')
        dobTXT = Text(frameInsertDataGUI, height=1, width=30)
        dobTXT.grid(row=r1, column=1, sticky='NE')
        def selectDateButtonEvent():
                def pickDateSelectionEvent():
                        selected_date = (cal.get_date())                
                        thedate = datetime.datetime.strptime(selected_date, '%m/%d/%y')
                        dateFormatted = thedate.strftime("%Y%m%d")
                        dobTXT.delete('1.0', END)
                        dobTXT.insert(INSERT, dateFormatted)
                        top.destroy()
                #create calendar
                top = Toplevel(frameInsertDataGUI)
                cal = Calendar(top,font="Arial 10",background='darkblue',foreground='white',selectmode='day')
                cal.grid()
                Button(top, text="OK", command=pickDateSelectionEvent).grid()
        Button(frameInsertDataGUI, text="Select Date for DOB", command=selectDateButtonEvent).grid(row=r1, column=2, sticky='NW')
        r1 += 1
        #Submit button
        def submitButtonEvent():
                #read data from GUI widgets
                title = titleTXT.get('1.0', "end-1c")
                name = nameTXT.get('1.0', "end-1c")
                gender = genderTXT.get('1.0', "end-1c")
                hobby = hobbyTXT.get('1.0', "end-1c")
                imgfile = imageFileTXT.get('1.0', "end-1c")
                dob = dobTXT.get('1.0', "end-1c")
                #save data in MySQL database
                sql = "INSERT INTO person(title,name,gender,hobby,pic,dob) VALUES("
                sql += "'"+title+"','"+name+"','"+gender+"','"+hobby+"','"+imgfile+"','"+dob+"')"
                msg = executeSQLQuery(sql)
                if msg==1:
                   msg = "Record save into database successfully."
                   tk.messagebox.showinfo("MESSAGE", msg, parent=frameInsertData)
                else:
                   tk.messagebox.showinfo("MESSAGE", msg, parent=frameInsertData)
                #display records from database table
                sql = "select * from person"
                executeSelectQuery(sql)
        Button(frameInsertDataGUI, text="Submit", width=20, command=submitButtonEvent).grid(row=r1, column=1, sticky='NW')
        #uniform padding for all controls on the frame 
        for widget in frameInsertDataGUI.winfo_children():
                widget.grid(padx=10, pady=2)

#====================================================================================
#main or root app window
root = Tk() 
root.title('KirtiKrit Software Management System') 
w, h = root.winfo_screenwidth()-20, root.winfo_screenheight()-100
root.geometry("%dx%d+0+0" % (w, h)) #root window size 'wxh' at left top coordinates 0,0
root.configure(background="light grey")
#background image & title bars
img = Image.open("bgimg.jpg") 
resizeimg = img.resize((w,h)) 
bgimg = ImageTk.PhotoImage(resizeimg)
welcometext = "Hey Folks! Welcome to KirtiKrit Soft Inc."
bgimglbl = Label(root, compound=tk.CENTER, text=welcometext, font='Helvetica 30 bold', fg='white', image=bgimg)
bgimglbl.grid(row=0, column=0)
welcometext1 = "Top Full Width"
welcomelbl1 = Label(root, height=2, text=welcometext1, font='Helvetica 15 bold', bg="grey")
welcomelbl1.grid(row=0, column=0, sticky='NEW')
welcometext2 = "Bottom Full Width"
welcomelbl2 = Label(root, height=2, text=welcometext2, font='Helvetica 15 bold', bg="grey")
welcomelbl2.grid(row=0, column=0, sticky='SEW')
#Menu
#use lambda to pass arguments
#newmenu.add_command(label="Item", command=lambda: desctable(tablename))
menubar = Menu(root)

mastermenu = Menu(menubar, tearoff=0)
mastermenu.add_command(label="Input Record", command=lambda: inputframe(root)) #frame1

#mastermenu.add_command(label="Update Record", command=lambda: selectUpdateDelete(root))
#mastermenu.add_command(label="Delete Record", command=lambda: selectUpdateDelete(root))

mastermenu.add_command(label="Table Structure", command=descQuery)
menubar.add_cascade(label="MASTER", menu=mastermenu)

reportmenu = Menu(menubar, tearoff=0)
reportmenu.add_command(label="Display A Record", command=lambda: outputframe(root)) #frame2
reportmenu.add_command(label="Display All Records", command=selectAllRec)
reportmenu.add_command(label="Select SQL Query", command=executeSelectQuery)
reportmenu.add_command(label="MatplotlibGUI", command=MatplotlibGUI)
reportmenu.add_command(label="Matplotlib", command=Matplotlib)
menubar.add_cascade(label="REPORT", menu=reportmenu)
#====================================================================================
#GUI - set menu and start infinite main root loop
root.config(menu=menubar)
root.mainloop()
#====================================================================================
# DATABASE SETUP
# ==============
'''
CREATE TABLE person (
  id int primary key auto_increment,
  title varchar(30),
  name varchar(30),
  gender varchar(30),
  hobby varchar(300),
  pic varchar(30),
  dob date
);
INSERT INTO person (id, title, name, gender, hobby, pic, dob) VALUES
(9, 'Mr.', 'Xyz', 'M', 'Reading,Writing', '1.png', '2022-09-07'),
(10, 'Ms.', 'abcd', 'F', 'Reading,Writing,Swimming', '2.png', '2012-03-15');
'''
#====================================================================================

