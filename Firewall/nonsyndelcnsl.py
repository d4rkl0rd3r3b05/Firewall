from Tkinter import *
import nonsyndel
import icmpfltr

class nonsyndelcnsl:
    def show(self,mainfrm):

	txtfont=("FreeSerif", 11,"bold")
	fnt=("FreeSerif",11,"bold")
	fntopt=("FreeSerif",10)
	fnttxt=("FreeSerif",12)

	nonsyndelfrm=Frame(mainfrm,relief=SOLID,borderwidth=1,bg="white")

	#----------------------------------------Delete by number frame-----------------------------------------
        delnumfrm=Frame(nonsyndelfrm,relief=SOLID,width=50,borderwidth=1,bg="white")
	
	delnum=Label(delnumfrm,text="Delete by number",font=txtfont,relief=RAISED,width=50,\
	height=1,bg="black",fg="white")
        delnum.pack(side=TOP,anchor=W,pady=0,padx=0)

	#--------Table---------
	#Table frame
        tblfrm=Frame(delnumfrm,bg="white")
	
        #Table label
        tbllbl=Label(tblfrm,text="Table"+"\t"*4,font=txtfont,relief=FLAT,width=24,bg="white")
        tbllbl.pack(side=LEFT)
       
	
	#Table option
	self.tbl=StringVar()
	self.tbl.set("filter")

	tblopt = OptionMenu(tblfrm,self.tbl,"filter","nat")
	tblopt["bg"]="white"
	tblopt["font"]=fntopt
	tblopt["width"]=18
	tblopt.pack(side=RIGHT)

      
	tblfrm.pack(expand=YES,fill=X)
 	#------------Chain------------
        #chain frame
	chnfrm=Frame(delnumfrm,bg="white")
        #chain label
        chnlbl=Label(chnfrm,text="Chain"+"\t"*4,font=txtfont,relief=FLAT,width=24,bg="white")
        chnlbl.pack(side=LEFT)
        #chain options
       	self.chn=StringVar()

	self.chn.set("INPUT") 

	chnopt = OptionMenu(chnfrm,self.chn,"INPUT","OUTPUT","FORWARD","PREROUTING","POSTROUTING")
	chnopt["bg"]="white"
	chnopt["font"]=fntopt
	chnopt["width"]=18
	chnopt.pack(side=RIGHT)

	chnfrm.pack(expand=YES,fill=BOTH)

	

	#-------------deletion Position---------
	#deletion Position frame
	delposfrm=Frame(delnumfrm,bg="white")
	self.delpos=StringVar()
	self.delpos.set('1') 
	#deletion Position label
        delposlbl=Label(delposfrm,text="Deletion Position"+"\t"*3,font=txtfont,relief=FLAT,width=24,bg="white")
        delposlbl.pack(side=LEFT,pady=4)
        
	#deletion Position text
	delpostxt=Entry(delposfrm,textvariable=self.delpos,font=fnttxt,relief=SUNKEN,bg="white")
        delpostxt.pack(side=RIGHT,pady=4)
	
	delposfrm.pack(expand=YES,fill=X)



        #-------------deletion Button---------
	delbtn=Button(delnumfrm,text="Delete Rule",command=self.delete,bg="white",\
	font=txtfont,relief=RAISED,width=18,height=1)
        delbtn.pack(side=BOTTOM,anchor=CENTER,pady=4)
 
  
	delnumfrm.pack(side=LEFT,expand=YES,fill=Y)
	
	#-------------------------------Flush Tables frame----------------------------------------------
        flsfrm=Frame(nonsyndelfrm,relief=SOLID,width=35,borderwidth=1,bg="white")

	flstb=Label(flsfrm,text="Flush Tables",font=txtfont,relief=RAISED,width=35,height=1,bg="black",fg="white")
        flstb.pack(side=TOP,anchor=CENTER,pady=0)

	
	#Filter Table
	self.fltfls=BooleanVar()
	fltflschkbtn=Checkbutton(flsfrm,text="Filter Table ",font=txtfont,width=20,variable=self.fltfls,bg="white",\
	borderwidth=0,activebackground="white")
	fltflschkbtn.pack(side=TOP,anchor=W,pady=22,expand=YES,fill=X)
	self.fltfls.set(False)

	#Nat Table
	self.natfls=BooleanVar()
	natflschkbtn=Checkbutton(flsfrm,text="NAT Table   ",font=txtfont,width=20,variable=self.natfls,bg="white",\
	borderwidth=0,activebackground="white")
	natflschkbtn.pack(side=TOP,anchor=W,pady=22,expand=YES,fill=X)
	self.natfls.set(False)
      
	#Mangle Table
	self.mnglfls=BooleanVar()
	mnglflschkbtn=Checkbutton(flsfrm,text="Mangle Table",font=txtfont,width=20,variable=self.mnglfls,bg="white",\
	borderwidth=0,activebackground="white")
	mnglflschkbtn.pack(side=TOP,anchor=W,pady=22,expand=YES,fill=X)
	self.mnglfls.set(False)
        
	flsbtn=Button(flsfrm,text="Flush Tables",command=self.fls,bg="white",\
	font=txtfont,relief=RAISED,width=18,height=1)
        flsbtn.pack(side=BOTTOM,anchor=CENTER,pady=4)

  
	flsfrm.pack(side=RIGHT,expand=YES,fill=Y)
	

	return nonsyndelfrm


    def delete(self):
	nonsyndel.delete(self)


    def fls(self):
	nonsyndel.flush(self)


