from Tkinter import *
import statusconsole
import policyconsole

class tab:
  
    def ctab(self,mframe):
	
	tbfrm=Frame(mframe,relief=SOLID,borderwidth=1)
	
	#Status Tab	
	statusbtn=Button(tbfrm,text="Status",command=self.status,\
		font=("FreeSerif", 10,"bold"),relief=RAISED,width=12,height=1)
        statusbtn.pack(side=LEFT,anchor=CENTER,pady=0)
	

	#Policy Tab
	policbtn=Button(tbfrm,text="Policy",command=self.policy,\
		font=("FreeSerif", 10,"bold"),relief=RAISED,width=12,height=1)
        policbtn.pack(side=LEFT,anchor=CENTER,pady=0)

	tbfrm.pack(side=TOP,expand=YES,fill=X)

	

	#---------status Frame----------
	self.sttsobj=statusconsole.sttscnsl()
	self.otptsttsfrm=self.sttsobj.show(mframe)
	self.otptsttsfrm.pack(side=TOP,expand=YES,fill=X)

	
	#---------policy Frame------------
	self.polobj=policyconsole.polcnsl()
	self.otptpolicfrm=self.polobj.show(mframe)
		
	

	
	
    def status(self):
	self.otptpolicfrm.pack_forget()
	self.otptsttsfrm.pack(side=TOP,expand=YES,fill=X)
	
	
	
    def policy(self):
	self.otptsttsfrm.pack_forget()
	self.otptpolicfrm.pack(side=TOP,expand=YES,fill=X)
	
