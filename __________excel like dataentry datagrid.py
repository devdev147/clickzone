
############## supressing future warnings
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
##############

from tkinter import *
import pandas as pd

# Create an instance of tkinter frame
window = Tk()

# Set the size of the tkinter window
window.geometry("800x200")

# Load data from source
df = pd.read_excel("data.xlsx")
print(df)

# Extract number of rows and columns
n_rows = df.shape[0]
n_cols = df.shape[1]

# Extracting columns from the data and
#creating text widget with some
# background color
column_names = df.columns
i=0
for j, col in enumerate(column_names):
	text = Text(window, width=16, height=1, bg = "#9BC2E6")
	text.grid(row=i,column=j)
	text.insert(INSERT, col)
	
# Dictionary for storing the text widget
# references
cells = {}

# adding all the other rows into the grid
for i in range(n_rows):
	for j in range(n_cols):
		text = Text(window, width=16, height=1)
		text.grid(row=i+1,column=j)
		#text.insert(INSERT, df.loc[i][j])
		text.insert(INSERT, df.iloc[i,j])
		cells[(i,j)] = text		
		
def do_something():
	"""
	When user clicks the "Save" button, modified data
	will be saved in excel file
	"""
	for i in range(n_rows):
		for j in range(n_cols):
			if df.iloc[i,j] != cells[(i,j)].get("1.0", "end-1c"): #if df.loc[i][j] != cells[(i,j)].get("1.0", "end-1c"):
				#print(cells[(i,j)].get("1.0", "end-1c"))
				#df.iloc[i,j] = str("") #intializing cell before value assignment; otherwise futrewarning appears with regard to incompatible datatype asking for casting
				df.iloc[i,j] = cells[(i,j)].get("1.0", "end-1c") #df.loc[[i],column_names[j]] = cells[(i,j)].get("1.0", "end-1c")
	df.to_excel("sample.xlsx")

save_button = Button(
	window, height = 2,
	width = 16,
	text ="Save",
	command = lambda:do_something())
save_button.grid(row=7,column = 0)
window.mainloop()
