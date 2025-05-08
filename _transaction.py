from _libraryAndDBConnection import * #includes database connection and cursor setting strings

submitbtnrow = 0
#-----------------------------------------------------------------------------
def table2df(frame, table, columns='*', condition='1=1'):
        try:
                sql = "select "+columns+" from "+table+" where "+condition
                #cursor = conn.cursor()
                cursor.execute(sql)
                data = cursor.fetchall()
                df = pd.DataFrame(data)
                return df
        except conn.Error as e:
                msg = "ERROR: "+str(e.args[0])+e.args[1]
                tk.messagebox.showinfo("MESSAGE", msg, parent=frame)
#=============================================================================
# child frame
#=============================================================================
def createTransChildFrames(root, param):

       
    w, h = root.winfo_screenwidth()-50, root.winfo_screenheight()-50
    parentframe = Frame(root)#, height=h-100, width=w/2)

    canvas = Canvas(parentframe, height=h-100, width=w/2)
    scrollbar = Scrollbar(parentframe, orient="vertical", command=canvas.yview)
    frame = Frame(canvas, width=w/2)
    frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all")
            )
        )
    canvas.create_window((0, 0), window=frame, anchor=W)
    canvas.configure(yscrollcommand=scrollbar.set)

    parentframe.grid(row=0, column=0, padx=15, pady=15)#, sticky=NSEW)    
    canvas.grid(row=0, column=0, sticky=NS)#EW)  #fill all the area available  
    scrollbar.grid(row=0, column=1, sticky=NS) #EW) #fill top to bottom

    #frame = Frame(root) #, xscrollcommand=hsb.set, yscrollcommand=vsb.set)
    #frame.grid(row=0, column=0, sticky='W', padx=15, pady=15)
    
    #frame.configure(background='yellow')  
    r = 0
    Label(frame, text="Transaction Record Entry").grid(row=r, column=0, sticky=W)
    # SET TRANSACTION TABLE
    table = param['table']    
    r += 1
    # SET DATE USING CALENDAR
    Label(frame, text='Date').grid(row=r, column=0, sticky=W)
    def getDate():
        dt = cal.get_date()
        sqlDate = dt.strftime("%Y%m%d") #20210418(For Database query) #displayDate = dt.strftime("%d-%B-%Y") # date string 18-April-2021
        globals()[param['dateColumn']].delete(0,END)
        globals()[param['dateColumn']].insert(INSERT,sqlDate)
    cal = DateEntry(frame, selectmode='day', width=25)
    cal.grid(row=r,column=1,sticky=W) #,padx=15)
    cal.set_date(date.today())
    setDateBTN = tk.Button(frame,text='Set Date',command=getDate)
    setDateBTN.grid(row=r,column=2,sticky=W,padx=10)
    globals()[param['dateColumn']] = Entry(frame)
    globals()[param['dateColumn']].grid(row=r,column=4,sticky=W)
    r += 1
    # SET PRIMARY KEY OF TRANSACTION TABLE e.g. invoice for sale or purchase
    for i in param['pk']:
            globals()[i+'LBL'] = Label(frame, text=i[i.find('.')+1:])
            globals()[i+'LBL'].grid(row=r, column=0, sticky=W)
            globals()[i] = Entry(frame, width=30)
            globals()[i].grid(row=r, column=1, sticky=W)
            r += 1

    '''
    # see - last most setting    
    # SET PREFILLED - non-database expression values
    for prefill in param['prefilled']:
            prefillLeft = prefill[:prefill.find('=')].strip()
            prefillRight = prefill[prefill.find('=')+1:]
            globals()[prefillLeft+'LBL'] = Label(frame, text=prefillLeft)
            globals()[prefillLeft+'LBL'].grid(row=r, column=0, sticky=W)
            globals()[prefillLeft] = Entry(frame, width=30)
            globals()[prefillLeft].grid(row=r, column=1, sticky=W)
            globals()[prefillLeft].delete(0,END)    
            globals()[prefillLeft].insert(INSERT, eval(prefillRight))
            r += 1
    '''    
        
    # SET PICKUP LISTS - single combo or parent-child combo and other affected GUI controls
    #for pickups in param['pickup']:
    for pickupcounter in range(len(param['pickup'])):
            # SET MASTER PICKUP DROP-DOWNS
            #'masterCBO' : ['item.itemcategory>item.itemname']  # masterCBO > childCBO ... select event of masterCBO changes lookup values in childCBO
            #for mcbo in param['masterCBO']:

            #print("PICKUP ITEM - ",param['pickup'][pickupcounter])
            
            for mcbo in param['pickup'][pickupcounter]['masterCBO']:
                    #set masterCBO
                    if len(param['pickup'][pickupcounter]['masterCBO'])>0:
                            masterCBO = mcbo[:mcbo.find('#')]
                            childCBO = mcbo[mcbo.find('#')+1:]                            
                            masterCBOtbl = masterCBO[:masterCBO.find('.')]
                            masterCBOcol = masterCBO[masterCBO.find('.')+1:]
                            childCBOtbl = childCBO[:masterCBO.find('.')]
                            childCBOcol = childCBO[masterCBO.find('.')+1:]

                            #conditionlist = param['pickup'][pickupcounter]['masterCBO']  #list
                            '''    
                            #list to string
                            condition = ''
                            for i in conditionlist:
                                    condition += i+','
                            condition = condition[:-1]                           
                            '''
                            '''
                            Label(frame, text=masterCBOcol).grid(row=r, column=0, sticky=W)                            
                            globals()[masterCBOtbl+'_'+masterCBOcol+'__'+childCBOtbl+'_'+childCBOcol+'___'+condition] = StringVar()
                            globals()[masterCBOcol] = Combobox(frame, name=masterCBOtbl+'_'+masterCBOcol+'__'+childCBOtbl+'_'+childCBOcol+'___'+condition) #use combobox name to get the table name column name and condition specified in _menu.py
                            globals()[masterCBOcol].grid(row=r, column=1, sticky=W)
                            '''
                            Label(frame, text=masterCBOcol).grid(row=r, column=0, sticky=W)                            
                            globals()[masterCBOtbl+'_'+masterCBOcol+'__'+childCBOtbl+'_'+childCBOcol+'___'+str(pickupcounter)] = StringVar()
                            #use combobox name to get the table name column name and its index in pickup list for checking condition later on as specified in _menu.py
                            globals()[masterCBOcol] = Combobox(frame, name=masterCBOtbl+'_'+masterCBOcol+'__'+childCBOtbl+'_'+childCBOcol+'___'+str(pickupcounter))
                            globals()[masterCBOcol].grid(row=r, column=1, sticky=W)
                            

                            #cols = '*'
                            #condition = '1=1'
                            #globals()[masterCBOtbl+'DF'] = table2df(root, masterCBOtbl, cols, cond)
                            #print('globals()[masterCBOcol]: ',globals()[masterCBOcol])
                            '''
                            # condition to filter child combobox upon selection in master combobox    
                            for conds in param['pickup'][pickupcounter]['condition']:
                                    if masterlookuptbl in conds:
                                            condition = condition[condition.find('.')+1:]
                            print(condition)
                            '''    

                            #sql = "select distinct "+masterCBOcol+" from "+masterCBOtbl+" where "+condition
                            #print(sql)    

                            sql = "select distinct "+masterCBOcol+" from "+masterCBOtbl
                            cursor.execute(sql)
                            data = cursor.fetchall()
                            globals()[masterCBOtbl+'DF'] = pd.DataFrame(data)
                            #print(globals()[masterCBOtbl+'DF'])
                            lookupvals = globals()[masterCBOtbl+'DF'][masterCBOcol].tolist()
                            globals()[masterCBOcol]['values'] = lookupvals


                            # masterCBO event handling        
                            def funcMasterCBOSelectedEvent(event):

                                    # name of combo widget is in format
                                    # masterCBOtbl+'_'+masterCBOcol+'__'+childCBOtbl+'_'+childCBOcol    
                                    mpk = event.widget._name

                                    mpkmaster = mpk[:mpk.find('__')]
                                    mpkchildcond = mpk[mpk.find('__')+2:]
                                    mpkchild = mpkchildcond[:mpkchildcond.find('___')]
                                    mpkconditioncounter = mpkchildcond[mpkchildcond.find('___')+3:]
                                    
                                    mCBOtbl = mpkmaster[:mpkmaster.find('_')]
                                    mCBOcol = mpkmaster[mpkmaster.find('_')+1:]
                                    mCBOval = globals()[mCBOcol].get()


                                    cCBOtbl = mpkchild[:mpkchild.find('_')]
                                    cCBOcol = mpkchild[mpkchild.find('_')+1:]
                                    
                                    #print('mCBOcol: ',mCBOcol,'  mpkmaster: ',mpkmaster)
                                    #print('cCBOcol: ',cCBOcol,'  mpkchild: ',mpkchild)
                                    #cCBOval = globals()[mCBOcol].get()

                                    
                                    '''                                    
                                    mCBOtbl = mpk[:mpk.find('_')]
                                    mCBOcol = mpk[mpk.find('_')+1:]
                                    mCBOval = globals()[mCBOcol].get()
                                    '''
                                    
                                    '''
                                    masterCBO = mcbo[:mcbo.find('#')]
                                    mCBOtbl = masterCBO[:masterCBO.find('.')]
                                    mCBOcol = masterCBO[masterCBO.find('.')+1:]
                                    mCBOval = globals()[mCBOcol].get()
                                    '''
                                    '''    
                                    childCBO = mcbo[mcbo.find('#')+1:]
                                    childCBOcol = childCBO[childCBO.find('.')+1:]
                                    '''
                                    #childCBOcol = globals()[childCBO][globals()[childCBO].find('.')+1:]

                                    #print('mpk: ',mpk,' mCBOtbl: ',mCBOtbl,' mCBOcol: ',mCBOcol,' mCBOval: ',mCBOval)    
                                    


                                    #print("invoice.get(): ",invoice.get())
                                    #condition:   e.g. 'item.itemcode < + int(price.get())' where '+' separates colname and value of a form control
                                    

                                    '''
                                    condition = '1=1'
                                    for conds in param['pickup'][int(mpkconditioncounter)]['condition']:
                                            print("conds: ",conds)
                                            if mCBOtbl in conds:
                                                    #condition = conds[conds.find('.')+1:]
                                                    conditionleft = conds[:conds.find('+')]    
                                                    conditionright = conds[conds.find('+')+1:]
                                    #globals()[mCBOtbl+'DF'] = table2df(root, mCBOtbl, cols, cond)
                                    '''
                                    
                                    '''
                                    condition = '1=1'
                                    for conds in param['pickup'][int(mpkconditioncounter)]['condition']:
                                            condition = conds
                                    #if (condition != '1=1') or (condition is not None):
                                    '''
                                    if len(param['pickup'][int(mpkconditioncounter)]['condition'])>0:
                                            condition = param['pickup'][int(mpkconditioncounter)]['condition'][0]
                                            #sql = "select * from "+mCBOtbl+" where "+mCBOcol+"='"+mCBOval+"' and "+conditionleft+str(eval(conditionright))
                                            sql = "select * from "+mCBOtbl+" where "+mCBOcol+"='"+mCBOval+"' and "+str(eval(condition))
                                    else:
                                            sql = "select * from "+mCBOtbl+" where "+mCBOcol+"='"+mCBOval+"'"



                                    print(sql)


                                    

                                    #print(sql)
                                    #print('masterCBO: ',masterCBO, ' childCBO: ',childCBO, '   ',mCBOtbl, '  ',mCBOcol, '  ',mCBOval)

                                    cursor.execute(sql)
                                    data = cursor.fetchall()
                                    globals()[mCBOtbl+'DF'] = pd.DataFrame(data)
                                    #print(globals()[mCBOtbl+'DF'])


                                    #lookupvals = globals()[mCBOtbl+'DF'][childCBOcol].tolist()

                                    #print(globals()[mCBOtbl+'DF'][cCBOcol].tolist())


                                    if globals()[mCBOtbl+'DF'].empty:
                                            lookupvals = ''
                                    else:    
                                            lookupvals = globals()[mCBOtbl+'DF'][cCBOcol].tolist()
                                    
                                    
                                    
                                    print("lookupvals: ",lookupvals)
                                    
                                    print("globals()[mCBOtbl+'DF']: \n",globals()[mCBOtbl+'DF'])

                                    print("globals()[cCBOcol]: ",globals()[cCBOcol])

                                    #childCBO = mcbo[mcbo.find('>')+1:]
                                    #childCBOtbl = childCBO[:childCBO.find('.')]                            
                                    #globals()[childCBOcol]['values'] = lookupvals
                                    globals()[cCBOcol]['values'] = lookupvals
                           
                            globals()[masterCBOcol].bind("<<ComboboxSelected>>", funcMasterCBOSelectedEvent)


                            #print("Combobox #",str(pickupcounter+1),globals()[masterCBOcol])
                            #print("Combobox #",str(pickupcounter+1),globals()[masterCBOcol])
                            #print("FIRST ROUND")
                    

            r += 1        
            #for i in param['masterLookupItems']:  #DICT ITEM: 'masterLookupItems':['table1.pk1','table2.pk2',...]
            for i in param['pickup'][pickupcounter]['masterLookupItems']:
                    # Pick one master table along with its primary key, lookup and autofills at a time
                    masterlookuptbl = i[:i.find('.')]
                    masterlookupcol = i[i.find('.')+1:]
                    #'condition' : ['item.itemstock > 0']
                    #default condition='1=1'
                    cols = '*'

                    '''
                    #need not check condition upon selection in lookup table - already checked upon selection in master CBO
                    cond = '1=1'
                    for conds in param['pickup'][pickupcounter]['condition']:
                            if masterlookuptbl in conds:
                                    cond = conds[conds.find('.')+1:]
                    ''' 
                    #print(cond)
                    #print(masterlookuptbl, "  ", masterlookupcol, "  ",cond)                

                    ############  PERFECTELY WORKING STATEMENT
                    ############ globals()[masterlookuptbl+'DF'] = table2df(root, masterlookuptbl, cols, cond)

                    #use sql query rather than table name to use condition
                    #sql = "select * from "+masterlookuptbl+" where "+cond
                    sql = "select * from "+masterlookuptbl

                    #print(sql)
                    cursor.execute(sql)
                    data = cursor.fetchall()
                    globals()[masterlookuptbl+'DF'] = pd.DataFrame(data)

                    #print(masterlookuptbl, "  ", masterlookupcol, "  ",cond)
                    #print(globals()[masterlookuptbl+'DF'])

                    
                    #print(globals()[masterlookuptbl+'DF'])
                    lookupvals = globals()[masterlookuptbl+'DF'][masterlookupcol].tolist()
                    #print(lookupvals)
                    # set combobox or drop-down with master table lookup values    
                    Label(frame, text=masterlookupcol).grid(row=r, column=0, sticky=W)
                    globals()[masterlookuptbl+'_'+masterlookupcol] = StringVar()
                    globals()[masterlookupcol] = Combobox(frame, name=masterlookuptbl+'_'+masterlookupcol) #use combobox name to get the table name 
                    globals()[masterlookupcol].grid(row=r, column=1, sticky=W)
                    globals()[masterlookupcol]['values'] = lookupvals
                    # master lookup table PKs
                    for mpk in param['pickup'][pickupcounter]['masterPrimaryKeys']:
                            if masterlookuptbl in mpk:
                                    masterlookuppkcol = mpk[mpk.find('.')+1:]
                                    globals()[masterlookuptbl+'PK']=masterlookuppkcol
                    Label(frame, text=masterlookuppkcol).grid(row=r, column=2, sticky=W)
                    globals()[masterlookuppkcol] = Entry(frame, width=30)                
                    globals()[masterlookuppkcol].grid(row=r, column=3, sticky=W)
                                       

                    #print('globals()[masterlookuppkcol]: ',masterlookuppkcol)
                    
                    r += 1
                    # master lookup table autofills
                    globals()[masterlookuptbl+'AF'] = []
                    for afv in param['pickup'][pickupcounter]['masterAutofillValues']:
                            if masterlookuptbl in afv:
                                    masterautofillcol = afv[afv.find('.')+1:]
                                    Label(frame, text=masterautofillcol).grid(row=r, column=0, sticky=W)
                                    globals()[masterautofillcol] = Entry(frame, width=30)
                                    globals()[masterautofillcol].grid(row=r, column=1, sticky=W)
                                    r += 1
                                    globals()[masterlookuptbl+'AF'].append(masterautofillcol)
                                    #print(masterautofillcol)
                    
                    # master - 'getvalfromothertableoncboevent' handling upon masterlookuptbl cbo selection 
                        

                    # master lookup event handling        
                    def funcSelectedEvent(event):
                                    #combobox name => mastertable+'_'+masterlookupcol
                                    #Get label text
                                    #print("label text:", event.widget.cget("text"))
                                    mpk = event.widget._name
                                    masterlookuptbl = mpk[:mpk.find('_')]
                                    masterlookupcol = mpk[mpk.find('_')+1:]
                                    masterlookupval = globals()[masterlookupcol].get()
                                    mastertbleDF = globals()[masterlookuptbl+'DF']
                                    #fill PK and autofill values from master pickup table

                                    #print('mpk: ',mpk)
                                    #print(param['pickup'][pickupcounter]['masterPrimaryKeys'])
                                    #print(masterlookuptbl)
                                    #print(mastertbleDF.columns)
                                    
                                    for c in mastertbleDF.columns:
                                            #print(masterlookuptbl+'.'+c,'      ',globals()[masterlookuptbl+'PK'])

                                            #if masterlookuptbl+'.'+c in param['pickup'][pickupcounter]['masterPrimaryKeys']:
                                            if c == globals()[masterlookuptbl+'PK']:                                            
                                                    #print("GOT PK: ",masterlookuptbl+'.'+c)
                                                    #masterlookuppkval = mastertbleDF[mastertbleDF[masterlookupcol]==masterlookupval][c].tolist()[0]

                                                    '''
                                                    print("mastertbleDF:   ",mastertbleDF)
                                                    print("masterlookuptbl:   ",masterlookuptbl)
                                                    print("masterlookupcol:   ",masterlookupcol)                                                    
                                                    print("masterlookupval:   ",masterlookupval)                                                    
                                                    print("c:   ",c)
                                                    print("mastertbleDF[masterlookupcol]: \n",mastertbleDF[masterlookupcol])
                                                    #print("mastertbleDF[masterlookupcol]==masterlookupval: \n",mastertbleDF[masterlookupcol]==int(masterlookupval))    #use int(masterlookupval) if column type is int
                                                    print("mastertbleDF[masterlookupcol]==masterlookupval: \n",mastertbleDF[masterlookupcol]==masterlookupval)    #use int(masterlookupval) if column type is int
                                                    print("mastertbleDF[mastertbleDF[masterlookupcol]==masterlookupval]: \n",mastertbleDF[mastertbleDF[masterlookupcol]==masterlookupval])
                                                    
                                                    print("mastertbleDF[mastertbleDF['membercode']=='G2']: \n",mastertbleDF[mastertbleDF['membercode']=='G2'])
                                                    print("mastertbleDF[mastertbleDF['membercode']=='G2'][c]: \n",mastertbleDF[mastertbleDF['membercode']=='G2'][c])
                                                    print("mastertbleDF[mastertbleDF['membercode']=='G2'][c].tolist()[0]: \n",mastertbleDF[mastertbleDF['membercode']=='G2'][c].tolist()[0])
                                                    '''
                                                    
                                                    

                                                    
                                                    masterlookuppkval = mastertbleDF[mastertbleDF[masterlookupcol]==masterlookupval][c].tolist()[0]
                                                    # use '==int(masterlookupval)' if lookup column type is int
                                                    


                                                    #print("masterlookuppkval:    ",masterlookuppkval)

                                                    
                                                    globals()[c].delete(0,END)    
                                                    globals()[c].insert(INSERT,masterlookuppkval)                                            
                     
                                            #if masterlookuptbl+'.'+c in param['pickup'][pickupcounter]['masterAutofillValues']:
                                            if c in globals()[masterlookuptbl+'AF']:
                                                    autofillVal = mastertbleDF[mastertbleDF[masterlookupcol].astype(str)==str(masterlookupval)][c].tolist()[0]
                                                    if isinstance(autofillVal, int)==True:
                                                            autofillVal = round(autofillVal,2)
                                                    globals()[c].delete(0,END)
                                                    #globals()[c].insert(INSERT,round(autofillVal,2))
                                                    if autofillVal is not None:
                                                            globals()[c].insert(INSERT,autofillVal)
                                                    else:
                                                            globals()[c].insert(INSERT,"")
                                                    #print(masterlookuptbl+'.'+c, '     ' ,autofillVal )

                                            
                                                    for gvfot in param['pickup'][pickupcounter]['getvalfromothertableonlookupcboevent']:
                                                            '''
                                                            gvfotcol = gvfot[:gvfot.find('=')]
                                                            gvfotquery = gvfot[gvfot.find('=')+1:]
                                                            print("gvfotcol: ",gvfotcol)
                                                            print("gvfotquery: ",gvfotquery)
                                                            print("studentclass.get(): ",globals()['studentclass'].get()+"xxxx")
                                                            #print("studentclass.get(): ",globals()[masterlookupcol].get())
                                                            cursor.execute(gvfotquery)
                                                            gvfotval = cursor.fetchall()
                                                            print("gvfotcol: ",gvfotval)
                                                            '''
                                                            if c in gvfot['triggercol']:

                                                                    global submitbtnrow                                                                    
                                                                    Label(frame, text=gvfot['targetcontrol']).grid(row=submitbtnrow, column=0, sticky=W)
                                                                    globals()[gvfot['targetcontrol']] = Entry(frame, width=30)
                                                                    globals()[gvfot['targetcontrol']].grid(row=submitbtnrow, column=1, sticky=W)
                                                                    
                                                                    print("gvfot['triggercol']: ",gvfot['triggercol'])
                                                                    print("gvfot['targetcontrol']: ",gvfot['targetcontrol'])
                                                                    print("gvfot['othertablecol']: ",gvfot['othertablecol'])
                                                                    print("gvfot['othertable']: ",gvfot['othertable'])
                                                                    print("gvfot['where']: ",gvfot['where'])

                                                                    sql =  ' select '+gvfot['othertablecol']
                                                                    sql += ' from '+gvfot['othertable']
                                                                    sql += ' where '
                                                                    for gvfoti in gvfot['where']:
                                                                            sql += gvfoti[:gvfoti.find('=')]+'="'
                                                                            sql += globals()[gvfoti[gvfoti.find('=')+1:]].get()+'"'
                                                                            sql += ' and '
                                                                    sql = sql[:-5]
                                                                    print(sql)
                                                                    cursor.execute(sql)
                                                                    gvfotval = cursor.fetchone()
                                                                    print("gvfotval: ",gvfotval)
                                                                    print("gvfotval[gvfot['targetcontrol']]: ",gvfotval[gvfot['targetcontrol']])
                                                                    globals()[gvfot['targetcontrol']].delete(0,'end') 
                                                                    #globals()[gvfot['targetcontrol']].insert(INSERT,gvfotval[gvfot['targetcontrol']])
                                                                    #globals()[gvfot['targetcontrol']].insert(0,gvfotval[gvfot['targetcontrol']])
                                                                    #if globals()[gvfot['targetcontrol']] is not None:                                    
                                                                    globals()[gvfot['targetcontrol']].insert(INSERT,gvfotval[gvfot['targetcontrol']])
                                                                    #entry.insert(tk.END, " Hello World")
                                                    
                    globals()[masterlookupcol].bind("<<ComboboxSelected>>", funcSelectedEvent)
                    r += 1




    for i in param['transItems']:
            globals()[i+'LBL'] = Label(frame, text=i[i.find('.')+1:])
            globals()[i+'LBL'].grid(row=r, column=0, sticky=W)
            globals()[i] = Entry(frame, width=30)
            globals()[i].grid(row=r, column=1, sticky=W)
            r += 1



    if len(param['expressions'])<=0:
                    pass
    else:
            def expressionBTNClickEvent():
                    for exp in param['expressions']:
                            expLeft = exp[:exp.find('=')].strip()
                            expRight = exp[exp.find('=')+1:]
                            #print("expLeft: ",expLeft)        
                            #print("expRight: ",expRight)
                            #print("expRight: ",eval(expRight))
                            #globals()[expLeft].insert(INSERT, round(eval(expRight),2))
                            globals()[expLeft].delete(0,END)    
                            globals()[expLeft].insert(INSERT, eval(expRight))
            expressionBTN = Button(frame, text="Calculate", command=expressionBTNClickEvent)
            expressionBTN.grid(row=r, column=1)
    

    r += 1
    for i in param['expressions']:
            i = i[:i.find('=')].strip()
            globals()[i+'LBL'] = Label(frame, text=i)
            globals()[i+'LBL'].grid(row=r, column=0, sticky=W)
            globals()[i] = Entry(frame, width=30)
            globals()[i].grid(row=r, column=1, sticky=W)
            r += 1




    # SET PREFILLED - non-database expression values
    # prefill textfields with default initial values
    for prefill in param['prefilled']:
            prefillLeft = prefill[:prefill.find('=')].strip()
            prefillRight = prefill[prefill.find('=')+1:]
            #globals()[prefillLeft+'LBL'] = Label(frame, text=prefillLeft)
            #globals()[prefillLeft+'LBL'].grid(row=r, column=0, sticky=W)
            #globals()[prefillLeft] = Entry(frame, width=30)
            #globals()[prefillLeft].grid(row=r, column=1, sticky=W)
            globals()[prefillLeft].delete(0,END)    
            globals()[prefillLeft].insert(INSERT, eval(prefillRight))
            #r += 1



    #for inv in param['invisible']:
    #        globals()[inv].grid_remove()


    def submitButtonClickEvent():
            # columns to be sent to trans 'table' - dateColumn, pk, transItems, expressions
            # master values not to be sent to trans table unless assigned to the columnnames in expression
            # masterUpdates to be set in master tables only
            #!IMPORTANT: date column should be named something as 'transdate' not as 'date'
            #Do not change 'keys' of the following dictionaries
            ##use column names only on right hand side of an expression
            #'invisible' - is the simple assignment which is to be saved in trans table
            # BUT NOT to be displayed on screen e.g. comboboxes without textfields inside PICKUP items
            
            cols = []
            vals = []
            table = param['table']
            cols.append(param['dateColumn'])
            for p in param['pk']:
                    cols.append(p[p.find('.')+1:])

            '''
            for mcb in param['masterCBO']:
                    cols.append(mcb[mcb.find('.')+1:mcb.find('#')])    
            for mpi in param['masterLookupItems']:
                    cols.append(mpi[mpi.find('.')+1:])
            for mpk in param['masterPrimaryKeys']:
                    #cols.append(mpk[mpk.find('.')+1:])
                    #cols.append(globals()[mpk[:mpk.find('.')]+'PK'])        #equivalent of globals()[table+'PK']
                    #t = globals()[mpk[mpk.find('.')+1:]].get()
                    cols.append(mpk[mpk.find('.')+1:])
            '''
            '''
            for pickupcounter in range(len(param['pickup'])):
                    for mcb in param['pickup'][pickupcounter]['masterCBO']:
                            cols.append(mcb[mcb.find('.')+1:mcb.find('#')])    
                    for mpi in param['pickup'][pickupcounter]['masterLookupItems']:
                            cols.append(mpi[mpi.find('.')+1:])
                    for mpk in param['pickup'][pickupcounter]['masterPrimaryKeys']:
                            #cols.append(mpk[mpk.find('.')+1:])
                            #cols.append(globals()[mpk[:mpk.find('.')]+'PK'])        #equivalent of globals()[table+'PK']
                            #t = globals()[mpk[mpk.find('.')+1:]].get()
                            cols.append(mpk[mpk.find('.')+1:])
            '''
            
            for ti in param['transItems']:
                    cols.append(ti[ti.find('.')+1:])
                    
            for ex in param['expressions']:
                    #cols.append(ex[ex.find('.')+1:])
                    cols.append(ex[:ex.find('=')].strip())

            '''
            if 'id' in cols:
                    cols.remove('id')  #do not insert any value for id column of type int auto_increment
            '''


            # primary keys in a table to be named as tblname+'id' of type int and auto_increment
            #print(cols)
            for c in cols:
                    if c[-2:]=='id':  
                            cols.remove(c)  #remove auto_increment primary key columns from insert sql query
                    if c in param['displayonlynoinsert']:  
                            cols.remove(c)  #remove display only columns from insert sql query
                        
                            
            for c in cols:
                    #print(cols,"   ",c)
                    vals.append(globals()[c].get())
            
            print("cols -1 : ",cols)
            print("vals -1 : ",vals)


            for inv in param['invisible']:  #simple assignments, same as expressions
                    #print("INV: ",inv)
                    cols.append(inv[:inv.find('=')].strip())
                    vals.append(eval(inv[inv.find('=')+1:].strip()))
                    

            print("cols -2 : ",cols)
            print("vals -2 : ",vals)


            if (len(param['transItems'])<=0) and (len(param['expressions'])<=0):
                    pass
            else:    
                    sql = "INSERT INTO "+ table[0] +"("
                    for c in cols:
                            sql += c+","
                    sql = sql[:-1]
                    sql += ") VALUES("
                    for v in vals:
                            sql += "'"+v+"',"
                    sql = sql[:-1]
                    sql += ")" 

                    print("INSERT SQL QUERY: ",sql)

                    try:
                            cursor.execute(sql)
                            #cursor.execute(sql1)
                            conn.commit()
                            msg = "SUCCESS: TRANSACTION (INSERT SQL query) executed successfully."
                            #tk.messagebox.showinfo("MESSAGE", msg, parent=frame)
                    except conn.Error as e:
                            msg = "ERROR: "+str(e.args[0])+e.args[1]
                            tk.messagebox.showinfo("MESSAGE", msg, parent=frame)
            #'masterUpdates' : ['item.stock=float(item.stock)+float(quantity)']
            for t in param['masterUpdates']:
                    left = t[:t.find('=')]
                    table = left[:left.find('.')]
                    col = left[left.find('.')+1:]
                    exp = t[t.find('=')+1:] #right
                    pkCol=''

                    print('before pkc loop - table: ',table,' col: ',col,' exp: ',exp)
                    for i in range(len(param['pickup'])):
                            for pkc in param['pickup'][i]['masterPrimaryKeys']:
                                    tbl = pkc[:pkc.find('.')]
                                    if tbl==table:
                                            pkCol = pkc[pkc.find('.')+1:]
                                            print('inside pkc loop - tbl: ',tbl,' pkCol: ',pkCol)
                                            #exp = str(round(eval(exp),2))
                                            exp = str(eval(exp))
                                            #print(exp)
                                            sql1 = "UPDATE "+ table +" SET "+ col +"='"+ exp + \
                                                   "' WHERE "+ pkCol +"='"+ globals()[pkCol].get() +"'"

                                            print("master update: ",sql1)
                                            
                                            try:
                                                    #####cursor.execute(sql)
                                                    cursor.execute(sql1)
                                                    conn.commit()

                                                        

                                                    
                                                    msg = "SUCCESS: Master table updated successfully."
                                                    tk.messagebox.showinfo("MESSAGE", msg, parent=frame)
                                            except conn.Error as e:
                                                    msg = "ERROR: Master table could not be updated.\n"+str(e.args[0])+e.args[1]
                                                    tk.messagebox.showinfo("MESSAGE", msg, parent=frame)        

                    try:
                            #cursor.execute(sql)
                            #cursor.execute(sql1)
                            #conn.commit()  #commit both INSERT and UPDATE queries together
                            msg = "SUCCESS: Transaction (insert) and Master update (update) executed successfully."
                            tk.messagebox.showinfo("MESSAGE", msg, parent=frame)
                    except conn.Error as e:
                            msg = "ERROR: "+str(e.args[0])+e.args[1]
                            tk.messagebox.showinfo("MESSAGE", msg, parent=frame)

        
    submitButton = Button(frame, text="Submit", command=submitButtonClickEvent)
    submitButton.grid(row=r+2, column=1)   #leave some rows for late generated controls
    global submitbtnrow
    submitbtnrow = r
    r += 1
    Label(frame, text='').grid(row=r, column=0, sticky=W)  #for padding
    #-----------------------------------------
    for widget in frame.winfo_children():
        widget.grid(padx=0, pady=5)
#=============================================================================
# root frame
#=============================================================================
def createTransRootFrame(rootframe, p):
        #print(p)
        w, h = rootframe.winfo_screenwidth()-50, rootframe.winfo_screenheight()-150
        transrootframe = Toplevel(rootframe)
        transrootframe.geometry("%dx%d+15+60" % (w, h)) 
        transrootframe.title("TRANSACTION ENTRY")
        table = p['table'][0]
        df = table2df(transrootframe,table)
        createTransChildFrames(transrootframe, p)
#=============================================================================
