from fpdf import FPDF
from _reportDataAnalysisPlotCustomFunctions import *  #to create df from SQL data

class PDF(FPDF):  

    #overriding FPDF methods() through object creation and add_page() method
    #-------------------------
    def __init__(self, orientation='P', unit='mm', format='A4'):
        super().__init__(orientation=orientation, unit=unit, format=format) 
    def header(self):  
        self.image('bvmlogo.png', 10, 8, 33)  
        self.set_font('Arial', 'B', 12)
        # School Info
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Birla Vidya Mandir, Nainital', 0, 1, 'C')
        self.set_font('Arial', '', 12)
        self.cell(0, 10, 'Nainital', 0, 1, 'C')
        self.cell(0, 10, 'Uttarakhand, 263001', 0, 1, 'C')
        self.cell(0, 10, 'Phone: (05942) 235370', 0, 1, 'C')
        self.cell(0, 10, 'Email: info@birlavidyamandir.com', 0, 1, 'C')
        self.ln(10)
    def footer(self):  
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    #custom methods() called manually
    #----------------
    def reportbodyTitle(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)
    def reportbodyTopData(self, df):
        #pdf.cell(width, height, text='', border=0, ln=0, align='', fill=0, link='')
        #roll, name, class,
        self.set_font('Arial', '', 12)
        self.cell(30, 10, 'Roll:', 0, 0, 'L')
        self.cell(30, 10, df.loc[0,'roll'], 0, 0, 'L')
        self.ln()
        self.cell(30, 10, 'Name: ', 0, 0, 'L')
        self.cell(30, 10, df.loc[0,'name'], 0, 0, 'L')
        self.ln()
        self.cell(30, 10, 'Class: ', 0, 0, 'L')
        self.cell(30, 10, df.loc[0,'class'], 0, 0, 'L')
        self.ln()
    def reportbodyDataTableHeader(self):
        self.set_fill_color(0, 225, 0) # fill table header row; cell will be filled with this color if its last parameter is '1'
        initial_y = self.get_y()
        self.multi_cell(w=50, h=10, txt="Exam", border=1, align='C', split_only=False, fill=True) # Draw the first multi-cell
        self.set_xy(self.get_x() + 50, initial_y) # Reset the x position to place the second multi-cell next to the first
        self.multi_cell(w=50, h=10, txt="Subject", border=1, align='C', split_only=False, fill=True) # Draw the second multi-cell
        self.set_xy(self.get_x() + 100, initial_y) 
        self.multi_cell(w=30, h=5, txt="Max\nMarks", border=1, align='C', split_only=False, fill=True) 
        self.set_xy(self.get_x() + 130, initial_y)
        self.multi_cell(w=30, h=5, txt="Marks\nObtained", border=1, align='C', split_only=False, fill=True)
        self.set_xy(self.get_x() + 160, initial_y)
        self.multi_cell(w=30, h=10, txt="Percentage", border=1, align='C', split_only=False, fill=True)
    def createDataTableRows(self, df):
        # Marks Data
        # studentid, academicsession, roll, name, class, stream, examname, subject, maxmarks, marksobtained, percent
        marksdata = []
        for i in range(len(df.index.tolist())):
            marksdatarow = {
             'examname': df.loc[i,'examname'],
             'subject': df.loc[i,'subject'],
             'maxmarks': df.loc[i,'maxmarks'],
             'marksobtained': df.loc[i,'marksobtained'],
             'percent': df.loc[i,'percent']
             }
            marksdata.append(marksdatarow)
        # Total Amount
        totalmarks = 0.0
        for marks in marksdata:
            self.reportbodyDataTableAddData(marks['examname'], marks['subject'], marks['maxmarks'], marks['marksobtained'], marks['percent'])
            if marks['percent'] is None:
                pass 
            else:
                totalmarks = totalmarks + float(marks['percent'])
        self.set_font('Arial', 'B', 12)
        self.cell(160, 10, 'Total Marks', 1)
        self.cell(30, 10, str(totalmarks), 1, 0, 'R')
        self.ln()
    def reportbodyDataTableAddData(self, examname, subject, maxmarks, marksobtained, percent):
        self.cell(50, 10, examname, 1, 0, 'L')
        self.cell(50, 10, subject, 1, 0, 'L')
        self.cell(30, 10, maxmarks, 1, 0, 'C')
        if marksobtained is None:
            self.cell(30, 10, " - ", 1, 0, 'C')
        else:
            self.cell(30, 10, marksobtained, 1, 0, 'C')
        if percent is None:
            self.cell(30, 10, " - ", 1, 0, 'R')
        else:
            self.cell(30, 10, percent, 1, 0, 'R')
        self.ln()

# =============================================================================================
# START
# =============================================================================================

global df
global pdf
# Create PDF & set its page settings
pdf = PDF(orientation='L', unit='mm', format='A4')
pdf.add_page()

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
    global pdf
    pdf.reportbodyTitle('Report Card:')
    pdf.reportbodyTopData(df)
    pdf.reportbodyDataTableHeader()
    pdf.createDataTableRows(df) # calls reportbodyDataTableAddData(df) to fill data in the tabale rows
    # Save PDF
    pdf.output('reportcard.pdf')  
