from Tkinter import *
import atkfltr

class atkfltcnsl:
    def show(self,mainfrm):

	txtfont=("FreeSerif", 11,"bold")

	atkfltfrm=Frame(mainfrm,relief=SOLID,borderwidth=1,bg="white")


	#---------------Information text for Attack console--------------------------
	atkflttxtfrm=Frame(atkfltfrm,relief=SOLID,borderwidth=0,bg="white")

	#logo
        atklogo = PhotoImage(file="icon/info.gif")
        logo=Label(atkflttxtfrm,image=atklogo,relief=FLAT,bg="white",width=80,height=80,borderwidth=0)
        logo.photo=atklogo
        logo.pack(side=LEFT,anchor=W,expand=YES,fill=X)

	infotxt="Malformed network packets can be used for reconnaissancing or"+"\n"+\
	"breaching.Attack filtering allows you to prevent such attacks,"+"\n"+\
	" but also disables many common network tools."+"\n"
	info=Label(atkflttxtfrm,text=infotxt,font=("FreeSerif",14,"bold"),\
	borderwidth=1,relief=FLAT,width=58,height=4,bg="white")
        info.pack(side=LEFT,anchor=W,pady=0,expand=YES,fill=BOTH)
	


	atkflttxtfrm.pack(side=TOP,expand=YES,fill=BOTH)
	
	

	#-----------------------------------CheckBoxes Area for atk console--------------------------------------
	chkfrm=Frame(atkfltfrm,relief=SOLID,borderwidth=0,bg="white")

	#----------------------------------------checkboxes left frame-----------------------------------------
        chklfrm=Frame(chkfrm,relief=SOLID,borderwidth=0,bg="white")

	#SYN Flooding
	self.syn=BooleanVar()
	synchkbtn=Checkbutton(chklfrm,text="SYN Flooding\t",font=txtfont,variable=self.syn,bg="white",\
	borderwidth=0,activebackground="white")
	synchkbtn.pack(side=TOP,anchor=W,expand=YES,fill=X,pady=22)
	self.syn.set(False)

	#Server Panic
	self.srvrpnc=BooleanVar()
	srvrpncchkbtn=Checkbutton(chklfrm,text="Server Panic  ",font=txtfont,variable=self.srvrpnc,bg="white",\
	borderwidth=0,activebackground="white")
	srvrpncchkbtn.pack(side=TOP,anchor=W,expand=YES,fill=X,pady=22)
	self.srvrpnc.set(False)
     
	chklfrm.pack(side=LEFT,expand=YES,fill=BOTH)
	
	#----------------------------checkboxes right frame----------------------------------------------------
        chkrfrm=Frame(chkfrm,relief=SOLID,height=6,borderwidth=0,bg="white")

	 
	#Xmas Attack
	self.xmas=BooleanVar()
	xmaschkbtn=Checkbutton(chkrfrm,text="Xmas Attack",font=txtfont,variable=self.xmas,bg="white",\
	borderwidth=0,activebackground="white")
	xmaschkbtn.pack(side=TOP,anchor=W,expand=YES,fill=X,pady=22)
	self.xmas.set(False)

	#Null Attack
	self.null=BooleanVar()
	nullchkbtn=Checkbutton(chkrfrm,text="Null Attack   "+"\t",font=txtfont,variable=self.null,bg="white",\
	borderwidth=0,activebackground="white")
	nullchkbtn.pack(side=TOP,anchor=W,expand=YES,fill=X,pady=22)
	self.null.set(False)
      
	
	chkrfrm.pack(side=LEFT,expand=YES,fill=BOTH)


	chkfrm.pack(side=TOP,expand=YES,fill=BOTH)
	#---------------------------------------------Block button--------------------------------------------------
	atkfltbtnfrm=Frame(atkfltfrm,relief=SOLID,borderwidth=0,bg="white")
	
        addbtn=Button(atkfltbtnfrm,text="Block/Unblock Attacks",command=self.block,bg="white",\
	font=txtfont,relief=RAISED,width=18,height=1)
        addbtn.pack(side=TOP,anchor=CENTER,pady=4)

 	atkfltbtnfrm.pack(side=TOP,expand=YES,fill=BOTH)

	return atkfltfrm


    def block(self):
	atkfltr.blck(self)

