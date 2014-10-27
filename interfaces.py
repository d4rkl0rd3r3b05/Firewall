from Tkinter import *
import os

def intrfc(prntwin):
	mainwin=Toplevel(master=prntwin)
	mainwin.title("INTERFACES :")
	mainwin.resizable(0,0)
	
	root=Frame(mainwin,relief=SOLID,borderwidth=1,bg="black")
	
        #body
	res=os.popen('ifconfig -a',"r").read()
	txt="\n"+res
        body=Text(root,relief=FLAT,bg="black",padx=2,pady=2,fg="#C7C0C0",font=("Comic Sans MS",8,"bold")\
	,height=30,width=80)
	body.insert("1.0",txt)
        body.pack(side=LEFT,expand=YES,fill=BOTH)
       
	hlptxtscrlbar=Scrollbar(root,command=body.yview)
	body["yscrollcommand"]=hlptxtscrlbar.set
	hlptxtscrlbar.pack(side=RIGHT,expand=YES,fill=Y)

    
	root.pack(side=LEFT,anchor=W,expand=YES,fill=Y) 
	mainwin.mainloop()
	
