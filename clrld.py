from Tkinter import *
import os
import tkFileDialog
import tkMessageBox


def clear(win):	
	win.spctab.sttsobj.clear()
	win.spctab.polobj.clear()
def reload(win):
	win.spctab.sttsobj.reload()
	win.spctab.polobj.reload()
def save():
	ruleflname=tkFileDialog.asksaveasfilename(filetypes=[("Firewall Rules",".rules")],defaultextension=".rules")
	if(ruleflname!=""):	
		os.popen('iptables-save > '+ruleflname,"r")
		tkMessageBox.showinfo("Saved","Firewall Rules have been saved as: "+ruleflname)
def restore():
	ruleflname=tkFileDialog.askopenfilename(filetypes=[("Firewall Rules",".rules")])
	if(ruleflname!=""):	
		os.popen('iptables-restore < '+ruleflname,"r")
		tkMessageBox.showinfo("Restored","Firewall Rules have been restored from: "+ruleflname)

