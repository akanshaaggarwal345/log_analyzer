#read access_log file and generate another file called report_file_all3 which contains ip count of the logs
import glob

import re
from collections import Counter
from operator import itemgetter

myregex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
f2=open("ipcount.csv","w")
f2.write("ipaddress,count\n")
list1=[]

def apache_log_reader(logfile):
    
    
    with open(logfile) as f:
		
		log = f.read()
		my_iplist = re.findall(myregex,log)
		return my_iplist
		
		

def ipcounter(l1):
	length=len(l1)
	j=0
	k=0
	ct=0
	
	for i in range(0,length):
		e1=l1[k]
		e2=l1[j]
		j=j+1
		if(e1==e2):
			ct=ct+1
			
		elif(e1!=e2):
			
			
		
			f2.write(l1[k]+","+str(ct)+"\n")
			k=j
			ct=0
	
	


	
