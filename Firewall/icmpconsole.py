from Tkinter import *
import icmpfltr

class icmpfltcnsl:
    def show(self,mainfrm):

	txtfont=("FreeSerif", 11,"bold")

	icmpfltfrm=Frame(mainfrm,relief=SOLID,borderwidth=1,bg="white")


	#---------------Information text for ICMP console--------------------------
	icmpflttxtfrm=Frame(icmpfltfrm,relief=SOLID,borderwidth=0,bg="white")

	#logo
        icmplogo = PhotoImage(file="icon/info.gif")
        logo=Label(icmpflttxtfrm,image=icmplogo,relief=FLAT,bg="white",width=80,height=80,borderwidth=0)
        logo.photo=icmplogo
        logo.pack(side=LEFT,anchor=W,expand=YES,fill=X)

	infotxt="ICMP filtering allows you to restrict control packet creation and"+"\n"+\
	"reception by the firewall, potentially preventing Denial of Service"+"\n"+\
	"attacks, but also disables many common network tools."+"\n"
	info=Label(icmpflttxtfrm,text=infotxt,font=("FreeSerif",14,"bold"),\
	borderwidth=1,relief=FLAT,width=58,height=4,bg="white")
        info.pack(side=LEFT,anchor=W,pady=0,expand=YES,fill=BOTH)
	


	icmpflttxtfrm.pack(side=TOP,expand=YES,fill=BOTH)
	
	

	#-----------------------------------CheckBoxes Area for ICMP console--------------------------------------
	chkfrm=Frame(icmpfltfrm,relief=SOLID,borderwidth=0,bg="white")

	#----------------------------------------checkboxes left frame-----------------------------------------
        chklfrm=Frame(chkfrm,relief=SOLID,borderwidth=0,bg="white")

	#Echo Request
	self.echoreq=BooleanVar()
	echoreqchkbtn=Checkbutton(chklfrm,text="Echo request\t",font=txtfont,variable=self.echoreq,bg="white",\
	borderwidth=0,activebackground="white")
	echoreqchkbtn.pack(side=TOP,anchor=W,expand=YES,fill=X,pady=22)
	self.echoreq.set(False)

	#Echo Reply
	self.echorply=BooleanVar()
	echorplychkbtn=Checkbutton(chklfrm,text="Echo reply   ",font=txtfont,variable=self.echorply,bg="white",\
	borderwidth=0,activebackground="white")
	echorplychkbtn.pack(side=TOP,anchor=W,expand=YES,fill=X,pady=22)
	self.echorply.set(False)
      
	#Timestamping
	self.tymstmpng=BooleanVar()
	tymstmpngchkbtn=Checkbutton(chklfrm,text="Timestamping",font=txtfont,variable=self.tymstmpng,bg="white",\
	borderwidth=0,activebackground="white")
	tymstmpngchkbtn.pack(side=TOP,anchor=W,expand=YES,fill=X,pady=22)
	self.tymstmpng.set(False)
        
  
	chklfrm.pack(side=LEFT,expand=YES,fill=BOTH)
	
	#-------------------------------checkboxes middle frame----------------------------------------------
        chkmfrm=Frame(chkfrm,relief=SOLID,height=6,borderwidth=0,bg="white")
	
	#Address Masking
	self.adrsmskng=BooleanVar()
	adrsmskngchkbtn=Checkbutton(chkmfrm,text="Address Masking ",font=txtfont,variable=self.adrsmskng,bg="white",\
	borderwidth=0,activebackground="white")
	adrsmskngchkbtn.pack(side=TOP,anchor=W,expand=YES,fill=X,pady=22)
	self.adrsmskng.set(False)

	#Redirection
	self.rdrcsn=BooleanVar()
	rdrcsnchkbtn=Checkbutton(chkmfrm,text="Redirection"+"\t"*2,font=txtfont,variable=self.rdrcsn,bg="white",\
	borderwidth=0,activebackground="white")
	rdrcsnchkbtn.pack(side=TOP,anchor=W,expand=YES,fill=X,pady=22)
	self.rdrcsn.set(False)
      
	#Source-Quenching
	self.srcqnchng=BooleanVar()
	srcqnchngchkbtn=Checkbutton(chkmfrm,text="Source Quenching",font=txtfont,variable=self.srcqnchng,bg="white",\
	borderwidth=0,activebackground="white")
	srcqnchngchkbtn.pack(side=TOP,anchor=W,expand=YES,fill=X,pady=22)
	self.srcqnchng.set(False)
        
  
	chkmfrm.pack(side=LEFT,expand=YES,fill=BOTH)
	
	
	#----------------------------checkboxes right frame------------------------------------------------------
        chkrfrm=Frame(chkfrm,relief=SOLID,height=6,borderwidth=0,bg="white")

	 
	#Parameter Problem
	self.prmtrprb=BooleanVar()
	prmtrprbchkbtn=Checkbutton(chkrfrm,text="Parameter Problem",font=txtfont,variable=self.prmtrprb,bg="white",\
	borderwidth=0,activebackground="white")
	prmtrprbchkbtn.pack(side=TOP,anchor=W,expand=YES,fill=X,pady=22)
	self.prmtrprb.set(False)

	#Unreachable
	self.unrchbl=BooleanVar()
	unrchblchkbtn=Checkbutton(chkrfrm,text="Unreachable"+"\t"*2,font=txtfont,variable=self.unrchbl,bg="white",\
	borderwidth=0,activebackground="white")
	unrchblchkbtn.pack(side=TOP,anchor=W,expand=YES,fill=X,pady=22)
	self.unrchbl.set(False)
      
	#Any
	self.any=BooleanVar()
	anychkbtn=Checkbutton(chkrfrm,text="Any  "+"\t"*3,font=txtfont,variable=self.any,bg="white",\
	borderwidth=0,activebackground="white")
	anychkbtn.pack(side=TOP,anchor=W,expand=YES,fill=X,pady=22)
	self.any.set(False)
        
  
	chkrfrm.pack(side=LEFT,expand=YES,fill=BOTH)


	chkfrm.pack(side=TOP,expand=YES,fill=BOTH)
	#---------------------------------------------Block button--------------------------------------------------
	icmpfltbtnfrm=Frame(icmpfltfrm,relief=SOLID,borderwidth=0,bg="white")
	
        addbtn=Button(icmpfltbtnfrm,text="Block/Unblock Rules",command=self.block,bg="white",\
	font=txtfont,relief=RAISED,width=18,height=1)
        addbtn.pack(side=TOP,anchor=CENTER,pady=4)

 	icmpfltbtnfrm.pack(side=TOP,expand=YES,fill=BOTH)

	return icmpfltfrm


    def block(self):
	icmpfltr.blck(self)

