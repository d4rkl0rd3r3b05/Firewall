import os


def blck(prntwin):

	#Echo Request
	if(prntwin.echoreq.get()==True):
		try:
			os.popen('iptables -I INPUT 1 -p icmp --icmp-type echo-request -j DROP',"r")
			os.popen('iptables -I OUTPUT 1 -p icmp --icmp-type echo-request -j DROP',"r")
		except:
			pass

	else:	
		try:
			os.popen('iptables -I INPUT 1 -p icmp --icmp-type echo-request -j ACCEPT',"r")
			os.popen('iptables -I OUTPUT 1 -p icmp --icmp-type echo-request -j ACCEPT',"r")
		except:
			pass


	#Echo Reply
	if(prntwin.echorply.get()==True):
    		try:
			os.popen('iptables -I INPUT 1 -p icmp --icmp-type echo-reply -j DROP',"r")
			os.popen('iptables -I OUTPUT 1 -p icmp --icmp-type echo-reply -j DROP',"r")
		except:
			pass

	else:	
		try:
			os.popen('iptables -I INPUT 1 -p icmp --icmp-type echo-reply -j ACCEPT',"r")
			os.popen('iptables -I OUTPUT 1 -p icmp --icmp-type echo-reply -j ACCEPT',"r")
		except:
			pass

	#Timestamping
	if(prntwin.tymstmpng.get()==True):
		try:
			os.popen('iptables -I INPUT 1 -p icmp --icmp-type timestamp-request -j DROP',"r")
			os.popen('iptables -I OUTPUT 1 -p icmp --icmp-type timestamp-request -j DROP',"r")
		
			os.popen('iptables -I INPUT 1 -p icmp --icmp-type timestamp-reply -j DROP',"r")
			os.popen('iptables -I OUTPUT 1 -p icmp --icmp-type timestamp-reply -j DROP',"r")
		except:
			pass

	else:	
		try:
			os.popen('iptables -I INPUT 1 -p icmp --icmp-type timestamp-request -j ACCEPT',"r")
			os.popen('iptables -I OUTPUT 1 -p icmp --icmp-type timestamp-request -j ACCEPT',"r")
		
			os.popen('iptables -I INPUT 1 -p icmp --icmp-type timestamp-reply -j ACCEPT',"r")
			os.popen('iptables -I OUTPUT 1 -p icmp --icmp-type timestamp-reply -j ACCEPT',"r")
		except:
			pass

	#Address Masking
	if(prntwin.adrsmskng.get()==True):
		try:
			os.popen('iptables -I INPUT 1 -p icmp --icmp-type address-mask-request -j DROP',"r")
			os.popen('iptables -I OUTPUT 1 -p icmp --icmp-type address-mask-request -j DROP',"r")
		
			os.popen('iptables -I INPUT 1 -p icmp --icmp-type address-mask-reply -j DROP',"r")
			os.popen('iptables -I OUTPUT 1 -p icmp --icmp-type address-mask-reply -j DROP',"r")
		except:
			pass

	else:	
		try:
			os.popen('iptables -I INPUT 1 -p icmp --icmp-type address-mask-request -j ACCEPT',"r")
			os.popen('iptables -I OUTPUT 1 -p icmp --icmp-type address-mask-request -j ACCEPT',"r")
		
			os.popen('iptables -I INPUT 1 -p icmp --icmp-type address-mask-reply -j ACCEPT',"r")
			os.popen('iptables -I OUTPUT 1 -p icmp --icmp-type address-mask-reply -j ACCEPT',"r")
		except:
			pass

	#Redirection
	if(prntwin.rdrcsn.get()==True):
		try:
			os.popen('iptables -I INPUT 1 -p icmp --icmp-type redirect -j DROP',"r")
			os.popen('iptables -I OUTPUT 1 -p icmp --icmp-type redirect -j DROP',"r")
		except:
			pass

	else:	
		try:
			os.popen('iptables -I INPUT 1 -p icmp --icmp-type redirect -j ACCEPT',"r")
			os.popen('iptables -I OUTPUT 1 -p icmp --icmp-type redirect -j ACCEPT',"r")
		except:
			pass

	#Source-Quenching
	if(prntwin.srcqnchng.get()==True):
		try:
			os.popen('iptables -I INPUT 1 -p icmp --icmp-type source-quench -j DROP',"r")
			os.popen('iptables -I OUTPUT 1 -p icmp --icmp-type source-quench -j DROP',"r")
		except:
			pass

	else:	
		try:
			os.popen('iptables -I INPUT 1 -p icmp --icmp-type source-quench -j ACCEPT',"r")
			os.popen('iptables -I OUTPUT 1 -p icmp --icmp-type source-quench -j ACCEPT',"r")
		except:
			pass

	#Parameter Problem
	if(prntwin.prmtrprb.get()==True):
		try:
			os.popen('iptables -I INPUT 1 -p icmp --icmp-type parameter-problem -j DROP',"r")
			os.popen('iptables -I OUTPUT 1 -p icmp --icmp-type parameter-problem -j DROP',"r")
		except:
			pass

	else:	
		try:
			os.popen('iptables -I INPUT 1 -p icmp --icmp-type parameter-problem -j ACCEPT',"r")
			os.popen('iptables -I OUTPUT 1 -p icmp --icmp-type parameter-problem -j ACCEPT',"r")
		except:
			pass

	#Unreachable
	if(prntwin.unrchbl.get()==True):
		try:
			os.popen('iptables -I INPUT 1 -p icmp --icmp-type destination-unreachable -j DROP',"r")
			os.popen('iptables -I OUTPUT 1 -p icmp --icmp-type destination-unreachable -j DROP',"r")
		except:
			pass

	else:	
		try:
			os.popen('iptables -I INPUT 1 -p icmp --icmp-type destination-unreachable -j ACCEPT',"r")
			os.popen('iptables -I OUTPUT 1 -p icmp --icmp-type destination-unreachable -j ACCEPT',"r")
		except:
			pass

	#Any
	if(prntwin.any.get()==True):
		try:
			os.popen('iptables -I INPUT 1 -p icmp --icmp-type any -j DROP',"r")
			os.popen('iptables -I OUTPUT 1 -p icmp --icmp-type any -j DROP',"r")
		except:
			pass

	else:	
		try:
			os.popen('iptables -I INPUT 1 -p icmp --icmp-type any -j ACCEPT',"r")
			os.popen('iptables -I OUTPUT 1 -p icmp --icmp-type any -j ACCEPT',"r")
		except:
			pass

	


