from Tkinter import *

def crd(prntwin):
	mainwin=Toplevel(master=prntwin)
	mainwin.resizable(0,0)	
	mainwin.title("CREDITS :)")
	
	rootl=Frame(mainwin,relief=SOLID,borderwidth=0,bg="white")
	fnt=("Comic Sans MS",8,"bold")
	#--------------------------------------------------------------------------
	crdlogo = PhotoImage(file="icon/credit.gif")
        logo=Label(rootl,image=crdlogo,relief=FLAT,bg="white")
        logo.photo=crdlogo
        logo.pack(side=TOP,anchor=CENTER,expand=YES,fill=X)
	
	#----------------------------------------------------------------------------
	Btfrm=Frame(rootl,relief=SOLID,borderwidth=0,bg="white")	
	
	#Bftfrm
	Bftfrm=Frame(Btfrm,relief=SOLID,borderwidth=0,bg="white")
	mtxt="MAYANK GUPTA"+"\n"+"  (AKA D4RKL0RD)"+"\t"*2
	
	Llbl1=Label(Bftfrm,text=mtxt,relief=SOLID,borderwidth=0,bg="white",fg="black",font=fnt)
	Llbl1.pack(side=TOP,expand=YES,fill=X,anchor=CENTER)
	Bftfrm.pack(side=LEFT,anchor=CENTER)

	Btfrm.pack(side=LEFT,anchor=W)	
	rootl.pack(side=LEFT,anchor=W,expand=YES,fill=Y) 

	mainwin.mainloop()
