from Tkinter import *
import clrld
import firewl
import rulesmeth
import apnd
import inst
import delete
import tkMessageBox



class dockbr:
    def __init__(self,prntwin):
	self.win=prntwin
	self.firwlstts=1
	
    def dock(self,mframe):

        tfrm=Frame(mframe,relief=SOLID,borderwidth=1)
        
	#---------------------------------Status Page DockBar-------------------------------------------------
	
	#Xtra Dock
	statusfrm=Frame(tfrm,relief=SOLID,borderwidth=1)
	imgprfrncs = PhotoImage(file="icon/xtra.gif")
        btnprfrncs= Button(statusfrm,width=48,height=48,image=imgprfrncs,bg='white',command=self.win.xtra)
	btnprfrncs.pack(side=LEFT, padx=2, pady=2)
	btnprfrncs.image = imgprfrncs

	#Enable Dock
	imgenb = PhotoImage(file="icon/enable.gif")
        self.btnenb= Button(statusfrm,width=48,height=48,image=imgenb,bg='white',command=self.enable,state=DISABLED)
	self.btnenb.pack(side=LEFT, padx=2, pady=2)
	self.btnenb.image = imgenb 
	
	#Disable Dock
	imgdisbl = PhotoImage(file="icon/disable.gif")
        self.btndisbl= Button(statusfrm,width=48,height=48,image=imgdisbl,bg='white',command=self.disable)
	self.btndisbl.pack(side=LEFT, padx=2, pady=2)
	self.btndisbl.image = imgdisbl 
	
	#Flush Dock
	imgfls = PhotoImage(file="icon/fls.gif")
        btnfls= Button(statusfrm,width=48,height=48,image=imgfls,bg='white',command=firewl.flush)
	btnfls.pack(side=LEFT, padx=2, pady=2)
	btnfls.image = imgfls 
 

	#---------------------------------Event Page DockBar-------------------------------------------------
	
	#Save Dock
	imgsave = PhotoImage(file="icon/save.gif")
        btnsave= Button(statusfrm,width=48,height=48,image=imgsave,bg='white',command=clrld.save)
	btnsave.pack(side=LEFT, padx=2, pady=2)
	btnsave.image = imgsave
	
	#Restore Dock
	imgres = PhotoImage(file="icon/res.gif")
        btnres= Button(statusfrm,width=48,height=48,image=imgres,bg='white',command=clrld.restore)
	btnres.pack(side=LEFT, padx=2, pady=2)
	btnres.image = imgres
		
	#Clear Dock
	imgclr = PhotoImage(file="icon/clr.gif")
        btnclr= Button(statusfrm,width=48,height=48,image=imgclr,bg='white',command=self.clear)
	btnclr.pack(side=LEFT, padx=2, pady=2)
	btnclr.image = imgclr  

	#Reload Dock
	imgrld = PhotoImage(file="icon/rld.gif")
        btnrld= Button(statusfrm,width=48,height=48,image=imgrld,bg='white',command=self.reload)
	btnrld.pack(side=LEFT, padx=2, pady=2)	
	btnrld.image = imgrld 
	

	#---------------------------------Policy Page DockBar-------------------------------------------------
	
	#Add Dock
	imgadd = PhotoImage(file="icon/add.gif")
        btnadd= Button(statusfrm,width=48,height=48,image=imgadd,bg='white',command=self.apnd)
	btnadd.pack(side=LEFT, padx=2, pady=2)
	btnadd.image = imgadd
	
	#Delete Dock
	imgrmv = PhotoImage(file="icon/rmv.gif")
        btnrmv= Button(statusfrm,width=48,height=48,image=imgrmv,bg='white',command=self.delete)
	btnrmv.pack(side=LEFT, padx=2, pady=2)
	btnrmv.image = imgrmv  

	#Insert Dock
	imgedt = PhotoImage(file="icon/insert.gif")
        btnedt= Button(statusfrm,width=48,height=48,image=imgedt,bg='white',command=self.inst)
	btnedt.pack(side=LEFT, padx=2, pady=2)
	btnedt.image = imgedt 
	
	#Default Dock
	imgdef = PhotoImage(file="icon/default.gif")
        btndef= Button(statusfrm,width=48,height=48,image=imgdef,bg='white',command=rulesmeth.default)
	btndef.pack(side=LEFT, padx=2, pady=2)
	btndef.image = imgdef

	
	statusfrm.pack(side=TOP,expand=YES,fill=X)


	tfrm.pack(side=TOP,expand=YES,fill=X)


    #-------------------------------------Enable button code----------------------------------------
    def enable(self):
	if(self.firwlstts==0):
		firewl.enable()
		self.btnenb["state"]=DISABLED
		self.btndisbl["state"]=ACTIVE
		self.firwlstts=1
	else:
		tkMessageBox.showinfo("Enabled","The Firewall is already Enabled.")
	

    #-------------------------------------Enable button code----------------------------------------
    def disable(self):
	if(self.firwlstts==1):
		stts=firewl.disable()
		if(stts=="yes"):
			self.btndisbl ["state"]=DISABLED
			self.btnenb["state"]=ACTIVE
			self.firwlstts=0
	else:
		tkMessageBox.showinfo("Disabled","The Firewall is already Disabled.")
	
    #-------------------------------------Clear button Code-------------------------------------------
    def clear(self):
	clrld.clear(self.win)

    #-------------------------------------Reload button Code-------------------------------------------
    def reload(self):
	clrld.reload(self.win)

    #-------------------------------------Append button Code-------------------------------------------
    def apnd(self):
	apnd.apndwn(self.win)

    #-------------------------------------Insert button Code-------------------------------------------
    def inst(self):
	inst.instwn(self.win)

    #-------------------------------------Delete button Code-------------------------------------------
    def delete(self):
	delete.deletion(self.win)
