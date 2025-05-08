from _reportDataAnalysisPlotCustomFunctions import *
#-----------------------------------------------------------------------------
# User Defined Plots and Data Analysis
#-----------------------------------------------------------------------------
# plot 1
#-----------------------------------------------------------------------------
def plotproductsales(frame):
        sql = "select productname, unitsell from sale"
        charttype = 'bar' #'plot','bar','hist'
        xcol = 'productname'
        ycol = 'unitsell'
        title = 'My Title'
        xlabel = 'PRODUCT NAME'
        ylabel = 'UNITS SOLD'
        xticks = ''
        yticks = ''
        executeSelectQueryForPlotAndDA(frame, sql, charttype, title, xlabel, ylabel, xticks, yticks, xcol, ycol)


def plotproductpurchase(frame):
        sql = "select productname, unitpurchase from purchase"
        charttype = 'bar' #'plot','bar','hist'
        xcol = 'productname'
        ycol = 'unitpurchase'
        title = 'My Title'
        xlabel = 'PRODUCT NAME'
        ylabel = 'UNITS PURCHASE'
        xticks = ''
        yticks = ''
        executeSelectQueryForPlotAndDA(frame, sql, charttype, title, xlabel, ylabel, xticks, yticks, xcol, ycol)


def plotTimeSales(frame):
        try:
                frame = Toplevel()
                sql = "select productname from sale"
                df = executeSelectQueryAndReturnDF(frame, sql)
                # GUI
                # drop-down/pick-up list
                Label(frame, text=" ").grid(row=1, column=1, sticky='NE')
                namevar = StringVar()
                namelookupvalues = df['productname'].tolist()
                Label(frame, text="productname").grid(row=2, column=1, sticky='NE')
                nameCBO = Combobox(frame, name='namecbo', width=30, textvariable=namevar)
                nameCBO.grid(row=2, column=2)
                nameCBO['values'] = namelookupvalues
                nameCBO.current(0)
                #COPY#
                Label(frame, text=" ").grid(row=1, column=1, sticky='NE')
                namevar = StringVar()
                namelookupvalues = df['productname'].tolist()
                Label(frame, text="productname").grid(row=2, column=1, sticky='NE')
                nameCBO = Combobox(frame, name='namecbo', width=30, textvariable=namevar)
                nameCBO.grid(row=2, column=2)
                nameCBO['values'] = namelookupvalues
                nameCBO.current(0)
                def nameCBOSelectedEvent(event):
                        name = event.widget.get()
                        sql = "SELECT unitsell, transdate FROM sale where productname='"+name+"'"
                        charttype = 'plot'
                        xcol = 'transdate'
                        ycol = 'unitsell'
                        title = 'Sale Trend of product:'
                        xlabel = 'DATE'
                        ylabel = 'SALES'
                        xticks = ''
                        yticks = ''
                        executeSelectQueryForPlotAndDA(frame, sql, charttype, title, xlabel, ylabel, xticks, yticks, xcol, ycol)      
                nameCBO.bind("<<ComboboxSelected>>", nameCBOSelectedEvent)
                Label(frame, text=" ").grid(row=3, column=3, sticky='NE')
        except conn.Error as e:
                msg = "ERROR: "+str(e.args[0])+e.args[1]
                tk.messagebox.showinfo("MESSAGE", msg, parent=frame)


#=============================================================================
# standalone start
#=============================================================================
param = {'table':['sale'],'pk':['saleid'],'cbo':[]}
if __name__ == "__main__":
        rootframe = Tk()
        plotproductsales(rootframe)        
#=============================================================================

