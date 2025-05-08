from sqlalchemy.types import VARCHAR
from sqlalchemy import create_engine
import pymysql
import pandas as pd
import numpy as np


def createtable():
        tbl = 'student'
        try:
            cursor.execute('DROP TABLE student')
        except conn.Error as e:
            pass
        try:
            sql = """CREATE TABLE IF NOT EXISTS student(
                    studentid INT PRIMARY KEY AUTO_INCREMENT,
                    academicsession VARCHAR(30),
                    roll VARCHAR(30) UNIQUE,
                    name VARCHAR(30),
                    class VARCHAR(30),
                    stream VARCHAR(30)
                    )"""
            cursor.execute(sql)
            print(tbl+" table created in the database "+db+".")
        except conn.Error as e:
            msg = "ERROR: "+str(e.args[0])+e.args[1]
            print("TABLE: "+tbl+"\n"+msg)

def insertintotable():
        try:
            sql = """INSERT INTO student 
                    (academicsession, roll,name,class)
                    VALUES
                    ('2023-24','1','Stud01','11A','PCM'),
                    ('2023-24','2','Stud02','11A','COM'),
                    ('2023-24','3','Stud03','12A','PCB'),
                    ('2023-24','4','Stud04','12A','COM'),
                    ('2023-24','5','Stud05','12C','PCM'),
                    ('2023-24','6','Stud06','11C','PCB')
                    """
            cursor.execute(sql)
            tkmsgbox.showinfo("MESSAGE!", "student table created with test data.", parent=frame)
        except conn.Error as e:
            msg = "ERROR: "+str(e.args[0])+e.args[1]
            tk.messagebox.showinfo("MESSAGE", "TABLE: "+tbl+"\n"+msg, parent=frame)



#Creating a dataframe
df = pd.read_csv("User_Download_03062021_140950.csv")
#printing the sample rows of the dataframe
print(df.head())
#database connectivity
#connection = pymysql.connect( host='localhost',user='root',password='',db='pythondb') #,cursorclass=pymysql.cursors.DictCursor)
sqlEngine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}".format(user="root",pw="",db="googlemeetlog"))
connection = sqlEngine.connect()
tableName="student"
try:
    frame = df.to_sql(tableName, connection, if_exists='replace', index=False);
except pymysql.Error as e:
    print("ERROR: %d: %s" %(e.args[0], e.args[1]))
else:
    print("Table %s created successfully."%tableName);   
finally:
    connection.close()



'''
from sqlalchemy.types import VARCHAR
from sqlalchemy import create_engine
import pymysql
import pandas as pd
import numpy as np

#Creating a dataframe
dftemp = pd.read_csv("KirtiGoogleMeetLog21Aug12Oct2020.csv")
#printing the sample rows of the dataframe
#print(dftemp.head())
df=dftemp[['Date','Meeting Code','Organizer Email','Duration','Participant Name']]
mymapper = {'Meeting Code':'MeetingCode','Organizer Email':'OrganizerEmail','Participant Name':'ParticipantName'}
df.rename(columns=mymapper, inplace=True)
print(df.head())

#database connectivity
#connection = pymysql.connect( host='localhost',user='root',password='',db='pythondb') #,cursorclass=pymysql.cursors.DictCursor)
sqlEngine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}".format(user="root",pw="",db="googlemeetlog"))
connection = sqlEngine.connect()
tableName="t1"
try:
    frame = df.to_sql(tableName, connection, if_exists='replace', index=False);
except pymysql.Error as e:
    print("ERROR: %d: %s" %(e.args[0], e.args[1]))
else:
    print("Table %s created successfully."%tableName);   
finally:
    connection.close()
'''
