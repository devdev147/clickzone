from fpdf import FPDF
#from _libraryAndDBConnection import * #includes database connection and cursor setting strings
from _reportDataAnalysisPlotCustomFunctions import *

class PDF(FPDF):
    def header(self):

        self.image('bvmlogo.png', 10, 8, 33)  # Adjust the path and size as needed
        self.set_font('Arial', 'B', 12)
        '''
        self.cell(0, 10, 'REPORT CARD', 0, 1, 'C')
        self.ln(10)
        '''
        '''
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'REPORT CARD', 0, 1, 'C')
        '''
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def reporttitle(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)

    #def reportbody(self, body):
    def reportbody(self, df):  #roll, name, class, 
        self.set_font('Arial', '', 12)
        #self.multi_cell(0, 10, body)

        #self.cell(0, 10, 'Roll: '+df.loc[0,'roll'], 0, 1, 'L') # 0 - next cell after line break; 'L' - left align
        self.cell(30, 10, 'Roll: ', 0, 0, 'L')  # 0 - No border; 1 - next cell on right side; 'L'|'C' - left|Center align;
        self.cell(30, 10, df.loc[0,'roll'], 0, 0, 'L')
        self.ln()
        self.cell(30, 10, 'Name: ', 0, 0, 'L')
        self.cell(30, 10, df.loc[0,'name'], 0, 0, 'L')
        self.ln()
        self.cell(30, 10, 'Class: ', 0, 0, 'L')
        self.cell(30, 10, df.loc[0,'class'], 0, 0, 'L')
        self.ln()

    def addmarksdata(self, examname, subject, maxmarks, marksobtained, percent):
        self.cell(50, 10, examname, 1, 0, 'L')
        self.cell(50, 10, subject, 1, 0, 'L')
        #self.cell(30, 10, str(maxmarks), 1)
        #self.cell(30, 10, f'${marksobtained:.2f}', 1)
        #self.cell(30, 10, f'${percent:.2f}', 1)
        self.cell(30, 10, maxmarks, 1, 0, 'C')
        self.cell(30, 10, marksobtained, 1, 0, 'C')
        self.cell(30, 10, percent, 1, 0, 'R')
        self.ln()

# --------------------------------------------------------------
# Create PDF
pdf = PDF()
pdf.add_page()

# Student Data
# TABLE: trytbl
# studentid, academicsession, roll, name, class, stream, examname, subject, maxmarks, marksobtained, percent

frame = Toplevel()
Label(frame, text=" ").grid(row=1, column=1, sticky='NE')
sql = "select * from trytbl where roll=1 and examname='UT1' and marksobtained is not null"
df = executeSelectQueryAndReturnDF(frame, sql)

# School Info
pdf.set_font('Arial', 'B', 16)
pdf.cell(0, 10, 'Birla Vidya Mandir, Nainital', 0, 1, 'C')
pdf.set_font('Arial', '', 12)
pdf.cell(0, 10, 'Nainital', 0, 1, 'C')
pdf.cell(0, 10, 'Uttarakhand, 263001', 0, 1, 'C')
pdf.cell(0, 10, 'Phone: (05942) 235370', 0, 1, 'C')
pdf.cell(0, 10, 'Email: info@birlavidyamandir.com', 0, 1, 'C')
pdf.ln(10)

# Student Info
pdf.reporttitle('Report Card:')

#pdf.reportbody('Student Name\nAddress City\nState, ZIP\n')
pdf.reportbody(df)




# Marks Table Header
# USE multi_cell(w, h, txt='', border=0, align='J', fill=False, split_only=False, link='')
# so as to wrap header text in multiple lines
pdf.set_fill_color(0, 225, 0) # fill table header row; cell will be filled with this color if its last parameter is '1'
initial_y = pdf.get_y()

pdf.multi_cell(w=50, h=10, txt="Exam", border=1, align='L', split_only=False, fill=True) # Draw the first multi-cell
pdf.set_xy(pdf.get_x() + 50, initial_y) # Reset the x position to place the second multi-cell next to the first

pdf.multi_cell(w=50, h=10, txt="Subject", border=1, align='L', split_only=False, fill=True) # Draw the second multi-cell
pdf.set_xy(pdf.get_x() + 100, initial_y) 

pdf.multi_cell(w=30, h=5, txt="Max\nMarks", border=1, align='L', split_only=False, fill=True) 
pdf.set_xy(pdf.get_x() + 130, initial_y)

pdf.multi_cell(w=30, h=5, txt="Marks\nObtained", border=1, align='L', split_only=False, fill=True)
pdf.set_xy(pdf.get_x() + 160, initial_y)

pdf.multi_cell(w=30, h=10, txt="Percentage", border=1, align='L', split_only=False, fill=True)

#pdf.ln(10) # Set cursor position for the next row of height 10
#pdf.ln()

'''
pdf.set_font('Arial', 'B', 12)
pdf.set_fill_color(0, 225, 0) # fill table header row; cell will be filled with this color if its last parameter is '1'
pdf.cell(50, 10, 'Exam', 1,  0, 'C', 1)
pdf.cell(50, 10, 'Subject', 1,  0, 'C', 1)
pdf.cell(30, 10, 'Max Marks', 1,  0, 'C', 1)
pdf.cell(30, 10, 'Marks \n Obtained', 1,  0, 'C', 1)
pdf.cell(30, 10, 'Percentage', 1,  0, 'C', 1)
pdf.ln()
'''


'''
# Invoice Items
items = [
    {'description': 'Product 1', 'quantity': 2, 'unit_price': 15.00},
    {'description': 'Product 2', 'quantity': 1, 'unit_price': 25.00},
    {'description': 'Service 1', 'quantity': 3, 'unit_price': 10.00},
]
total_amount = 0
for item in items:
    pdf.add_invoice_item(item['description'], item['quantity'], item['unit_price'])
    total_amount += item['quantity'] * item['unit_price']
'''
# studentid, academicsession, roll, name, class, stream, examname, subject, maxmarks, marksobtained, percent
# Marks Data
marksdata = []
#i=0
for i in range(len(df.index.tolist())):
    marksdatarow = {
     'examname': df.loc[i,'examname'],
     'subject': df.loc[i,'subject'],
     'maxmarks': df.loc[i,'maxmarks'],
     'marksobtained': df.loc[i,'marksobtained'],
     'percent': df.loc[i,'percent']
     }
    marksdata.append(marksdatarow)
totalmarks = 0.0
for marks in marksdata:
    pdf.addmarksdata(marks['examname'], marks['subject'], marks['maxmarks'], marks['marksobtained'], marks['percent'])
    totalmarks = totalmarks + float(marks['percent'])

# Total Amount
pdf.set_font('Arial', 'B', 12)
pdf.cell(160, 10, 'Total Marks', 1)
#pdf.cell(30, 10, '', 1)
#pdf.cell(30, 10, '', 1)
#pdf.cell(30, 10, f'${totalmarks:.2f}', 1)
pdf.cell(30, 10, str(totalmarks), 1, 0, 'R')
pdf.ln()

# Save PDF
pdf.output('reportcard.pdf')





# ====================================================================================
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
