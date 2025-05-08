from _reportDataAnalysisPlotCustomFunctions import *
#-----------------------------------------------------------------------------
# User Defined Reports
#-----------------------------------------------------------------------------
# report 1
#-----------------------------------------------------------------------------
def rptItemDetail(rootframe):
        frame = Toplevel()
        sql = "select * from product, coustomer"
        executeSelectQuery(frame, sql)

def rptsaleDetail(rootframe):
        frame = Toplevel()
        sql = "select * from sale"
        executeSelectQuery(frame, sql)

def rptpurchaseDetail(rootframe):
        frame = Toplevel()
        sql = "select * from purchase"
        executeSelectQuery(frame, sql)



#-----------------------------------------------------------------------------
# report 2
#-----------------------------------------------------------------------------
def rptItemDetailConditionalPickupList(rootframe):
        frame = Toplevel()
        sql = "select productname from product"
        df = executeSelectQueryAndReturnDF(frame, sql)
        # GUI 
        # drop-down/pick-up list
        Label(frame, text=" ").grid(row=1, column=1, sticky='NE')
        namevar = StringVar()
        namelookupvalues = df['productname'].tolist()
        Label(frame, text="product name").grid(row=2, column=1, sticky='NE')
        nameCBO = Combobox(frame, name='namecbo', width=30, textvariable=namevar)
        nameCBO.grid(row=2, column=2)
        nameCBO['values'] = namelookupvalues
        nameCBO.current(0)
        def nameCBOSelectedEvent(event):
                name = event.widget.get()
                sql = "SELECT * FROM product where productname='"+name+"'"
                executeSelectQuery(frame, sql)        
        nameCBO.bind("<<ComboboxSelected>>", nameCBOSelectedEvent)
        Label(frame, text=" ").grid(row=3, column=3, sticky='NE')
#-----------------------------------------------------------------------------
# report 3
#-----------------------------------------------------------------------------
def rptItemDetailConditionalTextbox(rootframe):
        frame = Toplevel()
        Label(frame, text=" ").grid(row=1, column=1, sticky='NE')
        Label(frame, text="SQL Query").grid(row=2, column=1, sticky='NE')
        sqlTXT = Entry(frame, width=30)
        sqlTXT.grid(row=2, column=2, sticky='NW')
        def clickButtonEvent():
                sql = sqlTXT.get()
                executeSelectQuery(frame, sql)        
        Button(frame, text="Submit", command=clickButtonEvent).grid(row=3, column=2, sticky='NW')
        Label(frame, text=" ").grid(row=4, column=3, sticky='NE')
        
#=============================================================================
# standalone start for code testing - to run this file independently
#=============================================================================
param = {'table':['product'],'pk':['productid'],'cbo':['productcategory.productcategory']}
if __name__ == "__main__":
        rootframe = Tk()
        #createSelectRootFrame(rootframe, param)
        #rptItemDetail(rootframe)                        # report 1
        #rptItemDetailConditionalPickupList(rootframe)       # report 2
        rptItemDetailConditionalTextbox(rootframe)          # report 3
        
#=============================================================================

