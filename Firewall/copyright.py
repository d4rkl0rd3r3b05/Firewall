from Tkinter import *

def cprght(prntwin):
	mainwin=Toplevel(master=prntwin)
	mainwin.title("COPYRIGHT :")
	mainwin.resizable(0,0)
	
	root=Frame(mainwin,relief=SOLID,borderwidth=1,bg="black")
	#logo
        cplogo = PhotoImage(file="icon/copylogo.gif")
        logo=Label(root,image=cplogo,relief=FLAT,bg="green")
        logo.photo=cplogo
        logo.pack(side=TOP,anchor=CENTER,expand=YES,fill=X)
        #body
        txt="\n"*4+"NOT RIGHT PROTECTED."+"\n"+"JUST COPY AND HAVE FUN !!!"+"\n"*4
        body=Label(root,text=txt,relief=FLAT,bg="green",padx=115,pady=3,fg="black",font=("FreeSerif", 14,"bold"))
        body.pack(side=TOP,expand=YES,fill=BOTH)
       
    
	root.pack(side=LEFT,anchor=W,expand=YES,fill=Y) 
	mainwin.mainloop()
	
