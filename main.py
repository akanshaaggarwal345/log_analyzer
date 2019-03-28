import logsplitter
import genipcount
import dbip_intip
import createdbip
import glob
import re
import ipmap2
import pushiplocation
from collections import Counter
list1=[]
if __name__ == '__main__':
	path='/home/ubuntu/Desktop/log/Access_logs/*'
	files=glob.glob(path)
	for file in files:
	
		logsplitter.splitcontent(file)#read all files in the folder apache_log
	
	logsplitter.file2.close()
	for file in files:
	
		x=genipcount.apache_log_reader(file)#read all files in the folder apache_log
		list1=list1+x #store the data in list named list1
	list1.sort(key=lambda ip:map(int,ip.split(".")))
	#sort list1
	genipcount.ipcounter(list1)#count duplicate elements
	dbip_intip.dbipint()
	createdbip.pushtodb()
	ipmap2.maptoloc()
	pushiplocation.pushloc()
