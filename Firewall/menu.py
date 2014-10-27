from Tkinter import *
import firewl
import clrld
import firewl
import rulesmeth
import apnd
import inst
import delete
import tkMessageBox


class menucls:
    def __init__(self,prntwin):
	self.win=prntwin

    def menu(self):
	#-------------------Menu Bar---------------------------------
	menubar=Menu(self.win)
	self.win["menu"]=menubar
	
	
	#------------------Status Menu Items------------------------
	statusmenu=Menu(menubar)
	statusmenu.add_command(label="Start Firewall",underline=0,command=self.win.enable)
	statusmenu.add_command(label="Stop Firewall",underline=3,command=self.win.disable)
	statusmenu.add_command(label="Flush",underline=2,command=firewl.flush)
	statusmenu.add_separator()
	statusmenu.add_command(label="Quit",underline=0,command=self.quit)
	#------------------Edit Menu Items------------------------
	editmenu=Menu(menubar)
	editmenu.add_command(label="Interfaces",underline=0,command=self.win.interfaces)
	editmenu.add_command(label="Default Settings",underline=0,command=rulesmeth.default)
	editmenu.add_separator()
	editmenu.add_command(label="Extras",underline=1,command=self.win.xtra)
	#------------------Event Menu Items------------------------
	eventmenu=Menu(menubar)
	eventmenu.add_command(label="Clear",underline=0,command=self.clear)
	eventmenu.add_command(label="Reload",underline=2,command=self.reload)
	eventmenu.add_separator()
	eventmenu.add_command(label="Save Rules",underline=0,command=clrld.save)
	eventmenu.add_command(label="Restore Rules",underline=0,command=clrld.restore)
	#------------------Policy Menu Items------------------------
	policmenu=Menu(menubar)
	policmenu.add_command(label="Append Rule",underline=0,command=self.apnd)
	policmenu.add_command(label="Delete Rule",underline=0,command=self.delete)
	policmenu.add_command(label="Insert Rule",underline=0,command=self.inst)
	policmenu.add_separator()
	policmenu.add_command(label="Show Rule",underline=0,command=self.win.policy)
	#------------------Policy Menu Items------------------------
	helpmenu=Menu(menubar)
	helpmenu.add_command(label="Help",underline=0,command=self.win.hlp)
	helpmenu.add_separator()
	helpmenu.add_command(label="Copyright",underline=0,command=self.win.cprght)
	helpmenu.add_command(label="About Us",underline=0,command=self.win.crd)

	menubar.add_cascade(label="Firewall",underline=0,menu=statusmenu)
	menubar.add_cascade(label="Edit",underline=0,menu=editmenu)
	menubar.add_cascade(label="Event",underline=1,menu=eventmenu)
	menubar.add_cascade(label="Policy",underline=0,menu=policmenu)
	menubar.add_cascade(label="Help",underline=0,menu=helpmenu)



    #-------------------------------------Clear Menu Item Code-------------------------------------------
    def clear(self):
	clrld.clear(self.win)

    #-------------------------------------Reload Menu Item Code-------------------------------------------
    def reload(self):
	clrld.reload(self.win)

    #-------------------------------------Quit Menu Item Code--------------------------------------------
    def quit(self):
	if (not tkMessageBox.askyesno("Exit", "Do you really want to Quit?")):
		return
	self.win.destroy()

   #-------------------------------------Append Menu Item Code-------------------------------------------
    def apnd(self):
	apnd.apndwn(self.win)

   #-------------------------------------Insert Menu Item Code-------------------------------------------
    def inst(self):
	inst.instwn(self.win)
 
    #-------------------------------------Insert Menu Item Code-------------------------------------------
    def delete(self):
	delete.deletion(self.win)
 
    
  

   

