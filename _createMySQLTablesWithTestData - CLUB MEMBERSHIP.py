from _libraryAndDBConnection import * #includes database connection and cursor setting strings
#=============================================================================
def createTablesWithTestData(frame):
    cursor = conn.cursor()    
    #Creating Tables with Test Data: CLUB


    #---- 1.  services
    #---- 2.  member
    #---- 3.  membercategory  
    #---- 4.  servicesavailed
    #---- 5.  paymentdemand
    #---- 6.  paymentsrecieved

    tbl = ''
    try:
        tkmsgbox.showinfo("MESSAGE!", "Creating tables with test data...", parent=frame)
        #================================================================
        # !IMPORTANT: date column should be named something
        # as 'transdate', 'pdate', 'sdate', 'doj' etc.
        # BUT NOT AS 'date'
        #================================================================
        tbl = 'member'
        try:
                cursor.execute('DROP TABLE member')
        except conn.Error as e:
                pass
        sql = """CREATE TABLE IF NOT EXISTS member(
                    memberid INT PRIMARY KEY AUTO_INCREMENT,
                    membercode VARCHAR(30) UNIQUE,
                    membername VARCHAR(30),
                    membermobile VARCHAR(10),
                    membercategory VARCHAR(30)
                    )"""
        cursor.execute(sql)
        sql = """INSERT INTO member
                    (membercode,membername,membermobile,membercategory)
                    VALUES
                    ('1','Member01','9411112345','Gold'),
                    ('2','Member02','9817612569','Gold'),
                    ('3','Member03','7891235490','Silver'),
                    ('4','Member04','9412189011','Gold'),
                    ('5','Member05','9413189022','Platinum')
                    """
        cursor.execute(sql)
        tkmsgbox.showinfo("MESSAGE!", "member table created with test data.", parent=frame)
        #------------------------------------------------
        tbl = 'membercategory'
        try:
                cursor.execute('DROP TABLE membercategory')
        except conn.Error as e:
                pass
        sql = """CREATE TABLE IF NOT EXISTS membercategory(
                    membercategoryid INT PRIMARY KEY AUTO_INCREMENT,
                    membercategory VARCHAR(30) UNIQUE
                    )"""
        cursor.execute(sql)
        sql = """INSERT INTO membercategory
                    (membercategory)
                    VALUES
                    ('Gold'),
                    ('Silver'),
                    ('Platinum')
                    """
        cursor.execute(sql)
        tkmsgbox.showinfo("MESSAGE!", "membercategory table created with test data.", parent=frame)
        #------------------------------------------------
        tbl = 'service'
        try:
                cursor.execute('DROP TABLE service')
        except conn.Error as e:
                pass
        sql = """CREATE TABLE IF NOT EXISTS service(
                    serviceid INT PRIMARY KEY AUTO_INCREMENT, 
                    servicecode VARCHAR(30) UNIQUE,
                    servicename VARCHAR(30),
                    servicecategory VARCHAR(30),
                    servicecharge DECIMAL(10,2) default 0,
                    serviceunit VARCHAR(30)
                    )"""
        cursor.execute(sql)
        sql = """INSERT INTO service 
                    (servicecode,servicename,servicecategory,servicecharge,serviceunit)
                    VALUES
                    ('1', 'Annual Subscription',    'S1',10000, 'No.'),
                    ('2', 'Monthly Subscription',   'S1',1000,  'No.'),
                    ('3', 'Service02',              'S2',200,   'Lt.'),
                    ('4', 'Service03',              'S2',150,   'Plate'),
                    ('5', 'Service04',              'S3',2500,  'Hr.'),
                    ('6', 'Service05',              'S4',4000,  'No.')
                    """
        cursor.execute(sql)
        tkmsgbox.showinfo("MESSAGE!", "service table created with test data.", parent=frame)
        #------------------------------------------------
        tbl = 'servicecategory'
        try:
                cursor.execute('DROP TABLE servicecategory')
        except conn.Error as e:
                pass
        sql = """CREATE TABLE IF NOT EXISTS servicecategory(
                    servicecategoryid INT PRIMARY KEY AUTO_INCREMENT,
                    servicecategory VARCHAR(30) UNIQUE
                    )"""
        cursor.execute(sql)
        sql = """INSERT INTO servicecategory
                    (servicecategory) 
                    VALUES
                    ('S1'),
                    ('S2'),
                    ('S3'),
                    ('Annual Subscription'),
                    ('Monthly Subscription')
                    """
        cursor.execute(sql)
        tkmsgbox.showinfo("MESSAGE!", "servicecategory table created with test data.", parent=frame)
        #------------------------------------------------
        tbl = 'serviceunit'
        try:
                cursor.execute('DROP TABLE serviceunit')
        except conn.Error as e:
                pass
        sql = """CREATE TABLE IF NOT EXISTS serviceunit(
                    serviceunitid INT PRIMARY KEY AUTO_INCREMENT,
                    serviceunit VARCHAR(30) UNIQUE
                    )"""
        cursor.execute(sql)
        sql = """INSERT INTO serviceunit
                    (serviceunit) 
                    VALUES
                    ('Lt.'),
                    ('No.'),
                    ('Kg'),
                    ('Plate'),
                    ('Hr.')
                    """
        cursor.execute(sql)
        tkmsgbox.showinfo("MESSAGE!", "serviceunit table created with test data.", parent=frame)
        #------------------------------------------------
        tbl = 'serviceavailed'
        try:
                cursor.execute('DROP TABLE serviceavailed')
        except conn.Error as e:
                pass
        sql = """CREATE TABLE IF NOT EXISTS serviceavailed(
                    serviceavailedid INT PRIMARY KEY AUTO_INCREMENT,
                    sadate DATE,
                    serviceinvoice VARCHAR(30),
                    memberid INT,
                    membercode VARCHAR(30),
                    membername VARCHAR(30),
                    membermobile VARCHAR(30),
                    membercategory VARCHAR(30),
                    serviceid INT,
                    servicecode VARCHAR(30),
                    servicename VARCHAR(30),
                    servicecategory VARCHAR(30),
                    servicecharge DECIMAL(10,2),
                    serviceunit VARCHAR(30),
                    serviceunitsavailed DECIMAL(10,2),
                    amount DECIMAL(10,2),
                    amountpaidsofar DECIMAL(10,2) DEFAULT 0
                    )"""
        cursor.execute(sql)
        tkmsgbox.showinfo("MESSAGE!", "serviceavailed table created with test data.", parent=frame)
        #------------------------------------------------
        tbl = 'paymentmade'
        try:
                cursor.execute('DROP TABLE paymentmade')
        except conn.Error as e:
                pass
        sql = """CREATE TABLE IF NOT EXISTS paymentmade(
                    paymentmadeid INT PRIMARY KEY AUTO_INCREMENT,
                    pdate DATE,
                    paymentinvoice VARCHAR(30),
                    serviceinvoice VARCHAR(30),
                    memberid INT,
                    membercode VARCHAR(30),
                    membername VARCHAR(30),
                    membercategory VARCHAR(30),
                    serviceid INT,
                    servicecode VARCHAR(30),
                    servicename VARCHAR(30),
                    servicecategory VARCHAR(30),
                    servicecharge DECIMAL(10,2),
                    serviceunit VARCHAR(30),
                    serviceunitsavailed DECIMAL(10,2),
                    amount DECIMAL(10,2),
                    paymentamount DECIMAL(10,2) DEFAULT 0
                    )"""
        cursor.execute(sql)
        tkmsgbox.showinfo("MESSAGE!", "paymentmade table created with test data.", parent=frame)
        #------------------------------------------------
        tkmsgbox.showinfo("SUCCESS MESSAGE!","ALL tables created successfully with dummy values.", parent=frame)
    except conn.Error as e:
                msg = "ERROR: "+str(e.args[0])+e.args[1]
                tk.messagebox.showinfo("MESSAGE", "TABLE: "+tbl+"\n"+msg, parent=frame)
#=============================================================================
# standalone start
#=============================================================================
if __name__ == "__main__":
    rootframe = Tk() 
    createDatabaseFrame(rootframe)
#=============================================================================
