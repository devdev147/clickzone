from _libraryAndDBConnection import *
# date time samples

# date time string formats to display different parts
'''
%d 	Day of month (01-31) 	                31 	
%b 	Month name, short  	                Dec 	
%B 	Month name, full  	                December 	
%m 	Month number (01-12) 	                12 	
%y 	Year, short without century 	        18 	
%Y 	Year, full with century                 2018 	
%C 	Century 	                        20 	
%a 	Weekday, short  	                Wed 	
%A 	Weekday, full  	                        Wednesday 	
%w 	Weekday, number (0-6; 0 is Sunday)      3 	 	
%u 	weekday (1-7) 	                        1 	

%H 	Hour (00-23) 	                        17 	
%I 	Hour (00-12) 	                        05 	
%M 	Minute (00-59) 	                        41 	
%S 	Second (00-59) 	                        08 	
%f 	Microsecond (000000-999999) 	        548513 	
%p 	AM/PM 	                                PM 	
%z 	UTC offset 	                        +0100 	
%Z 	Timezone 	                        CST 	

%j 	Day number of year (001-366) 	        365 	
%V 	Week number of year (01-53) 	        01
'''
#-----------------------------------------------------------------------------
def differenceBetweenDates():
        from datetime import datetime
        

        # get two dates
        d1 = '14/8/2019'
        d2 = '16/3/2022'
        # convert string to date object
        start_date = datetime.strptime(d1, "%d/%m/%Y")
        end_date = datetime.strptime(d2, "%d/%m/%Y")
        res = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
        

        '''
        from dateutil import relativedelta
        # Get the relativedelta between two dates
        delta = relativedelta.relativedelta(end_date, start_date)
        print('Years, Months, Days between two dates is')
        print(delta.years, 'Years,', delta.months, 'months,', delta.days, 'days')
        # get months difference
        res_months = delta.months + (delta.years * 12)
        print('Total Months between two dates is:', res_months)
        '''

        d1 = datetime.datetime(2022,1,1)
        d2 = datetime.datetime(2022,2,2)
        d3 = datetime.datetime(2022,3,3)
        print(d1<d2<d3)
        print(d2<d1<d3)

#-----------------------------------------------------------------------------
def getDateFromMySQLTable():
        from datetime import datetime       #for handling date & its formats    
        from dateutil import relativedelta  #for date based arithmatic operations
        
        con = pymysql.connect( host='localhost',
                        user='root',
                        password='',
                        db='ip2022',
                        cursorclass=pymysql.cursors.DictCursor)
        cursor = con.cursor()
        try:
                sql = "select * from person"
                cursor.execute(sql)
                # Format date
                #data = cursor.fetchone()
                #dob = datetime.strptime(data.dob, '%Y-%m-%d %H:%M:%S')
                data = cursor.fetchall()
                #df=pd.DataFrame(data)
                for row in data:
                        print('-'*30)
                        print(f"Title: {row['title']}")
                        print(f"Name: {row['name']}")
                        print(f"Gender: {row['gender']}")
                        print(f"Hobbies: {row['hobby']}")
                        #dob = datetime.strptime('2007-03-15 03:15:34', '%Y-%m-%d %H:%M:%S')  #convert string to formatted date
                        dob = row['dob'].strftime("%a, %d %B %Y") #format date-time 
                        #print(f"DOB: {row['dob']}\n")
                        print(f"DOB: {dob}")
                        # Get relativedelta between two dates - current date and DOB
                        today = datetime.now()  #datetime.today()
                        delta = relativedelta.relativedelta(today, row['dob'])
                        print('Age: ',delta.years, 'Years,', delta.months, 'months,', delta.days, 'days','\n')
                        #datebetween = datetime(2023,2,1) < row['dob'] < datetime(2023,7,1)  #datetime cannot be compared with date
                        datebetween = date(2023,2,1) < row['dob'] < date(2023,7,1)  #sql returns date, so compare it with date object & not with datetime object
                        print('Date between 1 Feb and 1 July 2023', datebetween)
                        '''
                        # get months difference
                        res_months = delta.months + (delta.years * 12)
                        print('Total Months between two dates is:', res_months)
                        # get days difference
                        res_days = ?
                        print('Total days between two dates is:', res_days)
                        '''        
                cursor.close()
        except conn.Error as e:
                msg = "ERROR: "+str(e.args[0])+e.args[1]
                print(msg)
        
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
        '''
#-----------------------------------------------------------------------------
def datetimefunctions():
        # current date-time
        dt = datetime.now()
        print("Current date & time: ",dt)
        # create date
        dt = datetime(2023, 5, 17)
        print("Date created using 3 integers 2023,5,17 ",dt)
        # format date
        dt = datetime.now()
        print("Formating current date & time to display its different parts:")
        print("3. ",dt.strftime("%B"))

        print("date.today(): ",date.today())
        print("date.today().year: ",date.today().year)
        print("date.today().year: ",date.today().month)
        print("date.today().year: ",date.today().day)

        print(dt.strftime("%A, %d %B %Y"))

#-----------------------------------------------------------------------------
def index(rootframe):

        frame = Toplevel()
        r=0
        Label(frame, text="Date Time Input").grid(row=r, column=0, sticky='W')
        datetimeinputTXT = Text(frame, height=1, width=30)
        datetimeinputTXT.grid(row=r, column=1, sticky='W')
        r+=1
        def currentDateTimeBTNClickEvent():
                dt = datetime.now()
                datetimeoutputTXT.delete('1.0', END)
                datetimeoutputTXT.insert(INSERT, dt)
        Button(frame, text="Current Date Time", width=20, command=currentDateTimeBTNClickEvent).grid(row=r, column=1, sticky='W')
        r+=1
        Label(frame, text="Date Time Output").grid(row=r, column=0, sticky='W')
        datetimeoutputTXT = Text(frame, height=1, width=30)
        datetimeoutputTXT.grid(row=r, column=1, sticky='W')

        '''
        r = 0
        #Title drop-down
        Label(frameGUI, text="Title", bg=bgcolor).grid(row=r1, column=0, sticky='NE')
        titleTXT = Text(frameGUI, height=1, width=30)
        titleTXT.grid(row=r1, column=1, sticky='NW')
        titleTXT.configure(bg='light grey') 
        titleTXT.bind("<Key>", lambda a: "break") #disable typing in the widget
        lookupvals = ['Mr.','Ms.','Dr.']
        title = StringVar()
        titleCBO = Combobox(frameGUI, name='titlecbo', width=30, textvariable=title)
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
        Label(frameGUI, text="Name", bg=bgcolor).grid(row=r1, column=0, sticky='NE')
        #nameTXT = Entry(frameGUI, width=35)
        nameTXT = Text(frameGUI, height=1, width=30)
        nameTXT.grid(row=r1, column=1)
        #Hobby Checkboxes
        r1 += 1
        hobbyFRM = LabelFrame(frameGUI, text="Hobbies", padx=15, pady=5)
        hobbyFRM.grid(row=r1, column=2, columnspan=3, sticky='NW')
        Label(frameGUI, text="Hobby", bg=bgcolor).grid(row=r1, column=0, sticky='NE')
        hobbyTXT = Text(frameGUI, height=3, width=30)
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
        Label(frameGUI, text="Gender", bg=bgcolor).grid(row=r1, column=0, sticky='NE')
        genderTXT = Text(frameGUI, height=1, width=30)
        genderTXT.grid(row=r1, column=1, sticky='NE')
        genderFRM = LabelFrame(frameGUI, text="Gender", padx=15, pady=5)
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
        Label(frameGUI, text="Upload Image", bg=bgcolor).grid(row=r1, column=0, sticky='NE')
        imageFileTXT = Text(frameGUI, height=1, width=30)
        imageFileTXT.grid(row=r1, column=1, sticky='NW')
        def imgFileUploadButtonEvent():
                #imgdir="E:\\photos\\" #image folder
                global imgdir
                fileName=filedialog.askopenfilename(parent=frameGUI, \
                                                    initialdir="/", title="Select a file", \
                                                    filetype=(("jpeg","*.jpg"),("png","*.png")))
                path=Path(fileName)
                imageFileTXT.delete('1.0', END)
                imageFileTXT.insert(INSERT, path.name)
                shutil.copy(fileName,imgdir)
                img=PIL.Image.open(fileName)
                img=img.resize((100,100))
                render=ImageTk.PhotoImage(img,master=frameGUI)
                imageFileLBL.config(image=render)
                imageFileLBL.image = render
        Button(frameGUI, text="Image File Upload", command=imgFileUploadButtonEvent).grid(row=r1, column=2, sticky='NW')
        r1 += 1       
        imageFileLBL = Label(frameGUI, bg=bgcolor)
        imageFileLBL.grid(row=r1, column=2, sticky='NW') 
        #Date of Birth Calendar dialog
        r1 += 1
        Label(frameGUI, text="Date of Birth", bg=bgcolor).grid(row=r1, column=0, sticky='NE')
        dobTXT = Text(frameGUI, height=1, width=30)
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
                top = Toplevel(frameGUI)
                cal = Calendar(top,font="Arial 10",background='darkblue',foreground='white',selectmode='day')
                cal.grid()
                Button(top, text="OK", command=pickDateSelectionEvent).grid()
        Button(frameGUI, text="Select Date for DOB", command=selectDateButtonEvent).grid(row=r1, column=2, sticky='NW')
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
                   tk.messagebox.showinfo("MESSAGE", msg, parent=frame)
                else:
                   tk.messagebox.showinfo("MESSAGE", msg, parent=frame)
                #display records from database table
                sql = "select * from person"
                executeSelectQuery(sql)
        Button(frameGUI, text="Submit", width=20, command=submitButtonEvent).grid(row=r1, column=1, sticky='NW')
        #uniform padding for all controls on the frame 
        for widget in frameGUI.winfo_children():
                widget.grid(padx=10, pady=2)

        '''
        
#=============================================================================
# standalone start for code testing - to run this file independently
#=============================================================================
if __name__ == "__main__":
        rootframe = Tk()
        #index(rootframe)
        #datetimefunctions()
        getDateFromMySQLTable()
#=============================================================================

