#====================================================================================
#import standard Python library files
#-------------------------------------
from _libraryAndDBConnection import *   #includes database connection and cursor setting strings
#import custom library files
#-------------------------------------
import _master                          #for master table data handling
import _edit                            #for updating tables data 
import _report                          #for selecting tables data  
import _transaction                     #for transaction table data handling
import _dataAnalysisAndPlot             #for data analysis & plotting 
import _database                        #for database management
import _createMySQLTablesWithTestData   #for creating MySQL tables with test data 
import _dataExportImport                #  
import _reportCustom                    #
import _dataAnalysisAndPlotCustom       #  
import _pdfFileGeneration               #
import _generatePDFCustomParameterized
import _about                           #
#====================================================================================
def donothing():
        pass
#====================================================================================
def menu(rootframe):
        #--------------------------------------------------------------------
        menubar = Menu(rootframe)
        #--------------------------------------------------------------------
        newmenu = Menu(menubar, tearoff=0)
        newmnuproduct = {'table':['product'],'pk':['productid'],'cbo':['productcategory.productcategory'],'autofill':[]} 
        newmenu.add_command(label="product",
                            command=lambda: _master.createInsertRootFrame(rootframe, newmnuproduct))
        newmnuproduct_category = {'table':['productcategory'],'pk':['productcategoryid'],'cbo':[''],'autofill':[]} 
        newmenu.add_command(label="product Category",
                            command=lambda: _master.createInsertRootFrame(rootframe, newmnuproduct_category))
        newmnusupplier = {'table':['supplier'],'pk':['supplierid'],'cbo':[''],'autofill':[]} 
        newmenu.add_command(label="supplier",
                            command=lambda: _master.createInsertRootFrame(rootframe, newmnusupplier))
        newmnucoustomer = {'table':['coustomer'],'pk':['coustomerid'],'cbo':[''],'autofill':[]} 
        newmenu.add_command(label="coustomer",
                            command=lambda: _master.createInsertRootFrame(rootframe, newmnucoustomer))
        newmnureplacement_refund = {'table':['replacementrefund'],'pk':['replacementrefundid'],'cbo':['productcategory.productcategory'],'autofill':[]} 
        newmenu.add_command(label="replacement refund",
                            command=lambda: _master.createInsertRootFrame(rootframe, newmnureplacement_refund))
        newmnucompanyname = {'table':['companyname'],'pk':['companynameid'],'cbo':[''],'autofill':[]} 
        newmenu.add_command(label="companyname",
                            command=lambda: _master.createInsertRootFrame(rootframe, newmnucompanyname))
        menubar.add_cascade(label="NEW", menu=newmenu)
        #--------------------------------------------------------------------
        editmenu = Menu(menubar, tearoff=0)
        editmenutabledata = {'table':['product'],'pk':['productid'],'cbo':['productcategory.productcategory'],'autofill':['']}
        editmenu.add_command(label="Edit Database Table Data",
                    command=lambda: _edit.createEditRootFrame(rootframe, editmenutabledata))
        menubar.add_cascade(label="EDIT", menu=editmenu)
        #--------------------------------------------------------------------
        transmenu = Menu(menubar, tearoff=0)
        paramsale = {
                'table'                 : ['sale'],
                'pk'                    : ['saleid'],
                'dateColumn'            : 'transdate',
                'pickup'                : [
                                          {                
                                          'masterCBO'             : ['product.productcategory#product.productname'],
                                          'masterLookupItems'     : ['product.productname'],
                                          'getvalfromothertableonlookupcboevent' : [],
                                          'masterPrimaryKeys'     : ['product.productid'],
                                          'masterAutofillValues'  : ['product.warrantyperiod','product.productunit'],
                                          'condition'             : [],
                                          },
                                          {                
                                          'masterCBO'             : ['coustomer.coustomercategory#coustomer.coustomername'],
                                          'masterLookupItems'     : ['coustomer.coustomername'],
                                          'getvalfromothertableonlookupcboevent' : [],
                                          'masterPrimaryKeys'     : ['coustomer.coustomerid'],
                                          'masterAutofillValues'  : [],
                                          'condition'             : [],
                                          }
                                          ],
                'transItems'            : ['invoice','saleprice','unitsell','gst'],
                'expressions'           : ['totalamount = float(unitsell.get()) * float(saleprice.get())',
                                           'gstamount = round(float(saleprice.get()) * float(gst.get()) / 100.00, 2)',
                                           'netamount = float(totalamount.get()) + float(gstamount.get())',],
                'displayonlynoinsert'   : [],
                'invisible'             : [
                                           'productid=productid.get()',
                                           'productname=productname.get()',
                                           'coustomername=coustomername.get()',
                                           'productcategory=productcategory.get()',
                                           'warrantyperiod=warrantyperiod.get()',
                                           'coustomerid=coustomerid.get()',
                                           ],
                'prefilled'             : [],  #to set 0.00 as default inital value in the textfield 'fright'
                'masterUpdates'         : [
                                           'product.productunit=float(productunit.get())-float(unitsell.get())',
                                           ],                                               
                }

        transmenu.add_command(label="sale", command=lambda: _transaction.createTransRootFrame(rootframe, paramsale))
        # use 'masterLookupItems' : ['item.itemname']
        # so as to update the total quantity in items table
        # in addition to the stock updation in itempurchase table
        parampurchase = {
                'table'                 : ['purchase'],                
                'pk'                    : ['purchaseid'],
                'dateColumn'            : 'transdate',
                'pickup'                : [                    
                                          {
                                          'masterCBO'             : ['product.productcategory#product.productname'],
                                          'masterLookupItems'     : ['product.productname'],
                                          'getvalfromothertableonlookupcboevent' : [],
                                          'masterPrimaryKeys'     : ['product.productid'],
                                          'masterAutofillValues'  : ['product.productunit'],                                         
                                          'condition'             : [],
                                          },
                                          {                
                                          'masterCBO'             : ['supplier.suppliercity#supplier.suppliername'],
                                          'masterLookupItems'     : ['supplier.suppliername'],
                                          'getvalfromothertableonlookupcboevent' : [],
                                          'masterPrimaryKeys'     : ['supplier.supplierid'],
                                          'masterAutofillValues'  : [],
                                          'condition'             : [],
                                          }
                                          ],
                'transItems'            : ['invoice','unitpurchase','gst','price'],
                'expressions'           : ['totalamount = float(unitpurchase.get()) * float(price.get())',
                                           'gstamount = round(float(totalamount.get()) * float(gst.get()) / 100.00, 2)',
                                           'netpurchaseprice = float(totalamount.get()) + float(gstamount.get())',],
                'displayonlynoinsert'   : [],
                'invisible'             : [
                                           'productid=productid.get()',
                                           'supplierid=supplierid.get()',
                                           'productcategory=productcategory.get()',
                                           'productname=productname.get()',
                                           'suppliercity=suppliercity.get()',
                                           'suppliername=suppliername.get()',
                                           ],               
                'prefilled'             : [],
                'masterUpdates'         : [
                                           'product.productunit=float(productunit.get())+float(unitpurchase.get())',
                                        ],
                }       
        transmenu.add_command(label="purchase", command=lambda: _transaction.createTransRootFrame(rootframe, parampurchase))

        menubar.add_cascade(label="TRANSACTIONS", menu=transmenu)
        #====================================================================
       
        #=====================================================================
        reportmenu = Menu(menubar, tearoff=0)
        rptparam1 ={'table':['product'],'pk':['productid'],'cbo':['productcategory.productcategory']}
        reportmenu.add_command(label="all", command=lambda: _report.createSelectRootFrame(rootframe, rptparam1)) #use lambda to pass arguments to the function        
        #rptparam2 = {'table':['coustomer'],'pk':['coustomerid'],'cbo':[]}
        #reportmenu.add_command(label="Customer", command=lambda: _report.createSelectRootFrame(rootframe, rptparam2))
        reportmenu.add_separator()
        reportmenu.add_command(label="product&customer", command=lambda: _reportCustom.rptItemDetail(rootframe))
        reportmenu.add_command(label="sale report", command=lambda: _reportCustom.rptsaleDetail(rootframe))
        reportmenu.add_command(label="purchase report", command=lambda: _reportCustom.rptpurchaseDetail(rootframe))
        reportmenu.add_command(label="selective product name", command=lambda: _reportCustom.rptItemDetailConditionalPickupList(rootframe))
        reportmenu.add_command(label="selective query", command=lambda: _reportCustom.rptItemDetailConditionalTextbox(rootframe))
        reportmenu.add_separator()
        reportmenu.add_command(label="Generate PDF", command=lambda: _pdfFileGeneration.invoicePurchase(rootframe))

        parampdf = {'table':'sale',
                    'condition':'1=1',
                    'nonRepetativeColumns':['saleid', 'coustomername', 'coustomerid'],
                    'repetativeColumns':[
                                        {'colname':'productname',   'colheader':'productname',       'colwidth':50,  'colheight':10,  'colalign':'L'},
                                        {'colname':'productcategory',      'colheader':'productcategory',       'colwidth':50,  'colheight':10,  'colalign':'C'},
                                        {'colname':'unitsell',       'colheader':'unitsell',          'colwidth':50,  'colheight':10, 'colalign':'L'},
                                        {'colname':'totalamount',       'colheader':'totalamount',          'colwidth':50,  'colheight':10, 'colalign':'L'},
                                        
                                        ],
                    'sumcol': ['totalamount',],
                    }
        reportmenu.add_command(label="Generate Parameterized PDF", command=lambda: _generatePDFCustomParameterized.index(rootframe, parampdf))
        

        menubar.add_cascade(label="REPORT", menu=reportmenu)
        #====================================================================
        damenu = Menu(menubar, tearoff=0)
        daparam1 = {'table':['product'],'pk':['productid'],'cbo':['productcategory.productcategory']}
        damenu.add_command(label="Data Analysis - Complete",
                    command=lambda: _dataAnalysisAndPlot.createDataAnalysisRootFrame(rootframe, daparam1))
        damenu.add_separator()
        damenu.add_command(label="Product Sales",command=lambda: _dataAnalysisAndPlotCustom.plotproductsales(rootframe))
        damenu.add_command(label="Product Purchase",command=lambda: _dataAnalysisAndPlotCustom.plotproductpurchase(rootframe))
        damenu.add_command(label="plotTimeSales",command=lambda: _dataAnalysisAndPlotCustom.plotTimeSales(rootframe))
        #damenu.add_command(label="Data Analysis - Filter (Boolean Indexing)", command=lambda: dataAnalysisFilterData.dataAnalysis(db))
        menubar.add_cascade(label="DATA ANALYSIS", menu=damenu)
        #====================================================================
        dbmenu = Menu(menubar, tearoff=0)
        dbmenu.add_command(label="Export-Import Data", command=lambda: _dataExportImport.index(rootframe))
        dbmenu.add_separator()
        #newdatabase = "d1234"
        #dbmenu.add_command(label="Create Database", command=lambda: _database.createNewDatabase(rootframe,newdatabase))
        dbmenu.add_command(label="Create Table", command=lambda: _createMySQLTablesWithTestData.createTablesWithTestData(rootframe))
        dbmenu.add_command(label="Backup Database", command=lambda: _database.backupDatabase(rootframe))
        dbmenu.add_command(label="Alter Table", command=lambda: _database.alterTable(rootframe))
        '''
        dbmenu.add_separator()
        dbmenu.add_command(label="Restore Database", command=lambda: _database.restoreDatabase(rootframe))
        dbmenu.add_command(label="Reset Database", command=lambda: _database.resetDatabase(rootframe))
        dbmenu.add_command(label="Drop Table", command=donothing)
        '''
        menubar.add_cascade(label="DATABASE", menu=dbmenu)
        #====================================================================
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command= _about.manual)
        helpmenu.add_command(label="Manual & Guide", command= _about.manual)
        helpmenu.add_command(label="Help", command= _about.help)
        helpmenu.add_command(label="Contact", command= _about.contact)
        menubar.add_cascade(label="HELP", menu=helpmenu)
        #====================================================================
        def clearcursorandconnection():
                #if cursor.open:
                #        cursor.close()
                if conn.open:
                        conn.close() #it will close its dependent cursor on its own
        def exitapp():
                #rootframe.quit() #NOT RECOMMENDED
                clearcursorandconnection()
                rootframe.destroy()
        exitmenu = Menu(menubar, tearoff=0)
        exitmenu.add_command(label="Close Cursor & Connection", command=clearcursorandconnection)
        exitmenu.add_command(label="Exit Application", command=exitapp) #rootframe.destroy
        menubar.add_cascade(label="Exit", menu=exitmenu)
        #====================================================================
        return menubar
#====================================================================================
