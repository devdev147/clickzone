from sqlalchemy.types import VARCHAR
from sqlalchemy import create_engine
import pymysql
import pandas as pd
import numpy as np


def createtable():
        tbl = 'trytbl'
        try:
            cursor.execute('DROP TABLE '+tbl)
        except conn.Error as e:
            pass
        try:
            sql = """CREATE TABLE IF NOT EXISTS """+tbl+"""(
                    studentid INT PRIMARY KEY AUTO_INCREMENT,
                    academicsession VARCHAR(30),
                    roll VARCHAR(30) UNIQUE,
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
            print(tbl+" table created in the database "+db+".")
        except conn.Error as e:
            msg = "ERROR: "+str(e.args[0])+e.args[1]
            print("TABLE: "+tbl+"\n"+msg)

def insertintotable():
        tbl = 'trytbl'
        try:
            sql = """INSERT INTO """+tbl+"""
                    (academicsession, roll,name,class,stream,subject,examname)
                    VALUES
                    ('2023-24','1','Stud01','11A','PCM','UT1','Eng','70'),
                    ('2023-24','2','Stud02','11A','COM','UT1','Eng','70'),
                    ('2023-24','3','Stud03','12A','PCB','UT1','Eng','70'),
                    ('2023-24','4','Stud04','12A','COM','UT1','Eng','70'),
                    ('2023-24','5','Stud05','12C','PCM','UT1','Eng','70'),
                    ('2023-24','1','Stud01','11A','PCM','UT1','Hindi','80'),
                    ('2023-24','2','Stud02','11A','COM','UT1','Hindi','80'),
                    ('2023-24','3','Stud03','12A','PCB','UT1','Hindi','80'),
                    ('2023-24','4','Stud04','12A','COM','UT1','Hindi','80'),
                    ('2023-24','5','Stud05','12C','PCM','UT1','Hindi','80'),
                    ('2023-24','1','Stud01','11A','PCM','UT1','Math','100'),
                    ('2023-24','2','Stud02','11A','COM','UT1','Math','100'),
                    ('2023-24','3','Stud03','12A','PCB','UT1','Math','100'),
                    ('2023-24','4','Stud04','12A','COM','UT1','Math','100'),
                    ('2023-24','5','Stud05','12C','PCM','UT1','Math','100')
                    """
            cursor.execute(sql)
            tkmsgbox.showinfo("MESSAGE!", tbl+" table created with test data.", parent=frame)
        except conn.Error as e:
            msg = "ERROR: "+str(e.args[0])+e.args[1]
            tk.messagebox.showinfo("MESSAGE", "TABLE: "+tbl+"\n"+msg, parent=frame)

def mysql2df(table, columns='*', condition='1=1'):
        try:
                sql = "select "+columns+" from "+table+" where "+condition
                #cursor = conn.cursor()
                cursor.execute(sql)
                data = cursor.fetchall()
                df = pd.DataFrame(data)
                return df
        except conn.Error as e:
                print("ERROR: "+str(e.args[0])+e.args[1])
                           

def csv2df():
    df = pd.read_csv("student.csv")
    print(df.head())

def df2mysql():
    try:
        user = 'root'
        password = ''
        database = 'mastertrans2022'
        table = 'student'
        sqlEngine = create_engine("mysql+pymysql://{user}:{pwd}@localhost/{db}".format(user,password,database))
        connection = sqlEngine.connect()
        df.to_sql(table, connection, if_exists='replace', index=False);
    except pymysql.Error as e:
        print("ERROR: %d: %s"%(e.args[0],e.args[1]))
    else:
        print(table+" created successfully.");   
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
