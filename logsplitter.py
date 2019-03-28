import glob
import re

file2=open("log_contents.csv","w")

def splitcontent(logfiles):
	file1=open(logfiles,"r")#apache combined log format
	file2.write("IP ADDRESS,DATE AND TIME,METHOD AND PROTOCOL,STATUS,SIZE\n")
	for line in file1:
		list1=line.split("]")[0].split("[")[0].split(" ")
		del(list1[3])
    
		ipaddress=list1[0]
		uid=list1[1]
		username=list1[2]
		list2=line.split("]")[0].split("[")
		#print list2
		date=list2[1]
   
   
		list3=line.split("]")[1].split("\"")
		#print list3
		list4=line.split("\" ")[1].split(" ")
		
		
		if(list4[0][0]=='H'):
			list5=line.split("\" ")[2].split(" ")
			status=list5[0]
			#print status
			size=list5[1]
			#print size
		else:
			status=list4[0]
			size=list4[1]
		method=list3[1]
		#statusandsize=list3[2]
		#status=statusandsize[0]
		#size=statusandsize[1]
		#referenceaddress=list3[4]
		#useragent=list3[5]
   

		file2.write(ipaddress+ "," +date+","+method+","+status+","+size+"\n")
	file1.close()


