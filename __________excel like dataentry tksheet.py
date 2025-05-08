from _libraryAndDBConnection import * #includes database connection and cursor setting strings
from tksheet import Sheet
'''
import tkinter as tk
from tkinter import filedialog
import csv
from os.path import normpath
import io
import pandas as pd
'''

def resultsheet():
    tbl = "trytbl"
    cols = ['roll','name','class','stream','examname']
    condition = "examname='UT1'"
    
    #subjects = ['Eng','Hindi','Math']
    try:
        #sql = "select "+cols+" from "+table+" where "+condition
        #cursor = conn.cursor()

        '''
        # converting 2d result sheet to single subject column based marks
        sql = "select roll,name,'Eng' as subject, eng as marksobtained from trytbl"
        sql += " UNION ALL "
        sql = "select roll,name,'Hindi' as subject, hindi as marksobtained from trytbl"
        sql += " UNION ALL "
        sql = "select roll,name,'Math' as subject, math as marksobtained from trytbl"
        '''

        # converting single column subject based marks to 2d result sheet with different subects as different columns
        sql = '''select roll,name,
                (select marksobtained from trytbl as teng where teng.roll=t.roll and teng.subject='eng' and teng.examname='UT1') as 'Eng',
                (select marksobtained from trytbl as thindi where thindi.roll=t.roll and thindi.subject='hindi' and thindi.examname='UT1') as 'Hindi'
                 from trytbl as t
                 group by roll
                 order by roll;
                 '''
        cursor.execute(sql)
        data = cursor.fetchall()
        df = pd.DataFrame(data)
        print(df)
        #return df
        idx = df.index
        cols = df.columns
        print("df.index: ",idx)
        print("df.columns: ",cols)
        print("First column in df: ",df[cols[0]])
        print("First row in df: ",df.loc[idx[0]])
        mylist = []
        mylist.append(df.columns.tolist())
        for i in idx:
            templist = df.loc[idx[i]].tolist()
            mylist.append(templist)
        print("mylist: ",mylist)
        return mylist

    except conn.Error as e:
        print("ERROR: "+str(e.args[0])+e.args[1]+"   TABLE: "+tbl)
    
    


def createtable():
        tbl = 'trytbl'
        try:
            cursor.execute("DROP TABLE "+tbl)
        except conn.Error as e:
            print("ERROR: "+str(e.args[0])+e.args[1]+"   TABLE: "+tbl)
        try:
            #CREATE TABLE IF NOT EXISTS """+tbl+"""(
            #studentid INT PRIMARY KEY AUTO_INCREMENT,
            sql = """CREATE TABLE """+tbl+"""(
                    studentid INT,
                    academicsession VARCHAR(30),
                    roll VARCHAR(30),
                    name VARCHAR(30),
                    class VARCHAR(30),
                    stream VARCHAR(30),
                    examname VARCHAR(30),
                    subject VARCHAR(30),
                    maxmarks VARCHAR(30),
                    marksobtained VARCHAR(30),
                    percent VARCHAR(30)
                    )"""
            cursor.execute(sql)
            print(tbl+" table created in the database.")
        except conn.Error as e:
            print("ERROR: "+str(e.args[0])+e.args[1]+"   TABLE: "+tbl)

