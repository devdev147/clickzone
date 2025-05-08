from fpdf import FPDF
from _reportDataAnalysisPlotCustomFunctions import *  #to create df from SQL data
#=============================================================================
# pdf.cell(width, height, text='', border=0, ln=0, align='', fill=0, link='')
#=============================================================================
def pageHeader(pdf):
    # header - business info
    pdf.image('F:/11A62023/2024 crud gui/__CRUD Master Code 2024 - MASTER CODE/sanjay.jpg', 10, 8, 33)  
    pdf.set_font('Arial', 'B', 12)
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'Clickzone Managementsystem', 0, 1, 'C')
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, 'DWARKA', 0, 1, 'C')
    pdf.cell(0, 10, 'DELHI, 111001', 0, 1, 'C')
    pdf.cell(0, 10, 'Phone: 898980766', 0, 1, 'C')
    pdf.cell(0, 10, 'Email: devbusiness@gmail.com', 0, 1, 'C')
    pdf.ln(10)
def pageTitle(pdf):
    # title
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, "sale list", 0, 1, 'L')
    pdf.ln(5)
def nonRepetativeData(pdf, df, parampdf):
    # body - client info (non-repetative data)
    for i in parampdf['nonRepetativeColumns']:     #['roll', 'name', 'class']
        pdf.set_font('Arial', '', 12)
        pdf.cell(30, 10, i, 0, 0, 'L')
        pdf.cell(30, 10, str(df.loc[0,i]), 0, 0, 'L')
        pdf.ln()        
def repetativeData(pdf, df, parampdf):
    # body - client info (repetative data in Tabular format)
    # parampdf['repetativeColumns'] = {'colname':'examname', 'colheader':'exam\nname', 'colwidth':50, 'colheight':5, 'colalign':'L'}
    # parampdf['sum'] = {'sumcolname':'percent'},

    # ---------- table header
    pdf.set_fill_color(0, 225, 0) #column header fill color
    for i in range(len(parampdf['repetativeColumns'])):
        running_x   = pdf.get_x()
        initial_y   = pdf.get_y()
        colwidth    = parampdf['repetativeColumns'][i]['colwidth']
        colheight   = parampdf['repetativeColumns'][i]['colheight']
        colheader   = parampdf['repetativeColumns'][i]['colheader']
        pdf.multi_cell(w=colwidth, h=colheight, txt=colheader.upper(), border=1, align='C', split_only=False, fill=True)
        running_x  += colwidth
        pdf.set_xy(running_x, initial_y)
    pdf.ln()
    
    # ---------- table data
    height = 10
    initial_y = pdf.get_y()
    running_x = pdf.get_x()
    total = 0.0
    for row in range(len(df.index.tolist())):
        for i in range(len(parampdf['repetativeColumns'])):
            colname     = parampdf['repetativeColumns'][i]['colname']
            colwidth    = parampdf['repetativeColumns'][i]['colwidth']
            colalign    = parampdf['repetativeColumns'][i]['colalign']
            if df.loc[row, colname] is None:
                pdf.cell(colwidth, height, "-", 1, 0, 'L')
            else:
                pdf.cell(colwidth, height, str(df.loc[row, colname]), 1, 0, colalign)
                if len(parampdf['sumcol'])>0:
                    #if colname==parampdf['sumcol'][0]:
                    if colname in parampdf['sumcol']:
                        total += float(df.loc[row, colname])
            globals()['total'+colname] = total
        pdf.ln()

    # ---------- summary data row
    if len(parampdf['sumcol'])>0:
        height = 15
        width = 0
        for i in range(len(parampdf['repetativeColumns'])-1):
            width += parampdf['repetativeColumns'][i]['colwidth']
        pdf.set_font('Arial', 'B', 12)
        for col in parampdf['sumcol']:            
            pdf.cell(width, height, 'TOTAL '+col.upper(), 1)
            pdf.cell(parampdf['repetativeColumns'][-1]['colwidth'], height, str(globals()['total'+col]), 1, 0, 'R')
            pdf.ln()
    
