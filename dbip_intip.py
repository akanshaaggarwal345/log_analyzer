#here IP address is converted from dotted decimal to integer.using the formula-(x.yz.w)=x*16777216 + y*65536 + z*256 + w
import csv
def dbipint():
	file2=open("iprange.csv","w") #create new file which holds ip along with its decimal value
	file2.write("ip1,intip1,ip2,intip2,country_code,city,region\n") #header of the file
	i=0
	with open('dbip.csv','r')as f:
    		r=csv.reader(f)
    		dbiplist=[]
    		for row in r:
        
        		if len(row)!=0:
            			dbiplist.append(row)
            			ip1=dbiplist[i][0]#extract ipaddress from dbipcsv that is present in 1st column
            			l1=ip1.split(".")#convert using the formula mentioned above
            			a=int(l1[3])*1
            			b=int(l1[2])*256
            			c=int(l1[1])*256**2
            
            			d=int(l1[0])*256**3
            
            			intip1=a+b+c+d
           			ip2=dbiplist[i][1]#store it in the next row to dotted decimal
            			l2=ip2.split(".")
            			e=int(l2[3])*1
            
            			f=int(l2[2])*256
            			g=int(l2[1])*256**2
            
            			h=int(l2[0])*256**3
            			intip2=e+f+g+h
            			file2.write(str(ip1)+" , "+str(intip1)+" , "+str(ip2)+" , "+str(intip2)+" , "+dbiplist[i][2]+" , "+dbiplist[i][3]+" , "+dbiplist[i][4]+"\n")
            			i=i+1
            			
            
file2.close()

            
            			
       
	
	

