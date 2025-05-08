from fpdf import FPDF
from _reportDataAnalysisPlotCustomFunctions import *

class PDF(FPDF):
    def header(self):
        self.image('bvmlogo.png', 10, 8, 33)  # Adjust the path and size as needed
        self.set_font('Arial', 'B', 12)
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')
    def reporttitle(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)
    def reportbody(self, df):
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
    def addmarksdata(self, examname, subject, maxmarks, marksobtained, percent):
        #pdf.cell(width, height, text='', border=0, ln=0, align='', fill=0, link='')
        self.cell(50, 10, examname, 1, 0, 'L')
        self.cell(50, 10, subject, 1, 0, 'L')
        self.cell(30, 10, maxmarks, 1, 0, 'C')
        self.cell(30, 10, marksobtained, 1, 0, 'C')
        self.cell(30, 10, percent, 1, 0, 'R')
        self.ln()

        #self.cell(30, 10, str(maxmarks), 1)
        #self.cell(30, 10, f'${marksobtained:.2f}', 1)
        #self.cell(30, 10, f'${percent:.2f}', 1)

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
# USE multi_cell() so as to wrap header text in multiple lines
# multi_cell(w, h, txt='', border=0, align='J', fill=False, split_only=False, link='')
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
#pdf.ln(10)
#pdf.ln()

# Marks Data
# studentid, academicsession, roll, name, class, stream, examname, subject, maxmarks, marksobtained, percent
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

# Total Amount
totalmarks = 0.0
for marks in marksdata:
    pdf.addmarksdata(marks['examname'], marks['subject'], marks['maxmarks'], marks['marksobtained'], marks['percent'])
    totalmarks = totalmarks + float(marks['percent'])
pdf.set_font('Arial', 'B', 12)
pdf.cell(160, 10, 'Total Marks', 1)
pdf.cell(30, 10, str(totalmarks), 1, 0, 'R')
pdf.ln()

# Save PDF
pdf.output('reportcard.pdf')