Button(frame, text='Generate PDF file', command=GeneratePDFFileBtnClickEvent).grid(row=r, column=1, sticky='W')
Label(frame, text=" ").grid(row=3, column=3, sticky='NE') #padding

# ====================================================================================
'''
Create a subclass of FPDF class which allows to
    - override __init__() constructor for pagesize, orientation etc. and
    - override header(), footer() methods

In the subclass, create methods to
    - Call the parent class (FPDF) constructor with the desired page format
    - Override the header method which gets called automatically by add_page() method
    - Override the footer method which gets called automatically by add_page() method

Create an instance (object) of custom subclass PDF and using orientation, unit and format paramteres pass
    - page orientation ('L', 'P')
    - custom page size ('A4', 'A5', 'Letter' or e.g. (100, 150) for 100mm(width) x 150mm(height) page size as tuple, if unit is 'mm')
    - unit of measurement on page (cm, mm)
Use pdf = PDF() to create PDF with default page settings

pdf = PDF(orientation='L', unit='mm', format='A4') # calls __init()__ constructor automatically
pdf.add_page() #create a new page in the PDF document and calls header() and footer() methods automatically to set the header and footer of the page


        # DATA FORMATTING IN cells
        #self.cell(30, 10, str(maxmarks), 1)
        #self.cell(30, 10, f'${marksobtained:.2f}', 1)
        #self.cell(30, 10, f'${percent:.2f}', 1)



'''


'''
Cell in FPDF
============
Cell() method prints a cell (rectangular area) with optional borders, background color and character string.
The upper-left corner of the cell corresponds to the current position.
The text can be aligned or centered.
After the call, the current position moves to the right or to the next line.
It is possible to put a link on the text. If automatic page breaking is enabled and the cell goes beyond the limit, a page break is done before outputting.
Use cell() method to create cells for placing text or borders in a PDF document.
It’s one of the core methods for layout management in FPDF.

Here's a breakdown of the method's syntax:

pdf.cell(width, height, text='', border=0, ln=0, align='', fill=0, link='')

Parameters and Their Meanings
width(float):   Specifies the width of the cell. If set to 0, the cell extends to the right margin.
height(float):  Specifies the height of the cell. This is generally set based on the line height.
text(str):      The text string to be printed in the cell. If empty, it creates an empty cell, which can be useful for positioning or spacing.
border(mixed): Sets the border type around the cell.
                It can take values like:
                0: No border (default).
                1: Full border around the cell.
                Individual border sides:
                L, T, R, B (for Left, Top, Right, Bottom respectively).
                Multiple sides can be combined like 'LT' for top and left borders.
ln(int):        Indicates the position after the function call.
                0: Puts the next cell to the right (default).
                1: Moves the cursor to the beginning of the next line.
                2: Moves the cursor to the beginning of the next line with a horizontal offset.
align (str):    Specifies text alignment within the cell.
                'L': Left alignment (default).
                'C': Centered alignment.
                'R': Right alignment.
fill (int):     Specifies whether to draw a filled background color.
                0: Transparent (default).
                1: Filled background using the current fill color.
link (str):     Makes the cell text a clickable link. Pass a URL or link identifier to make the text link to a destination within the document.

Example:
# Create a new cell with 40 width, 10 height, text "Hello", a border, center-aligned, and move to the next line after printing.
pdf.cell(40, 10, "Hello", border=1, ln=1, align='C')

# Create an empty cell of width 20, height 10, with only left and right borders.
pdf.cell(20, 10, border='LR')

# Create a filled cell with a width of 50, a height of 10, and a background color set beforehand.
pdf.set_fill_color(200, 220, 255)  # Set background color
pdf.cell(50, 10, "This is a filled cell", border=1, ln=1, align='C', fill=1)

Tips for Using cell()
Combine multiple parameters like border, align, and fill to customize your table layouts.
Adjust ln values to control the flow and placement of the next cells.
If you want to insert a table, set a fixed width for each cell and loop through rows of data to generate structured tables.





In the fpdf2 library, the multi_cell() method is used to create cells that can handle text wrapping across multiple lines. Unlike the cell() method, which creates a single line of text within a fixed width, multi_cell() automatically wraps text if it exceeds the width of the cell, creating new lines as needed. This makes it ideal for displaying paragraphs or longer text blocks within table cells.

Syntax:
python
Copy code
multi_cell(w, h, txt='', border=0, align='J', fill=False, split_only=False, link='')
Parameters:
w (float):

Width of each cell in the multi-cell block.
h (float):

Height of each line of text within the multi-cell block.
txt (str):

Text to be displayed inside the multi-cell.
Supports multi-line strings or text that automatically wraps based on the specified width.
border (mixed):

Sets the border around the multi-cell area.
0: No border (default).
1: Full border.
You can also specify individual sides, e.g., L, T, R, B.
align (str):

Alignment of text within each cell.
Possible values: L (left), C (center), R (right), and J (justified).
fill (bool):

Sets whether to fill the background color for each line of the multi-cell.
False: Transparent (default).
True: Fill with the current fill color.
split_only (bool):

If True, the text is split into lines but not output to the PDF.
Useful for calculating cell heights before rendering.
link (str):

A clickable link to an external URL or an internal document identifier.

'''

