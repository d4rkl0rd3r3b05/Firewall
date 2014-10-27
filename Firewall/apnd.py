from Tkinter import *
import os

class apndwin:
    def apndwin(self,prntwin):

	mainwin=Toplevel(master=prntwin)
	mainwin.resizable(0,0)
   	mainwin.title("Append Rule")
	

        #-----------------------------------------This is mainframe--------------------------------------------
        mframe=Frame(mainwin)

	fnt=("FreeSerif",11,"bold")
	fntopt=("FreeSerif",10)
	fnttxt=("FreeSerif",12)
        #------------------------------------------Chain--------------------------------------------------
        #chain frame
	chnfrm=Frame(mframe)
        #chain label
        chnlbl=Label(chnfrm,text="Chain"+"\t"*4,font=fnt,relief=FLAT,width=24)
        chnlbl.pack(side=LEFT,pady=4)
        #chain options
       	self.chn=StringVar()

	self.chn.set("INPUT") 

	chnopt = OptionMenu(chnfrm,self.chn,"INPUT","OUTPUT")
	chnopt["font"]=fntopt
	chnopt["width"]=18
	chnopt.pack()

	chnfrm.pack(expand=YES,fill=BOTH)

	
	#------------------------------------------Action--------------------------------------------------
        #Action frame
	actfrm=Frame(mframe)
        #Action label
        actlbl=Label(actfrm,text="Action"+"\t"*4,font=fnt,relief=FLAT,width=24)
        actlbl.pack(side=LEFT,pady=4)
        #Action option
	self.act=StringVar()
	self.act.set("REJECT")

	actopt = OptionMenu(actfrm,self.act,"REJECT", "DROP", "LOG","ACCEPT","RETURN")
	actopt["font"]=fntopt
	actopt["width"]=18
	actopt.pack()


	actfrm.pack(expand=YES,fill=BOTH)
      	
	#--------------------------------------Protocol------------------------------------------------------
	#Protocol frame
        protofrm=Frame(mframe)
	
        #protocol label
        protolbl=Label(protofrm,text="Protocol"+"\t"*4,font=fnt,relief=FLAT,width=24)
        protolbl.pack(side=LEFT,pady=4)
       
	
	#protocol option
	self.proto=StringVar()
	self.proto.set("tcp")

	protoopt = OptionMenu(protofrm,self.proto,"TCP", "UDP","SCTP", "ICMP","UDPLITE","ESP","AH","ALL")
	protoopt["font"]=fntopt
	protoopt["width"]=18
	protoopt.pack()

      
	protofrm.pack(expand=YES,fill=X)

	#-----------------------------------------source address-----------------------------------------------
	#source address frame
	srcaddfrm=Frame(mframe)
	self.srcadd=StringVar()
	#source address label
        srcaddlbl=Label(srcaddfrm,text="Source Address"+"\t"*3,font=fnt,relief=FLAT,width=24)
        srcaddlbl.pack(side=LEFT,pady=4)
        
	#source address text
	srcaddtxt=Entry(srcaddfrm,textvariable=self.srcadd,font=fnttxt,relief=SUNKEN)
        srcaddtxt.pack(side=LEFT,pady=4)
	
	srcaddfrm.pack(expand=YES,fill=X)	
	
	#-----------------------------------------source port-----------------------------------------------
	#source port frame
	srcprtfrm=Frame(mframe)
	self.srcprt=StringVar()
	#source port label
        srcprtlbl=Label(srcprtfrm,text="Source Port"+"\t"*3,font=fnt,relief=FLAT,width=24)
        srcprtlbl.pack(side=LEFT,pady=4)
        
	#source port text
	srcprttxt=Entry(srcprtfrm,textvariable=self.srcprt,font=fnttxt,relief=SUNKEN)
        srcprttxt.pack(side=LEFT,pady=4)
	
	srcprtfrm.pack(expand=YES,fill=X)
      
	
	#-----------------------------------------destination address-----------------------------------------------
	#destination address frame
	desaddfrm=Frame(mframe)
	self.desadd=StringVar()
	#destination address label
        desaddlbl=Label(desaddfrm,text="Destination Address"+"\t"*2,font=fnt,relief=FLAT,width=24)
        desaddlbl.pack(side=LEFT,pady=4)
        
	#desination address text
	desaddtxt=Entry(desaddfrm,textvariable=self.desadd,font=fnttxt,relief=SUNKEN)
        desaddtxt.pack(side=LEFT,pady=4)
	
	desaddfrm.pack(expand=YES,fill=X)	
	
	#-----------------------------------------destination port-----------------------------------------------
	#destination port frame
	desprtfrm=Frame(mframe)
	self.desprt=StringVar()
	#desination port label
        desprtlbl=Label(desprtfrm,text="Destination Port"+"\t"*3,font=fnt,relief=FLAT,width=24)
        desprtlbl.pack(side=LEFT,pady=4)
        
	#desination port text
	desprttxt=Entry(desprtfrm,textvariable=self.desprt,font=fnttxt,relief=SUNKEN)
        desprttxt.pack(side=LEFT,pady=4)
	
	desprtfrm.pack(expand=YES,fill=X)


	#---------------------------------------------Append button--------------------------------------------------
        addbtn=Button(mframe,text="Append Rule",command=self.apnd,\
	font=fnt,relief=RAISED,width=18,height=1)
        addbtn.pack(side=TOP,anchor=CENTER,pady=4)

      	
	mframe.pack(expand=YES,fill=BOTH)
	

	mainwin.mainloop()

    def apnd(self):
	

	chain='iptables -A '+self.chn.get()
	action=' -j '+self.act.get()
	
	#--------------------------------------------------------------------
	if(self.chn.get()=="INPUT"):
		if(self.srcadd.get()!=""):
			addrs=' -s '+self.srcadd.get()
		else:	
			addrs=' -s 0/0'
	else:	
		if(self.desadd.get()!=""):
			addrs=' -d '+self.desadd.get()
		else:	
			addrs=' -d 0/0'
	
		

	#---------------------------------------------------------------------
	if(self.proto!=""):
		prtcl=' -p '+self.proto.get()
	else:	
		prtcl=""
	
	#---------------------------------------------------------------------
	if(self.srcprt.get()!=""):
		sprt=' --sport '+self.srcprt.get()
	else:	
		sprt=""

	#---------------------------------------------------------------------
	if(self.desprt.get()!=""):
		dprt=' --dport '+self.desprt.get()
	else:	
		dprt=""


	try:
		os.popen(chain+prtcl+addrs+sprt+dprt+action,"r")
	except:
		pass



apndobj=apndwin()
def apndwn(mnwin):
	apndobj.apndwin(mnwin)	
        

       

