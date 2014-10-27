import os

def prtcl():
	result=os.popen('iptables -L OUTPUT |grep -iv "chain"|grep -iv "prot"| awk \'{print $2}\'',"r").read()
	return result

def src():
	result=os.popen(' iptables -L OUTPUT|grep -iv "chain"|grep -iv "prot" | awk \'{print $4}\'',"r").read()
	return result 


def des():
	result=os.popen('iptables -L OUTPUT |grep -iv "chain"|grep -iv "prot"| awk \'{print $5}\'',"r").read()
	return result 


def pol():
	result=os.popen('iptables -L OUTPUT |grep -iv "chain"|grep -iv "prot"| awk \'{print $1}\'',"r").read()
	return result


def misc():
	result=os.popen('iptables -L OUTPUT|grep -iv "chain"|grep -iv "prot" | awk \'{print $NF}\'',"r").read()
	return result
