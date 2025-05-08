import tkinter as tk
from tkinter import *
from tkinter import ttk 
import tkinter.messagebox as tkmsgbox
import pymysql
import pandas as pd
import numpy as np

def manual():
    frameHelp = Tk()
    r=0
    Label(frameHelp, height=10, width=50, text="start using by making tabels of your choice through new menu...").grid(row=r, column=0)
    frameHelp.mainloop()    
def help():
    frameHelp = Tk()
    r=0
    Label(frameHelp, height=10, width=50, text="try to undo the changes which you did before...").grid(row=r, column=0)
    frameHelp.mainloop()
def about():    
    frameHelp = Tk()
    r=0
    Label(frameHelp, height=10, width=50, text="this software is made by Devyansh Deopa and Pawan singh for class 12th project...").grid(row=r,column=5)
    frameHelp.mainloop()
def contact():
    frameHelp = Tk()
    r=0
    Label(frameHelp, height=10, width=50, text="for more query contact-deopadevyansh88@gmail.com").grid(row=r, column=0)
    frameHelp.mainloop()    
