import csv
def dbipint():
	file2=open("iprange.csv","w")
	file2.write("ip1,intip1,ip2,intip2,country_code,city,region\n")
	i=0
	with open('dbip.csv','r')as f:
    		r=csv.reader(f)
    		dbiplist=[]
    		for row in r:
        
        		if len(row)!=0:
            			dbiplist.append(row)
            			ip1=dbiplist[i][0]
            			l1=ip1.split(".")
            			a=int(l1[3])*1
            
            			b=int(l1[2])*256
            			c=int(l1[1])*256**2
            
            			d=int(l1[0])*256**3
            
            			intip1=a+b+c+d
           
            #print intip
            #print b
            
            
            			ip2=dbiplist[i][1]
            			l2=ip2.split(".")
            			e=int(l2[3])*1
            
            			f=int(l2[2])*256
            			g=int(l2[1])*256**2
            
            			h=int(l2[0])*256**3
            			intip2=e+f+g+h
            			file2.write(str(ip1)+" , "+str(intip1)+" , "+str(ip2)+" , "+str(intip2)+" , "+dbiplist[i][2]+" , "+dbiplist[i][3]+" , "+dbiplist[i][4]+"\n")
            			i=i+1
            #print intip
            #print l1
            #print l2
            #print ip1+" "+ip2
#print list1

#f.close()
	
	file2.close()
#with open('excel2.csv','w')as f:

