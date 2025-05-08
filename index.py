from _libraryAndDBConnection import * #includes database connection and cursor setting strings
import _menu

#----------------------------
'''
Instructions:
-------------
1. Set database name in _libraryAndDBConnection.py file

2. Customize 'DROP TABLE', 'CREATE TABLE' and 'INSERT INTO' statements
   in _createMySQLTablesWithTestData.py file

3. Set menu options in _menu.py file with
   (1) tablename
   (2) primary key name
   (3) combobox/drop-down source table & column names
   (4) date column name [for calendar]
   (5) image column name [...to be implemented in future versions]
'''
#----------------------------


#====================================================================================
# rootframe (parent window) to be Tk ()
# rest others (child windows) to be Toplevel() or Frame()
#====================================================================================
#ROOT OR MAIN OR PARENT FRAME
rootframe = Tk() 
rootframe.title('clickzone management system') 
welcometext = ""
#maximize root window with title
w, h = rootframe.winfo_screenwidth(), rootframe.winfo_screenheight()-100
rootframe.geometry("%dx%d+0+0" % (w, h)) #root window size 'wxh' at left top coordinates 0,0
rootframe.configure(background="light grey",bd=-10)
#add background image to main root window using label after resizing the image to fit well within it
mywidth = rootframe.winfo_screenwidth() #-20
myheight = rootframe.winfo_screenheight()-80 #-100
#BACKGROUND IMAGE
img = Image.open("F:/11A62023/clickzone final/__CRUD Master Code 2024 - MASTER CODE/CLICKZONE.jpg") #read the image
resizeimg = img.resize((mywidth, myheight)) #resize the image
bgimg = ImageTk.PhotoImage(resizeimg) #set resized images as bg
#bgimglbl = Label(rootframe, image=bgimg) #place bg image in the label instead of text as in Label(frame, text="text")
bgimglbl = Label(rootframe, compound=tk.CENTER, text=welcometext, bd=-10, font='Helvetica 30 bold', fg='white', image=bgimg)
bgimglbl.grid(row=0, column=0, sticky=tk.E+tk.W) #place the label in the first row, first column of the main root window; centered by default
#place text field over the bg image at the top centered horizontally
#logo
'''
#logoimg = Image.open("bvmlogo.png") #logo image
#resizeimg = logoimg.resize((100, 100)) #resize the image
logoimg=PhotoImage(file="bvmlogo.png") #logo image
logoimglbl=Label(rootframe, height=2, image=logoimg, bg= "grey")
logoimglbl.grid(row=0, column=0, sticky='NEW')
'''
'''
topframe = Frame(rootframe, background='')
topframe.grid(row=0, column=0, sticky='NEW')
'''
'''
from tkinter import Canvas
#import ImageTk
t = Tk()
t.title("Transparency")
#frame = Frame(t)
frame = Frame(rootframe)
#frame.pack()
frame.grid(row=0, column=0, padx=(20,20), pady=(20,20), sticky='NE')
#canvas = Canvas(frame, bg="black", width=500, height=500)
#canvas.pack()
canvas = Canvas(rootframe, bg="black", width=500, height=500)
canvas.grid(row=0, column=0, padx=(20,20), pady=(20,20), sticky='NE')
photoimage = ImageTk.PhotoImage(file="bvmlogo.png")
canvas.create_image(150, 150, image=photoimage)
'''
#lbl.grid( padx=(padleft, padright), pady=(padtop, padbottom))
'''logoimg=Image.open('bvmlogo.png')# Load the image
logoresizedimg=logoimg.resize((75, 100))# Resize the image in the given (width, height)
logofinalimg=ImageTk.PhotoImage(logoresizedimg)# Conver the image in TkImage
logoimglbl=Label(rootframe, image=logofinalimg)# Display the image with label
logoimglbl.grid(row=0, column=0, padx=(20,20), pady=(20,20), sticky='NE')''' #set the label
'''
canvas = Canvas(rootframe, bg="black", width=75, height=100)
canvas.grid(row=0, column=0, padx=(20,20), pady=(20,20), sticky='NW')
canvas.create_image(75, 100, image=logofinalimg)
'''
#place text field over the bg image at the bottom centered horizontally

#---------------------------------------------
#GUI - App Menu
menubar = _menu.menu(rootframe)
#---------------------------------------------
#GUI - infinite main root loop
rootframe.config(menu=menubar)
rootframe.mainloop()
