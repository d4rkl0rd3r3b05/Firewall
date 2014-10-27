import os
import tkMessageBox


def default():
	if (not tkMessageBox.askyesno("Default Settings", "Do you really want to force Default Settings?")):
		return
	os.popen('iptables -F',"r")
	os.popen('iptables -A INPUT -p tcp -s 0/0 --dport 1:1024 -j DROP',"r")
	os.popen('iptables -A INPUT -p udp -s 0/0 --dport 1:1024 -j DROP',"r")
	os.popen(' iptables -A INPUT -p ICMP -s 0/0 -j DROP',"r")
	tkMessageBox.showinfo("Default Settings","Default Settings has been applied.")
	



	
