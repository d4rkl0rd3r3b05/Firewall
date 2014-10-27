from Tkinter import *	
import polotptmeth


class polotpt:
    def __init__(self,otptpolfrm):
	txtfont=("FreeSerif", 10,"bold")
	
	#---------------Title------------------------------------------------------------------------------
	optitlefrm=Frame(otptpolfrm,relief=SOLID,height=1,borderwidth=1)
	title=Label(optitlefrm,text="OUTPUT",font=txtfont,relief=FLAT,width=27,height=1)
        title.pack(side=LEFT,anchor=CENTER,pady=0)
	optitlefrm.pack(side=TOP,expand=YES,fill=BOTH)


	#---------------label for policy console------------------------------------------------------------
	oplblfrm=Frame(otptpolfrm,relief=SOLID,height=1,borderwidth=1)
		
	src=Label(oplblfrm,text="Source Address",font=txtfont,relief=RAISED,width=27,height=1)
        src.pack(side=LEFT,anchor=CENTER,pady=0)

	des=Label(oplblfrm,text="Destination Address",font=txtfont,relief=RAISED,width=26,height=1)
        des.pack(side=LEFT,anchor=CENTER,pady=0)

	recv=Label(oplblfrm,text="Protocol",font=txtfont,relief=RAISED,width=16,height=1)
        recv.pack(side=LEFT,anchor=CENTER,pady=0)

	send=Label(oplblfrm,text="Action",font=txtfont,relief=RAISED,width=15,height=1)
        send.pack(side=LEFT,anchor=CENTER,pady=0)
	
	stt=Label(oplblfrm,text="Miscellaneous",font=txtfont,relief=RAISED,width=33,height=1)
        stt.pack(side=LEFT,anchor=CENTER,pady=0)
	


	oplblfrm.pack(side=TOP,expand=YES,fill=BOTH)
	
	

	#-------------------Text Area for status console----------------------------------------------------
	#output frame
        optxtfrm=Frame(otptpolfrm,relief=SOLID,height=30,borderwidth=1)
        txtfnt=("FreeSerif", 9,"bold")

        #text box 4 source address
        self.srctxt=Text(optxtfrm,bg="white",fg="black",font=txtfnt,width=31,height=8)
        self.srctxt.pack(side=LEFT,expand=YES,fill=BOTH)


	 #text box 4 destination address
        
        self.destxt=Text(optxtfrm,bg="white",fg="black",font=txtfnt,width=30,height=8)
        self.destxt.pack(side=LEFT,expand=YES,fill=BOTH)
	
	      
	
	#text box 4 protocol
        
        self.prtcltxt=Text(optxtfrm,bg="white",fg="black",font=txtfnt,width=18,height=8)
        self.prtcltxt.pack(side=LEFT,expand=YES,fill=BOTH)

	
        #text box 4 policy
        
        self.poltxt=Text(optxtfrm,bg="white",fg="black",font=txtfnt,width=18,height=8)
        self.poltxt.pack(side=LEFT,expand=YES,fill=BOTH)

	
       	
        #text box 4 miscellaneous
        
        self.misctxt=Text(optxtfrm,bg="white",fg="black",font=txtfnt,width=36,height=8)
        self.misctxt.pack(side=LEFT,expand=YES,fill=BOTH)


	
	      
	optxtfrm.pack(side=TOP,expand=YES,fill=BOTH)
	optxtscrlbar=Scrollbar(optxtfrm,command=self.srctxt.yview and self.destxt.yview and self.prtcltxt.yview)
	optxtscrlbar=Scrollbar(optxtfrm,command=self.poltxt.yview and self.misctxt.yview)
	

	self.srctxt["yscrollcommand"]=optxtscrlbar.set
	self.destxt["yscrollcommand"]=optxtscrlbar.set
	self.poltxt["yscrollcommand"]=optxtscrlbar.set
	self.prtcltxt["yscrollcommand"]=optxtscrlbar.set
	self.misctxt["yscrollcommand"]=optxtscrlbar.set
	optxtscrlbar.pack(side=RIGHT,expand=YES,fill=Y)

	
	self.reload()

	


    def reload(self):
	self.clear()
	res=polotptmeth.src()
	self.srctxt.insert("1.0",res)

	res=polotptmeth.des()
	self.destxt.insert("1.0",res)


	res=polotptmeth.pol()
	self.poltxt.insert("1.0",res)

	res=polotptmeth.prtcl()
	self.prtcltxt.insert("1.0",res)

	res=polotptmeth.misc()
	self.misctxt.insert("1.0",res)



    def clear(self):	
	self.srctxt.delete("1.0",END)
	self.destxt.delete("1.0",END)
	self.poltxt.delete("1.0",END)
	self.misctxt.delete("1.0",END)
	self.prtcltxt.delete("1.0",END)
	

 

	