def insertintotable():
        tbl = 'trytbl'
        try:
            sql = """INSERT INTO """+tbl+"""
                    (studentid,academicsession,roll,name,class,stream,examname,subject,maxmarks)
                    VALUES
                    (1,'2023-24','1','Stud01','11A','PCM','UT1','Eng','70'),
                    (2,'2023-24','2','Stud02','11A','COM','UT1','Eng','70'),
                    (3,'2023-24','3','Stud03','12A','PCB','UT1','Eng','70'),
                    (4,'2023-24','4','Stud04','12A','COM','UT1','Eng','70'),
                    (5,'2023-24','5','Stud05','12C','PCM','UT1','Eng','70'),
                    (1,'2023-24','1','Stud01','11A','PCM','UT1','Hindi','80'),
                    (2,'2023-24','2','Stud02','11A','COM','UT1','Hindi','80'),
                    (3,'2023-24','3','Stud03','12A','PCB','UT1','Hindi','80'),
                    (4,'2023-24','4','Stud04','12A','COM','UT1','Hindi','80'),
                    (5,'2023-24','5','Stud05','12C','PCM','UT1','Hindi','80'),
                    (1,'2023-24','1','Stud01','11A','PCM','UT1','Math','100'),
                    (2,'2023-24','2','Stud02','11A','COM','UT1','Math','100'),
                    (3,'2023-24','3','Stud03','12A','PCB','UT1','Math','100'),
                    (4,'2023-24','4','Stud04','12A','COM','UT1','Math','100'),
                    (5,'2023-24','5','Stud05','12C','PCM','UT1','Math','100')
                    """
            cursor.execute(sql)
            conn.commit()
            print("SUCCESS!", tbl+" table created with test data.")
        except conn.Error as e:
            print("ERROR: "+str(e.args[0])+e.args[1]+"   TABLE: "+tbl)





def mysql2dfcomplete(table='trytbl', columns='*', condition='1=1'):
        try:
                sql = "select * from "+table
                #cursor = conn.cursor()
                cursor.execute(sql)
                data = cursor.fetchall()
                df = pd.DataFrame(data)
                return df
        except conn.Error as e:
                print("ERROR: "+str(e.args[0])+e.args[1]+"   TABLE: "+tbl)


def mysql2df(table, columns='*', condition='1=1'):
        try:
                sql = "select "+columns+" from "+table+" where "+condition
                #cursor = conn.cursor()
                cursor.execute(sql)
                data = cursor.fetchall()
                df = pd.DataFrame(data)
                return df
        except conn.Error as e:
                print("ERROR: "+str(e.args[0])+e.args[1]+"   TABLE: "+tbl)


def mysql2listoflists(tbl='trytbl',columns='*',condition='1=1'):
    try:
        sql = "select "+columns+" from "+tbl+" where "+condition
        print(sql)
        #cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        df = pd.DataFrame(data)
        print("DF: \n",df)
        #return df
        idx = df.index
        cols = df.columns
        print("df.index: ",idx)
        print("df.columns: ",cols)
        print("First column in df: ",df[cols[0]])
        print("First row in df: ",df.loc[idx[0]])
        mylist = []
        mylist.append(df.columns.tolist())
        for i in idx:
            templist = df.loc[idx[i]].tolist()
            mylist.append(templist)
        print("mylist: ",mylist)
        return mylist
    except conn.Error as e:
        print("ERROR: "+str(e.args[0])+e.args[1]+"   TABLE: "+tbl)
        
