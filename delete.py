from Tkinter import *
import nonsyndelcnsl
import syndelcnsl


class deletionwn:
  
    def deletionwn(self,prntwin):

	mainwin=Toplevel(master=prntwin)
	mainwin.title("DELETION :")
	mainwin.resizable(0,0)
	
	fnt=("FreeSerif", 10,"bold")
	
	mframe=Frame(mainwin,relief=SOLID,borderwidth=1,bg="white")
	tbfrm=Frame(mframe,relief=SOLID,borderwidth=1,bg="white")

	

	#Non-Syntactical Deletion Tab
	nonsyndelbtn=Button(tbfrm,text="Non-Syntactical Deletion",command=self.nonsyndel,\
		font=fnt,relief=RAISED,width=18,height=2,bg="white")
        nonsyndelbtn.pack(side=TOP,anchor=N,pady=0)	



	#Syntactical Deletion Tab	
	syndelbtn=Button(tbfrm,text="Syntactical Deletion",command=self.syndel,\
		font=fnt,relief=RAISED,width=18,height=2,bg="white")
        syndelbtn.pack(side=TOP,anchor=N,pady=0)
	

	
	tbfrm.pack(side=LEFT,anchor=N,expand=YES,fill=X)

	

	#---------Non-Syntactical Deletion Frame----------
	self.nonsyndelobj=nonsyndelcnsl.nonsyndelcnsl()
	self.nonsyndelfrm=self.nonsyndelobj.show(mframe)
	self.nonsyndelfrm.pack(side=LEFT,expand=YES,fill=X)
	
	#---------Syntactical Deletion Frame------------
	self.syndelobj=syndelcnsl.syndelcnsl()
	self.syndelfrm=self.syndelobj.show(mframe)
		
	mframe.pack(side=LEFT,anchor=W,expand=YES,fill=Y)
	mainwin.mainloop()	
	

	
	
    def nonsyndel(self):
	self.syndelfrm.pack_forget()
	self.nonsyndelfrm.pack(side=LEFT,expand=YES,fill=X)
	
	

    	
    def syndel(self):
	self.nonsyndelfrm.pack_forget()
	self.syndelfrm.pack(side=LEFT,expand=YES,fill=X)
	


deletionobj=deletionwn()
def deletion(mnwin):
	deletionobj.deletionwn(mnwin)
	




