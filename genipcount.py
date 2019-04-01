#read access_log file and generate another file called ipcount.csv which contains ip count of the logs
import glob
import re
from collections import Counter
from operator import itemgetter

myregex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}' # Regular expression for IP ADDRESSES
f2=open("ipcount.csv","w") # new file where IP counts will be written
f2.write("ipaddress,count\n") #header of the file
list1=[]
#In this functions we are going to read all the logs and extract ip addresses out of the logs using regular expression and then store these IP addresses in the list1
def apache_log_reader(logfile):
    
    
    with open(logfile) as f:
		
		log = f.read()
		my_iplist = re.findall(myregex,log)
		return my_iplist
		
		
#in this function we are going to generate a count corresponding to each IP address
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
	
	


	
