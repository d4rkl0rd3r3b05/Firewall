import os

def prtcl():
	result=os.popen('netstat -anut |grep -iv "active" |grep -iv "proto"|awk \'{print $1}\'',"r").read()
	return result

def src():
	result=os.popen(' netstat -anut |grep -iv "active" |grep -iv "proto"\
	| awk \'{print $4}\' | cut -d: -f1 | sed -e \'/^$/d\'',"r").read()
	return result 


def srcpt():
	result=os.popen('netstat -anut |grep -iv "active" |grep -iv "proto"|awk \'{print $4}\'\
	|awk \'BEGIN {FS=":"};{print $NF}\'',"r").read()
	return result


def des():
	result=os.popen(' netstat -anut |grep -iv "active" |grep -iv "proto"\
	| awk \'{print $5}\' | cut -d: -f1 | sed -e \'/^$/d\'',"r").read()
	return result 

def despt():
	result=os.popen('netstat -anut |grep -iv "active" |grep -iv "proto"|awk \'{print $5}\'\
	|awk \'BEGIN {FS=":"};{print $NF}\'',"r").read()
	return result


def recv():
	result=os.popen('netstat -anut |grep -iv "active" |grep -iv "proto"|awk \'{print $2}\'',"r").read()
	return result


def send():
	result=os.popen('netstat -anut |grep -iv "active" |grep -iv "proto"|awk \'{print $3}\'',"r").read()
	return result


def stt():
	result=os.popen('netstat -anut |grep -iv "active" |grep -iv "proto"|awk \'{print $6}\'',"r").read()
	return result
