#Here we are going to parse our log files and save them in a csv file named as log_contents.csv.
#The log file we have is an apache logfile in combined log format 
#Log Format: "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-agent}i\""
# %h: IP Address
# %l: remote logname
# %u:user id of the requester
# %t: Date and Time
# %r: It represents three important information method,resource accessed,protocol used
# %>s: This is status code that server sends back to the client
# %b: size of the object returned to the client.
# %{Refer}i: This gives the site that the client reports having been referred from
# %{User-agent}i: The User-Agent HTTP request header. This is the identifying information that the client browser reports about itself.
# So the log is going to look like :
#199.30.24.222 - - [31/May/2017:01:17:49 +0530] "GET /images/img2.jpg HTTP/1.1" 200 16276 "-"
#"Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) 
#Version/7.0 Mobile/11A465 Safari/9537.53 BingPreview/1.0b"
import glob 
import re

file2=open("log_contents.csv","w") # creating the new file
#defining splitcount functions to split  the contents of log file
def splitcontent(logfiles):
	file1=open(logfiles,"r")#apache combined log format
	file2.write("IP ADDRESS,DATE AND TIME,METHOD AND PROTOCOL,STATUS,SIZE\n") # header of our file
	for line in file1:
		list1=line.split("]")[0].split("[")[0].split(" ")
		# split till date first and then split based on " " and store the contents in a list
		del(list1[3])
    		# extract the useful information from the list
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
		
   

		file2.write(ipaddress+ "," +date+","+method+","+status+","+size+"\n") #write back to the file
	file1.close()


