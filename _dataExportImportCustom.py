from _reportDataAnalysisPlotCustomFunctions import *
#------------------------------------------------------------------------------------------------
global df #for reference from within many functions
#------------------------------------------------------------------------------------------------
#=============================================================================
def savedisplayedDFasCSVFileCustom(df):
    filetypes = [('CSV Files','*.csv')]
    saveatfilepath = asksaveasfile(mode='w', filetypes = filetypes, defaultextension=filetypes)
    df.to_csv(saveatfilepath, index=False,  lineterminator='\n') #use lineterminator to avoid blank lines in csv file
    # header=False
#=============================================================================
def dataExportItem(rootframe):
    
    global df

    frame = Toplevel()
    r = 1
    Label(frame, text=" ").grid(row=r, column=3, sticky='NE') #padding
    
    sql = "select * from item"
    df = executeSelectQueryAndReturnDF(frame, sql)

    r += 1
    Label(frame, text="Column to filter on:").grid(row=r, column=0, sticky='NE')
    colnames = df.columns.tolist()
    print(colnames)
    colnamesCBO = Combobox(frame, name='cols', width=30)
    colnamesCBO.grid(row=r, column=1)
    colnamesCBO['values'] = colnames
    colnamesCBO.current(0)
    #print(colnamesCBO.current(0))
    def colnamesCBOSelectedEvent(event):
            global df
            col = event.widget.get()
            sql = "SELECT DISTINCT "+col+" FROM item"
            #executeSelectQuery(frame, sql)
            df = executeSelectQueryAndReturnDF(frame, sql)
            valCBO['values'] = df[col].tolist()
    colnamesCBO.bind("<<ComboboxSelected>>", colnamesCBOSelectedEvent)
    
    r += 1    
    var = StringVar()
    #print(colnamesCBO.get())
    lookupvalues = df[colnamesCBO.get()]  
    Label(frame, text="Select Value:").grid(row=r, column=0, sticky='NE')
    valCBO = Combobox(frame, name='valcbo', width=30, textvariable=var)
    valCBO.grid(row=r, column=1)
    valCBO['values'] = lookupvalues
    valCBO.current(0)
    def valCBOSelectedEvent(event):
            global df
            val = event.widget.get()  #valcbo.get()
            sql = "SELECT * FROM item where "+colnamesCBO.get()+"='"+val+"'"
            df = executeSelectQueryAndReturnDF(frame, sql)
    valCBO.bind("<<ComboboxSelected>>", valCBOSelectedEvent)

    r += 1
    def saveDFasCSVFileCustomBtnClickEvent():
        global df
        savedisplayedDFasCSVFileCustom(df)
        msg = "CSV File saved."
        tk.messagebox.showinfo("MESSAGE", msg, parent=frame)  
    Button(frame, text='Save DF as CSV file', command=saveDFasCSVFileCustomBtnClickEvent).grid(row=r, column=1, sticky='W')

    Label(frame, text=" ").grid(row=3, column=3, sticky='NE') #padding




#=============================================================================
def dataExport(rootframe):
    
    global df

    frame = Toplevel()
    r = 1
    Label(frame, text=" ").grid(row=r, column=3, sticky='NE') #padding
    
    sql = "select * from trytbl"
    df = executeSelectQueryAndReturnDF(frame, sql)

    r += 1
    Label(frame, text="Column to filter on:").grid(row=r, column=0, sticky='NE')
    colnames = df.columns.tolist()
    print(colnames)
    colnamesCBO = Combobox(frame, name='cols', width=30)
    colnamesCBO.grid(row=r, column=1)
    colnamesCBO['values'] = colnames
    colnamesCBO.current(0)
    #print(colnamesCBO.current(0))
    def colnamesCBOSelectedEvent(event):
            global df
            col = event.widget.get()
            sql = "SELECT DISTINCT "+col+" FROM trytbl"
            #executeSelectQuery(frame, sql)
            df = executeSelectQueryAndReturnDF(frame, sql)
            valCBO['values'] = df[col].tolist()
    colnamesCBO.bind("<<ComboboxSelected>>", colnamesCBOSelectedEvent)
    
    r += 1    
    var = StringVar()
    #print(colnamesCBO.get())
    lookupvalues = df[colnamesCBO.get()]  
    Label(frame, text="Select Value:").grid(row=r, column=0, sticky='NE')
    valCBO = Combobox(frame, name='valcbo', width=30, textvariable=var)
    valCBO.grid(row=r, column=1)
    valCBO['values'] = lookupvalues
    valCBO.current(0)
    def valCBOSelectedEvent(event):
            global df
            val = event.widget.get()  #valcbo.get()
            sql = "SELECT * FROM trytbl where "+colnamesCBO.get()+"='"+val+"'"
            df = executeSelectQueryAndReturnDF(frame, sql)
    valCBO.bind("<<ComboboxSelected>>", valCBOSelectedEvent)

    r += 1
    def saveDFasCSVFileCustomBtnClickEvent():
        global df
        savedisplayedDFasCSVFileCustom(df)
        msg = "CSV File saved."
        tk.messagebox.showinfo("MESSAGE", msg, parent=frame)  
    Button(frame, text='Save DF as CSV file', command=saveDFasCSVFileCustomBtnClickEvent).grid(row=r, column=1, sticky='W')

    Label(frame, text=" ").grid(row=3, column=3, sticky='NE') #padding

#=============================================================================
# standalone start for code testing - to run this file independently
#=============================================================================
# param = {'table':['trytbl'],'pk':['trytblid'],'cbo':['trytbl.class']}
if __name__ == "__main__":
    rootframe = Tk()
    dataExport(rootframe)
#=============================================================================


