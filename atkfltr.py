import os


def blck(prntwin):

	#SYN Attack
	if(prntwin.syn.get()==True):
		try:
			os.popen('iptables -A INPUT -p tcp ! --syn -m state --state NEW -j DROP',"r")
		except:
			pass
	else:	
		try:
			os.popen('iptables -A INPUT -p tcp ! --syn -m state --state NEW -j ACCEPT',"r")
		except:
			pass


	#Server-Panic Attack
	if(prntwin.srvrpnc.get()==True):
    		try:
			os.popen('iptables -A INPUT -f -j DROP',"r")
		except:
			pass
	else:	
		try:
			os.popen('iptables -A INPUT -f -j ACCEPT',"r")
		except:
			pass

	#XMAS-Attack
	if(prntwin.xmas.get()==True):
		try:
			os.popen('iptables -A INPUT -p tcp --tcp-flags ALL ALL -j DROP',"r")
		except:
			pass
	else:	
		try:
			os.popen('iptables -A INPUT -p tcp --tcp-flags ALL ALL -j ACCEPT',"r")
		except:
			pass

	#NULL Attacks
	if(prntwin.null.get()==True):
		try:
			os.popen('iptables -A INPUT -p tcp --tcp-flags ALL NONE -j DROP',"r")
		except:
			pass
	else:	
		try:
			os.popen('iptables -A INPUT -p tcp --tcp-flags ALL NONE -j ACCEPT',"r")
		except:
			pass