def customCalculation(pdf, df, parampdf):        
    # finally, add summary rows to the table
    totalmarks = 0.0
    for row in range(len(df.index.tolist())):
        if df.loc[row,'percent'] is None:
            pass
        else:
            totalmarks = totalmarks + float(df.loc[row,'percent'])
    height = 15
    width = 0
    for i in range(len(parampdf['repetativeColumns'])-1):
        width += parampdf['repetativeColumns'][i]['colwidth']
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(width, height, 'Total Marks', 1)
    pdf.cell(parampdf['repetativeColumns'][-1]['colwidth'], height, str(totalmarks), 1, 0, 'R')
    pdf.ln()
def savePDF(frame, pdf):
    # Save PDF
    pdf.output('salelist.pdf')
    tk.messagebox.showinfo("MESSAGE", "sale list - PDF file generated", parent=frame)  

def generatePDF(frame, df, parampdf):
    # master function coordinating PDF page elements
    pdf = FPDF(orientation='L', unit='mm', format='A4')
    pdf.add_page()
    pageHeader(pdf)
    pageTitle(pdf)
    nonRepetativeData(pdf, df, parampdf)
    repetativeData(pdf, df, parampdf)
    #customCalculation(pdf, df, parampdf)
    savePDF(frame, pdf)
#=============================================================================
def index(frame, parampdf):
    global df
    frame = Toplevel()
    r = 1
    sql = "select * from "+parampdf['table']
    df = executeSelectQueryAndReturnDF(frame, sql)
    r += 1
    # Create combobox of table columns
    Label(frame, text="Column to filter on:").grid(row=r, column=0, sticky='NE')
    colnames = df.columns.tolist()
    colnamesCBO = Combobox(frame, name='cols', width=30)
    colnamesCBO.grid(row=r, column=1)
    colnamesCBO['values'] = colnames
    colnamesCBO.current(0)
    def colnamesCBOSelectedEvent(event):
            global df
            col = event.widget.get()
            sql = "SELECT DISTINCT "+col+" FROM "+parampdf['table']
            df = executeSelectQueryAndReturnDF(frame, sql)
            valCBO['values'] = df[col].tolist()
    colnamesCBO.bind("<<ComboboxSelected>>", colnamesCBOSelectedEvent)
    r += 1    
    # Create combobox of distinct values of the selected column
    var = StringVar()
    lookupvalues = df[colnamesCBO.get()]  
    Label(frame, text="Select Value:").grid(row=r, column=0, sticky='NE')
    valCBO = Combobox(frame, name='valcbo', width=30, textvariable=var)
    valCBO.grid(row=r, column=1)
    valCBO['values'] = lookupvalues
    valCBO.current(0)
    def valCBOSelectedEvent(event):
            global df
            val = event.widget.get()  #valcbo.get()
            sql = "SELECT * FROM "+parampdf['table']+" where "+colnamesCBO.get()+"='"+val+"' and "+parampdf['condition']
            df = executeSelectQueryAndReturnDF(frame, sql)
    valCBO.bind("<<ComboboxSelected>>", valCBOSelectedEvent)
    r += 1
    # Create button to generate PDF
    def GeneratePDFFileBtnClickEvent():
        global df
        generatePDF(frame, df, parampdf)
    Button(frame, text='Generate PDF file', command=GeneratePDFFileBtnClickEvent).grid(row=r, column=1, sticky='W')
    Label(frame, text=" ").grid(row=3, column=3, sticky='NE') #padding

    
#=============================================================================
# standalone start for code testing - to run this file independently
#=============================================================================
parampdf = {'table':'trytbl',
            'condition':'1=1',
            'nonRepetativeColumns':['roll', 'name', 'class'],
            'repetativeColumns':[
                                {'colname':'examname',      'colheader':'exam\nname',       'colwidth':50,  'colheight':5,  'colalign':'L'},
                                {'colname':'subject',       'colheader':'subject',          'colwidth':50,  'colheight':10, 'colalign':'L'},
                                {'colname':'maxmarks',      'colheader':'max\nmarks',       'colwidth':30,  'colheight':5,  'colalign':'C'},
                                {'colname':'marksobtained', 'colheader':'marks\nobtained',  'colwidth':30,  'colheight':5,  'colalign':'C'},
                                {'colname':'percent',       'colheader':'percent',          'colwidth':30,  'colheight':10, 'colalign':'R'},
                                ],
            'sumcol': ['percent',],
            }
if __name__ == "__main__":
    rootframe = Tk()
    index(rootframe, parampdf)
#=============================================================================