class demo(tk.Tk):
    def __init__(self, mydata):
        tk.Tk.__init__(self)
        self.withdraw()
        self.title("tksheet")
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 1)
        self.frame = tk.Frame(self)
        self.frame.grid_columnconfigure(0, weight = 1)
        self.frame.grid_rowconfigure(0, weight = 1)
        #names = ['name1','name2','name3','name4','name5','name6','name7']
        #marks = [0,0,0,0,0,0,0]
        #mydata = [names,marks]
        self.sheet = Sheet(self.frame,data = mydata)
        #self.sheet.header(newheaders = 0) #first row to be header
        self.sheet.enable_bindings("all", "edit_header", "edit_index")
        self.frame.grid(row = 0, column = 0, sticky = "nswe")
        self.sheet.grid(row = 0, column = 0, sticky = "nswe")
        self.sheet.popup_menu_add_command("Open csv", self.open_csv)

        self.sheet.popup_menu_add_command("save sheet as list of lists", self.save_sheet_as_list_of_lists)


        self.sheet.popup_menu_add_command("Save sheet as CSV", self.save_sheet)

        self.sheet.popup_menu_add_command("Save Resultsheet in MySQL Database", self.save_resultsheet)


        self.sheet.popup_menu_add_command("Save this sheet as Excel (.xlsx) file", self.save_sheet_as_xlsx_file)
        
        


        
        self.sheet.set_all_cell_sizes_to_text()
        self.sheet.change_theme("light green")
        
        # center the window and unhide
        self.update_idletasks()
        w = self.winfo_screenwidth() - 20
        h = self.winfo_screenheight() - 70
        size = (900, 500)
        x = (w/2 - size[0]/2)
        y = h/2 - size[1]/2
        self.geometry("%dx%d+%d+%d" % (size + ((w/2 - size[0]/2), h/2 - size[1]/2)))
        self.deiconify()


    def save_resultsheet(self):
        mylist = self.sheet.get_sheet_data(
               get_displayed = False, 
               get_header = False,
               get_index = False,
               get_index_displayed = True,
               get_header_displayed = True,
               only_rows = None,
               only_columns = None)
        print(mylist)
        savedf = pd.DataFrame(mylist[1:])#, columns=)
        savedf.columns = mylist[0]
        print(savedf)
        #update mysql table
        tbl = 'trytbl'
        pkcol = 'roll'
        col = 'marksobtained'
        condcol = 'subject'
        condvals = ['Eng','Hindi']
        for i in range(len(savedf.index)):
            for j in condvals:
                if savedf.iloc[i][j] is not None:
                    sqlupdate = "UPDATE "+ tbl +" SET "+ col +"='"+ savedf.iloc[i][j] + \
                        "', percent=round("+str(savedf.iloc[i][j])+"/maxmarks*100,1)" \
                        " WHERE "+ pkcol +"='"+ str(savedf.iloc[i][pkcol]) +"'" \
                        " and "+ condcol +"='"+ j +"'"
                    print(sqlupdate)
                    try:
                        cursor.execute(sqlupdate)
                        conn.commit()
                        #print("SUCCESS: Master table updated successfully.")
                    except conn.Error as e:
                        print("ERROR: Master table could not be updated.\n"+str(e.args[0])+e.args[1])
        print("SUCCESS: Master table updated successfully.")


    def save_sheet_as_xlsx_file(self):

               mylist = self.sheet.get_sheet_data(
               get_displayed = False, 
               get_header = False,
               get_index = False,
               get_index_displayed = True,
               get_header_displayed = True,
               only_rows = None,
               only_columns = None)
               savedf = pd.DataFrame(mylist[1:])#, columns=)
               savedf.columns = mylist[0]
               savedf.to_excel("tksheet.xlsx")

    def save_sheet_as_list_of_lists(self):

        d = self.sheet.data
        print(d)
        
        mylist = self.sheet.get_sheet_data(
               get_displayed = False, 
               get_header = False,
               get_index = False,
               get_index_displayed = True,
               get_header_displayed = True,
               only_rows = None,
               only_columns = None)
        print(mylist)
        savedf = pd.DataFrame(mylist[1:])#, columns=)
        savedf.columns = mylist[0]

        #savedf['percent']=savedf['marksobtained'].astype(int)/savedf['maxmarks'].astype(int)*100
        
        #savedf.columns = savedf.iloc[0] #make first row as column header of dataframe
        #savedf = savedf[1:]
        print(savedf)
        #insert into mysql table
        '''
                    sql = "INSERT INTO "+ table[0] +"("
                    for c in cols:
                            sql += c+","
                    sql = sql[:-1]
                    sql += ") VALUES("
                    for v in vals:
                            sql += "'"+v+"',"
                    sql = sql[:-1]
                    sql += ")" 

                    print("INSERT SQL QUERY: ",sql)

                    try:
                            cursor.execute(sql)
                            #cursor.execute(sql1)
                            conn.commit()
                            msg = "SUCCESS: TRANSACTION (INSERT SQL query) executed successfully."
                            #tk.messagebox.showinfo("MESSAGE", msg, parent=frame)
                    except conn.Error as e:
                            msg = "ERROR: "+str(e.args[0])+e.args[1]
                            tk.messagebox.showinfo("MESSAGE", msg, parent=frame)

        '''

        #update mysql table
        tbl = 'trytbl'
        pkcol = 'studentid'
        col = 'marksobtained'
        condcol = 'subject'
        for i in range(len(savedf.index)):
            if savedf.iloc[i][col] is not None:
                sqlupdate = "UPDATE "+ tbl +" SET "+ col +"='"+ savedf.iloc[i][col] + \
                        "', percent='"+ str(round(int(savedf.iloc[i][col])/int(savedf.iloc[i]['maxmarks'])*100,1)) +"'" \
                        " WHERE "+ pkcol +"='"+ str(savedf.iloc[i][pkcol]) +"'" \
                        " and "+ condcol +"='"+ savedf.iloc[i][condcol] +"'"
                print(sqlupdate)
                try:
                    cursor.execute(sqlupdate)
                    conn.commit()
                    #print("SUCCESS: Master table updated successfully.")
                except conn.Error as e:
                    print("ERROR: Master table could not be updated.\n"+str(e.args[0])+e.args[1])
        print("SUCCESS: Master table updated successfully.")
                                                    
        '''
                                                    #print(exp)
                                            sql1 = "UPDATE "+ table +" SET "+ col +"='"+ exp + \
                                                   "' WHERE "+ pkCol +"='"+ globals()[pkCol].get() +"'"
                                            print(sql1)                    
                                            try:
                                                    #####cursor.execute(sql)
                                                    cursor.execute(sql1)
                                                    conn.commit()
                                                    msg = "SUCCESS: Master table updated successfully."
                                                    tk.messagebox.showinfo("MESSAGE", msg, parent=frame)
                                            except conn.Error as e:
                                                    msg = "ERROR: Master table could not be updated.\n"+str(e.args[0])+e.args[1]
                                                    tk.messagebox.showinfo("MESSAGE", msg, parent=frame)        
        '''

        
        
    def save_sheet(self):
        '''
        mylist = self.sheet.get_sheet_data(get_displayed = False, 
               get_header = False,
               get_index = False,
               get_index_displayed = True,
               get_header_displayed = True,
               only_rows = None,
               only_columns = None)
        print(mylist)
        '''
        filepath = filedialog.asksaveasfilename(parent = self,
                                                title = "Save sheet as",
                                                filetypes = [('CSV File','.csv'),
                                                             ('TSV File','.tsv')],
                                                defaultextension = ".csv",
                                                confirmoverwrite = True)
        if not filepath or not filepath.lower().endswith((".csv", ".tsv")):
            return
        try:
            with open(normpath(filepath), "w", newline = "", encoding = "utf-8") as fh:
                writer = csv.writer(fh,
                                    dialect = csv.excel if filepath.lower().endswith(".csv") else csv.excel_tab,
                                    lineterminator = "\n")
                writer.writerows(self.sheet.get_sheet_data(get_header = False, get_index = False))
        except:
            return
                
    def open_csv(self):
        filepath = filedialog.askopenfilename(parent = self, title = "Select a csv file")
        if not filepath or not filepath.lower().endswith((".csv", ".tsv")):
            return
        try:
            with open(normpath(filepath), "r") as filehandle:
                filedata = filehandle.read()
            self.sheet.set_sheet_data([r for r in csv.reader(io.StringIO(filedata),
                                                             dialect = csv.Sniffer().sniff(filedata),
                                                             skipinitialspace = False)])
        except:
            return

#=====================================================================
# FUNCTION CALLS
#=====================================================================
'''                          
createtable()
insertintotable()
'''

'''
mydata = mysql2listoflists()
#app = demo()
app = demo(mydata)
app.mainloop()
'''

print(mysql2dfcomplete())  #print entire dataframe
mydata1 = resultsheet()
app = demo(mydata1)
app.mainloop()

