from  Tkinter import *
from menu import *
from dock import *
from tab import *
import sys
import copyright
import credit
import help
import interfaces
import xtra



class GUI(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.win()

    def win(self):
        self.resizable(0,0)
        self.title("FIREWALL-0.0")

        #main frame
        self.mframe=Frame(self)

	
	#menu section
	mnu=menucls(self)
	mnu.menu()        

	#Dock section
	self.dcklt=dockbr(self)
	self.dcklt.dock(self.mframe)
	
     	
	#tab section
	self.spctab=tab()
	self.spctab.ctab(self.mframe)
	
	self.mframe.pack(expand=YES,fill=BOTH)


    def cprght(self):
	copyright.cprght(self)
	

    def crd(self):
	credit.crd(self)

    def hlp(self):
	help.hlp(self)

    def interfaces(self):
	interfaces.intrfc(self)

    def disable(self):
	self.dcklt.disable()

    def policy(self):
	self.spctab.policy()

	
    def enable(self):
	self.dcklt.enable()


    
    def xtra(self):
	xtra.xtrawin(self)
	
