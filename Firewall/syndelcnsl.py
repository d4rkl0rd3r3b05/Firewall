from Tkinter import *
import os
import tkMessageBox

class syndelcnsl:
    def show(self,mainfrm):

	#-----------------------------------------This is mainframe--------------------------------------------
        syndelfrm=Frame(mainfrm,relief=SOLID,borderwidth=1,bg="white")
	txtfont=("FreeSerif", 11,"bold")
	fnt=("FreeSerif",11,"bold")
	fntopt=("FreeSerif",10)
	fnttxt=("FreeSerif",12)
	
      	#------------Chain------------
        #chain frame
	chnfrm=Frame(syndelfrm,bg="white")
        #chain label
        chnlbl=Label(chnfrm,text="Chain"+"\t"*4,font=txtfont,relief=FLAT,width=24,bg="white")
        chnlbl.pack(side=LEFT)
        #chain options
       	self.chn=StringVar()

	self.chn.set("INPUT") 

	chnopt = OptionMenu(chnfrm,self.chn,"INPUT","OUTPUT","FORWARD")
	chnopt["bg"]="white"
	chnopt["font"]=fntopt
	chnopt["width"]=18
	chnopt.pack(side=RIGHT)

	chnfrm.pack(expand=YES,fill=BOTH)

	
	
	#------------------------------------------Action--------------------------------------------------
        #Action frame
	actfrm=Frame(syndelfrm,bg="white")
        #Action label
        actlbl=Label(actfrm,text="Action"+"\t"*4,font=fnt,relief=FLAT,width=24,bg="white")
        actlbl.pack(side=LEFT,pady=4)

        #chain options
       	self.act=StringVar()
	self.act.set("REJECT") 

	actopt = OptionMenu(actfrm,self.act,"REJECT", "DROP", "LOG","ACCEPT","RETURN")
	actopt["bg"]="white"
	actopt["font"]=fntopt
	actopt["width"]=18
	actopt.pack(side=RIGHT)

	actfrm.pack(expand=YES,fill=BOTH)
      	
	#--------------------------------------Protocol------------------------------------------------------
	#Protocol frame
        protofrm=Frame(syndelfrm,bg="white")
	
        #protocol label
        protolbl=Label(protofrm,text="Protocol"+"\t"*4,font=fnt,relief=FLAT,width=24,bg="white")
        protolbl.pack(side=LEFT,pady=4)
       
	
	#protocol options 
       	self.proto=StringVar()
	self.proto.set("tcp") 

	protoopt = OptionMenu(protofrm,self.proto,"tcp", "udp","sctp", "icmp","udplite","esp","ah","all")
	protoopt["bg"]="white"
	protoopt["font"]=fntopt
	protoopt["width"]=18
	protoopt.pack(side=RIGHT)
 
	protofrm.pack(expand=YES,fill=X)

	#-----------------------------------------source address-----------------------------------------------
	#source address frame
	srcaddfrm=Frame(syndelfrm,bg="white") 
	self.srcadd=StringVar()
	#source address label
        srcaddlbl=Label(srcaddfrm,text="Source Address"+"\t"*3,font=fnt,relief=FLAT,width=24,bg="white")
        srcaddlbl.pack(side=LEFT,pady=4)
        
	#source address text
	srcaddtxt=Entry(srcaddfrm,textvariable=self.srcadd,relief=SUNKEN,bg="white")
        srcaddtxt.pack(side=LEFT,pady=4)
	
	srcaddfrm.pack(expand=YES,fill=X)	
	
	#-----------------------------------------source port-----------------------------------------------
	#source port frame
	srcprtfrm=Frame(syndelfrm,bg="white") 
	self.srcprt=StringVar()
	#source port label
        srcprtlbl=Label(srcprtfrm,text="Source port"+"\t"*3,font=fnt,relief=FLAT,width=24,bg="white")
        srcprtlbl.pack(side=LEFT,pady=4)
        
	#source port text
	srcprttxt=Entry(srcprtfrm,textvariable=self.srcprt,relief=SUNKEN,bg="white")
        srcprttxt.pack(side=LEFT,pady=4)
	
	srcprtfrm.pack(expand=YES,fill=X)
      
	
	#-----------------------------------------destination address-----------------------------------------------
	#destination address frame
	desaddfrm=Frame(syndelfrm,bg="white") 
	self.desadd=StringVar()
	#destination address label
        desaddlbl=Label(desaddfrm,text="Destination Address"+"\t"*2,font=fnt,relief=FLAT,width=24,bg="white")
        desaddlbl.pack(side=LEFT,pady=4)
        
	#desination address text
	desaddtxt=Entry(desaddfrm,textvariable=self.desadd,relief=SUNKEN,bg="white")
        desaddtxt.pack(side=LEFT,pady=4)
	
	desaddfrm.pack(expand=YES,fill=X)	
	
	#-----------------------------------------destination port-----------------------------------------------
	#destination port frame
	desprtfrm=Frame(syndelfrm,bg="white") 
	self.desprt=StringVar()
	#desination port label
        desprtlbl=Label(desprtfrm,text="Destination port"+"\t"*3,font=fnt,relief=FLAT,width=24,bg="white")
        desprtlbl.pack(side=LEFT,pady=4)
        
	#desination port text
	desprttxt=Entry(desprtfrm,textvariable=self.desprt,relief=SUNKEN,bg="white")
        desprttxt.pack(side=LEFT,pady=4)
	
	desprtfrm.pack(expand=YES,fill=X)

	#---------------------------------------------Delete button--------------------------------------------------
        delbtn=Button(syndelfrm,text="Delete Rule",command=self.delr,\
	font=fnt,relief=RAISED,width=18,height=1,bg="white")
      	delbtn.pack(side=TOP,anchor=CENTER,pady=4)

      	
	return syndelfrm


    def delr(self):
	
	if (not tkMessageBox.askyesno("Delete", "Do you really want to Delete specified rule?")):
		return	
	chain='iptables -D '+self.chn.get()
	action=' -j '+self.act.get()
	
	#--------------------------------------------------------------------
	if(self.chn.get()=="INPUT"):
		if(self.srcadd.get()!=""):
			addrs=' -s '+self.srcadd.get()
		else:	
			addrs=" -s 0/0"
	else:	
		if(self.desadd.get()!=""):
			addrs=' -d '+self.desadd.get()
		else:	
			addrs=" -d 0/0"
	

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

	#---------------------------------------------------------------------
	if(self.proto.get()!=""):
		proto=' -p '+self.proto.get()
	else:	
		proto=""

	try:
		print chain+proto+addrs+sprt+dprt+action
		os.popen(chain+proto+addrs+sprt+dprt+action,"r")
		tkMessageBox.showinfo("Deleted","Specified rule has been Deleted.")
	except:
		pass

   	


       

