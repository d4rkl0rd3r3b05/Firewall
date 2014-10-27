from Tkinter import *
import polinpt
import polotpt
import polfwd


class polcnsl:
    def show(self,mainfrm):

	txtfont=("FreeSerif", 10,"bold")

	otptpolfrm=Frame(mainfrm,relief=SOLID,borderwidth=1)
	
	self.inptfrm=polinpt.polinpt(otptpolfrm)
	self.otptfrm=polotpt.polotpt(otptpolfrm)
	self.fwdfrm=polfwd.polfwd(otptpolfrm)	
	
	return otptpolfrm


    def reload(self):
	self.inptfrm.reload()
	self.otptfrm.reload()
	self.fwdfrm.reload()


    def clear(self):
	self.inptfrm.clear()
	self.otptfrm.clear()
	self.fwdfrm.clear()
