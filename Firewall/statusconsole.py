from Tkinter import *
import sttsotpt

class sttscnsl:
    def show(self,mainfrm):

	txtfont=("FreeSerif", 10,"bold")

	otptsttsfrm=Frame(mainfrm,relief=SOLID,borderwidth=1)
	
	#---------------label for status console------------------------------------------------------------
	oplblfrm=Frame(otptsttsfrm,relief=SOLID,height=1,borderwidth=1)
		
	src=Label(oplblfrm,text="Local",font=txtfont,relief=RAISED,width=16,height=1)
        src.pack(side=LEFT,anchor=CENTER,pady=0)

	srcpt=Label(oplblfrm,text="Source Port",font=txtfont,relief=RAISED,width=15,height=1)
        srcpt.pack(side=LEFT,anchor=CENTER,pady=0)
	
	des=Label(oplblfrm,text="Foreign",font=txtfont,relief=RAISED,width=16,height=1)
        des.pack(side=LEFT,anchor=CENTER,pady=0)

	
	despt=Label(oplblfrm,text="Destination Port",font=txtfont,relief=RAISED,width=15,height=1)
        despt.pack(side=LEFT,anchor=CENTER,pady=0)

	recv=Label(oplblfrm,text="Recieve-Q",font=txtfont,relief=RAISED,width=12,height=1)
        recv.pack(side=LEFT,anchor=CENTER,pady=0)

	send=Label(oplblfrm,text="Send-Q",font=txtfont,relief=RAISED,width=12,height=1)
        send.pack(side=LEFT,anchor=CENTER,pady=0)
	
	prtcl=Label(oplblfrm,text="Protocol",font=txtfont,relief=RAISED,width=12,height=1)
        prtcl.pack(side=LEFT,anchor=CENTER,pady=0)

	stt=Label(oplblfrm,text="State",font=txtfont,relief=RAISED,width=20,height=1)
        stt.pack(side=LEFT,anchor=CENTER,pady=0)
	


	oplblfrm.pack(side=TOP,expand=YES,fill=BOTH)
	
	

	#-------------------Text Area for status console----------------------------------------------------
	#output frame
        optxtfrm=Frame(otptsttsfrm,relief=SOLID,height=30,borderwidth=1)
        

        #text box 4 source address
        
        self.srctxt=Text(optxtfrm,bg="white",fg="black",font=txtfont,width=15,height=30)
        self.srctxt.pack(side=LEFT,expand=YES,fill=BOTH)
	
	      
	
	#text box 4 source port
        
        self.srcpttxt=Text(optxtfrm,bg="white",fg="black",font=txtfont,width=15,height=30)
        self.srcpttxt.pack(side=LEFT,expand=YES,fill=BOTH)

	
        #text box 4 destination address
        
        self.destxt=Text(optxtfrm,bg="white",fg="black",font=txtfont,width=16,height=30)
        self.destxt.pack(side=LEFT,expand=YES,fill=BOTH)

	
       	
        #text box 4 destination port
        
        self.despttxt=Text(optxtfrm,bg="white",fg="black",font=txtfont,width=15,height=30)
        self.despttxt.pack(side=LEFT,expand=YES,fill=BOTH)



	
        #text box 4 recv-Q
        
        self.recvtxt=Text(optxtfrm,bg="white",fg="black",font=txtfont,width=12,height=30)
        self.recvtxt.pack(side=LEFT,expand=YES,fill=BOTH)



	
        #text box 4 send-Q
        
        self.sendtxt=Text(optxtfrm,bg="white",fg="black",font=txtfont,width=12,height=30)
        self.sendtxt.pack(side=LEFT,expand=YES,fill=BOTH)



	
        #text box 4 protocol
        
        self.prtcltxt=Text(optxtfrm,bg="white",fg="black",font=txtfont,width=11,height=30)
        self.prtcltxt.pack(side=LEFT,expand=YES,fill=BOTH,anchor=CENTER)
	
	

	
        #text box 4 status
        
        self.stttxt=Text(optxtfrm,bg="white",fg="black",font=txtfont,width=18,height=30)
        self.stttxt.pack(side=LEFT,expand=YES,fill=BOTH,anchor=CENTER)



	

	optxtfrm.pack(side=TOP,expand=YES,fill=BOTH)
	
        #scroll bar 4 o/p txt
        optxtscrlbar=Scrollbar(optxtfrm,command=self.srctxt.yview and self.stttxt.yview and self.destxt.yview)
	optxtscrlbar=Scrollbar(optxtfrm,command=self.srcpttxt.yview and self.despttxt.yview and self.recvtxt.yview)
 	optxtscrlbar=Scrollbar(optxtfrm,command=self.sendtxt.yview and self.prtcltxt.yview)


	self.srctxt["yscrollcommand"]=optxtscrlbar.set
	self.destxt["yscrollcommand"]=optxtscrlbar.set
	self.srcpttxt["yscrollcommand"]=optxtscrlbar.set
	self.despttxt["yscrollcommand"]=optxtscrlbar.set
	self.recvtxt["yscrollcommand"]=optxtscrlbar.set
	self.sendtxt["yscrollcommand"]=optxtscrlbar.set
	self.prtcltxt["yscrollcommand"]=optxtscrlbar.set
	self.stttxt["yscrollcommand"]=optxtscrlbar.set
	optxtscrlbar.pack(side=RIGHT,expand=YES,fill=Y)

	self.reload()

	return otptsttsfrm


    def reload(self):
	self.clear()
	res=sttsotpt.src()
	self.srctxt.insert("1.0",res)

	res=sttsotpt.srcpt()
	self.srcpttxt.insert("1.0",res)

	res=sttsotpt.des()
	self.destxt.insert("1.0",res)

	res=sttsotpt.despt()
	self.despttxt.insert("1.0",res)
	
	res=sttsotpt.recv()
	self.recvtxt.insert("1.0",res)

	res=sttsotpt.send()
	self.sendtxt.insert("1.0",res)

	res=sttsotpt.prtcl()
	self.prtcltxt.insert("1.0",res)

	res=sttsotpt.stt()
	self.stttxt.insert("1.0",res)

 
    def clear(self):  
    	self.srctxt.delete("1.0",END)
	self.destxt.delete("1.0",END)
	self.srcpttxt.delete("1.0",END)
	self.despttxt.delete("1.0",END)
	self.prtcltxt.delete("1.0",END)
	self.stttxt.delete("1.0",END)
	self.recvtxt.delete("1.0",END)
	self.sendtxt.delete("1.0",END)

