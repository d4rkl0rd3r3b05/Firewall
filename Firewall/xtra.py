from Tkinter import *
import icmpconsole
import atkconsole


class xtra:
  
    def xtrab(self,prntwin):

	mainwin=Toplevel(master=prntwin)
	mainwin.title("EXTRAS :")
	mainwin.resizable(0,0)
	
	fnt=("FreeSerif", 10,"bold")
	
	mframe=Frame(mainwin,relief=SOLID,borderwidth=1,bg="white")
	tbfrm=Frame(mframe,relief=SOLID,borderwidth=1,bg="white")
	
	#ICMP Filtering Tab	
	icmpbtn=Button(tbfrm,text="ICMP Filtering",command=self.icmp,\
		font=fnt,relief=RAISED,width=12,height=2,bg="white")
        icmpbtn.pack(side=TOP,anchor=N,pady=0)
	
	
	#Attack Filtering Tab
	atkbtn=Button(tbfrm,text="Attack Filtering",command=self.attack,\
		font=fnt,relief=RAISED,width=12,height=2,bg="white")
        atkbtn.pack(side=TOP,anchor=N,pady=0)

	
	tbfrm.pack(side=LEFT,anchor=N,expand=YES,fill=X)

	

	#---------ICMP Filtering Frame----------
	self.icmpfltobj=icmpconsole.icmpfltcnsl()
	self.icmpfltfrm=self.icmpfltobj.show(mframe)
	self.icmpfltfrm.pack(side=LEFT,expand=YES,fill=X)
	
	#---------Attack Filtering Frame------------
	self.atkfltobj=atkconsole.atkfltcnsl()
	self.atkfltfrm=self.atkfltobj.show(mframe)
	
	
	mframe.pack(side=LEFT,anchor=W,expand=YES,fill=Y)
	mainwin.mainloop()	
	

	
	
    def icmp(self):
	self.atkfltfrm.pack_forget()
	self.icmpfltfrm.pack(side=LEFT,expand=YES,fill=X)
	
	

    def attack(self):
	self.icmpfltfrm.pack_forget()
	self.atkfltfrm.pack(side=LEFT,expand=YES,fill=X)



xtraobj=xtra()
def xtrawin(mnwin):
	xtraobj.xtrab(mnwin)
	
