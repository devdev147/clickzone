from fpdf import FPDF
from _reportDataAnalysisPlotCustomFunctions import *  #to create df from SQL data
#=============================================================================
# pdf.cell(width, height, text='', border=0, ln=0, align='', fill=0, link='')
#=============================================================================
def generatePDF(frame, df):
    pdf = FPDF(orientation='L', unit='mm', format='A4')
    pdf.add_page()
    # header - business info
    pdf.image('bvmlogo.png', 10, 8, 33)  
    pdf.set_font('Arial', 'B', 12)
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'Birla Vidya Mandir, Nainital', 0, 1, 'C')
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, 'Nainital', 0, 1, 'C')
    pdf.cell(0, 10, 'Uttarakhand, 263001', 0, 1, 'C')
    pdf.cell(0, 10, 'Phone: (05942) 235370', 0, 1, 'C')
    pdf.cell(0, 10, 'Email: info@birlavidyamandir.com', 0, 1, 'C')
    pdf.ln(10)
    # title
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, "Report Card", 0, 1, 'L')
    pdf.ln(5)
    # body - client info (non-repetative data)
    # roll, name, class
    pdf.set_font('Arial', '', 12)
    pdf.cell(30, 10, 'Roll:', 0, 0, 'L')
    pdf.cell(30, 10, df.loc[0,'roll'], 0, 0, 'L')
    pdf.ln()
    pdf.cell(30, 10, 'Name: ', 0, 0, 'L')
    pdf.cell(30, 10, df.loc[0,'name'], 0, 0, 'L')
    pdf.ln()
    pdf.cell(30, 10, 'Class: ', 0, 0, 'L')
    pdf.cell(30, 10, df.loc[0,'class'], 0, 0, 'L')
    pdf.ln()
    # body - client info (repetative transaction data)
    # ---------- table header
    pdf.set_fill_color(0, 225, 0) # fill table header row; cell will be filled with this color if its last parameter is '1'
    initial_y = pdf.get_y()
    pdf.multi_cell(w=50, h=10, txt="Exam", border=1, align='C', split_only=False, fill=True) # Draw the first multi-cell
    pdf.set_xy(pdf.get_x() + 50, initial_y) # Reset the x position to place the second multi-cell next to the first
    pdf.multi_cell(w=50, h=10, txt="Subject", border=1, align='C', split_only=False, fill=True) # Draw the second multi-cell
    pdf.set_xy(pdf.get_x() + 100, initial_y) 
    pdf.multi_cell(w=30, h=5, txt="Max\nMarks", border=1, align='C', split_only=False, fill=True) 
    pdf.set_xy(pdf.get_x() + 130, initial_y)
    pdf.multi_cell(w=30, h=5, txt="Marks\nObtained", border=1, align='C', split_only=False, fill=True)
    pdf.set_xy(pdf.get_x() + 160, initial_y)
    pdf.multi_cell(w=30, h=10, txt="Percentage", border=1, align='C', split_only=False, fill=True)
    # ---------- table data
    # - add data rows to the table (repetative)
    # - finally, add summary rows to the table
    totalmarks = 0.0
    marksdata = []
    for i in range(len(df.index.tolist())):
        totalmarks = 0.0
        pdf.cell(50, 10, df.loc[i,'examname'], 1, 0, 'L')
        pdf.cell(50, 10, df.loc[i,'subject'], 1, 0, 'L')
        pdf.cell(30, 10, df.loc[i,'maxmarks'], 1, 0, 'C')
        if df.loc[i,'marksobtained'] is None:
            pdf.cell(30, 10, " - ", 1, 0, 'C')
        else:
            pdf.cell(30, 10, df.loc[i,'marksobtained'], 1, 0, 'C')
        if df.loc[i,'percent'] is None:
            pdf.cell(30, 10, " - ", 1, 0, 'R')
        else:
            pdf.cell(30, 10, df.loc[i,'percent'], 1, 0, 'R')
            totalmarks = totalmarks + float(df.loc[i,'percent'])
        pdf.ln()
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(160, 10, 'Total Marks', 1)
    pdf.cell(30, 10, str(totalmarks), 1, 0, 'R')
    pdf.ln()
    # Save PDF
    pdf.output('reportcard.pdf')
    tk.messagebox.showinfo("MESSAGE", "reportcard - PDF file generated", parent=frame)  
    
#=============================================================================
def index(rootframe):
    global df
    # Get Student Data into a DataFrame
    # TABLE: trytbl - (studentid, academicsession, roll, name, class, stream, examname, subject, maxmarks, marksobtained, percent)
    frame = Toplevel()
    r = 1
    Label(frame, text=" ").grid(row=r, column=3, sticky='NE') #padding 
    sql = "select * from trytbl"
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
            sql = "SELECT DISTINCT "+col+" FROM trytbl"
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
            sql = "SELECT * FROM trytbl where "+colnamesCBO.get()+"='"+val+"'"
            df = executeSelectQueryAndReturnDF(frame, sql)
    valCBO.bind("<<ComboboxSelected>>", valCBOSelectedEvent)
    r += 1
    # Create button to generate PDF
    def GeneratePDFFileBtnClickEvent():
        global df
        generatePDF(frame, df)
    Button(frame, text='Generate PDF file', command=GeneratePDFFileBtnClickEvent).grid(row=r, column=1, sticky='W')
    Label(frame, text=" ").grid(row=3, column=3, sticky='NE') #padding
#=============================================================================
# standalone start for code testing - to run this file independently
#=============================================================================
# param = {'table':['trytbl'],'pk':['trytblid'],'cbo':['trytbl.class']}
if __name__ == "__main__":
    rootframe = Tk()
    index(rootframe)
#=============================================================================



