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
        tbl = 'product'
        try:
                cursor.execute('DROP TABLE product')
        except conn.Error as e:
                pass
        sql = """CREATE TABLE IF NOT EXISTS product(
                    productid int PRIMARY KEY AUTO_INCREMENT,
                    productname VARCHAR(30) ,
                    productcategory VARCHAR(30),
                    productunit int,
                    productfeatures varchar(100),
                    productcompany varchar(30),
                    warrantyperiod varchar(30)
                    )"""
        cursor.execute(sql)
        sql = """INSERT INTO product
                    (
                    productname,
                    productcategory,
                    productunit,
                    productfeatures,
                    productcompany,
                    warrantyperiod
                    )
                    values
                    ('nikon d7000','dslr',10,'this camera is good for professional photographer for weddings and other occaison',
                    'nikon','4years'),
                    ('canon c6','dslr','12','good for potrait','canon','2years'),
                    ('sony m6','dslr','9','good for potrait','sony','2years')
                    """
        cursor.execute(sql)
        tkmsgbox.showinfo("MESSAGE!", "product table created with test data.", parent=frame)
        #------------------------------------------------
        tbl = 'productcategory'
        try:
                cursor.execute('DROP TABLE productcategory')
        except conn.Error as e:
                pass
        sql = """CREATE TABLE IF NOT EXISTS productcategory(
                    productcategoryid int PRIMARY KEY AUTO_INCREMENT,
                    productcategory varchar(30)
                    )"""
        cursor.execute(sql)
        sql = """INSERT INTO productcategory
                    (
                    productcategoryid,
                    productcategory
                    )
                    values
                    (1,'dslr'),
                    (2,'slr'),
                    (3,'movie camera'),
                    (4,'tripod'),
                    (5,'other accesories')
                    """
        cursor.execute(sql)
        tkmsgbox.showinfo("MESSAGE!", "productcategory table created with test data.", parent=frame)
        #--------------------------------------------------
        tbl = 'supplier'
        try:
                cursor.execute('DROP TABLE supplier')
        except conn.Error as e:
                pass
        sql = """CREATE TABLE IF NOT EXISTS supplier(
                    supplierid INT PRIMARY KEY AUTO_INCREMENT,
                    suppliername VARCHAR(30),
                    suppliercountry varchar(30),
                    suppliercity varchar(30),
                    suppliercompany varchar(30),
                    suppliercategory varchar(30),
                    suppliercontact varchar(11),
                    supplierrating varchar(10)
                    )"""
        cursor.execute(sql)
        sql = """INSERT INTO supplier
                    (suppliername,
                    suppliercountry,
                    suppliercity,
                    suppliercompany,
                    suppliercategory,
                    suppliercontact,
                    supplierrating)
                    VALUES
                    ('sanju','India','delhi','nikon','wholeseller','9896754902','good'),
                    ('manju','india','mathura','canon','retailer','9897905678','good'),
                    ('seenu','india','mumbai','sony','retailer','8987905678','good')
                    """
        cursor.execute(sql)
        tkmsgbox.showinfo("MESSAGE!", "supplier table created with test data.", parent=frame)
        #------------------------------------------------
        tbl = 'coustomer'
        try:
                cursor.execute('DROP TABLE coustomer')
        except conn.Error as e:
                pass
        sql = """CREATE TABLE IF NOT EXISTS coustomer(
                    coustomerid int primary key AUTO_INCREMENT,
                    coustomername varchar(30),
                    coustomercity varchar(30),
                    coustomercountry varchar(30),
                    coustomermobile char(10),
                    coustomercategory varchar(10),	
                    coustomerrating varchar(10)
                    )"""
        cursor.execute(sql)
        sql = """INSERT INTO coustomer 
                    (coustomername,
                    coustomercity,
                    coustomercountry,
                    coustomermobile,
                    coustomercategory,	
                    coustomerrating
                    )
                    VALUES
                    ('Devyansh','delhi','india',9897282762,'for personal use','average'),
                    ('methu','nainital','india',9897277778,'for personal use','good'),
                    ('pawan','mumbai','india',677685778,'for personal use','good')
                    """
        cursor.execute(sql)
        tkmsgbox.showinfo("MESSAGE!", "coustomer table created with test data.", parent=frame)
        #------------------------------------------------
        tbl = 'replacementrefund'
        try:
                cursor.execute('DROP TABLE replacementrefund')
        except conn.Error as e:
                pass
        sql = """CREATE TABLE IF NOT EXISTS replacementrefund(
                    replacementrefundid INT PRIMARY KEY AUTO_INCREMENT,
                    productcode VARCHAR(30),
                    productname varchar(30),
                    coustomerid int,
                    coustomername varchar(20),
                    productcategory varchar(30)
                    )"""
        cursor.execute(sql)
        sql = """INSERT INTO replacementrefund
                    (
                    replacementrefundid,
                    productcode,
                    productname,
                    coustomerid,
                    coustomername,
                    productcategory
                    )
                    VALUES
                    (1,'123','d7000','123','shiv','dslr')
                    """
        cursor.execute(sql)
        tkmsgbox.showinfo("MESSAGE!", "replacement_refund table created with test data.", parent=frame)
        #------------------------------------------------
        tbl = 'sale'
        try:
                cursor.execute('DROP TABLE sale')
        except conn.Error as e:
                pass
        sql = """CREATE TABLE IF NOT EXISTS sale(
                    saleid int primary key auto_increment,
                    invoice varchar(10),
                    productname varchar(30),
                    productid int,
                    coustomerid int,
                    coustomername varchar(30),
                    productcategory varchar(30),
                    unitsell int,
                    warrantyperiod varchar(30),
                    transdate date,
                    saleprice int ,
                    gst int,
                    totalamount varchar(10),
                    gstamount varchar(10),
                    netamount varchar(10)
                    )"""
        cursor.execute(sql)
        tkmsgbox.showinfo("MESSAGE!", "sale table created", parent=frame)
        #------------------------------------------------
        tbl = 'purchase'
        try:
                cursor.execute('DROP TABLE purchase')
        except conn.Error as e:
                pass
        sql = """CREATE TABLE IF NOT EXISTS purchase(
                    purchaseid int primary key auto_increment,
                    invoice varchar(10),
                    productname varchar(30),
                    productid int,
                    supplierid int,
                    suppliername varchar(30),
                    suppliercity varchar(30),
                    productcategory varchar(30),
                    unitpurchase int,
                    netpurchaseprice int,
                    transdate date,
                    gst varchar(5),
                    totalamount varchar(10),
                    price varchar(10),
                    gstamount varchar(10)
                    )"""
        cursor.execute(sql)
        tkmsgbox.showinfo("MESSAGE!", "purchase table created", parent=frame)
        #------------------------------------------------
       
#------------------------------------------------
        tbl = 'companyname'
        try:
                cursor.execute('DROP TABLE companyname')
        except conn.Error as e:
                pass
        sql = """CREATE TABLE IF NOT EXISTS companyname(
                    companynameid int primary key auto_increment,
                    companyname varchar(30),
                    gstinvoice int
                    )"""
        cursor.execute(sql)
        sql = """INSERT INTO companyname
                    (
                    companynameid,
                    companyname,
                    gstinvoice
                    )
                    VALUES
                    (1,'clickzone',4534532)
                    """
        cursor.execute(sql)
        tkmsgbox.showinfo("MESSAGE!", "COMPANY NAME table created with test data.", parent=frame)

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
