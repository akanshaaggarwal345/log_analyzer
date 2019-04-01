# here we will collect all ipaddresses,their iplocations and their respective ipcounts and  store this information in the file ipcountandlocation.csv
import sqlite3,csv
def maptoloc():
	flag=0
	con=sqlite3.connect("dbip.db")#connect to dbip database that we have created
	con.text_factory=str
	cur=con.cursor()

	cur.execute("DROP TABLE IF EXISTS iploc")
	cur.execute("DROP TABLE IF EXISTS cache_table")

	f1=open("ipcountandlocation.csv","w")#create new file ipcountandlocation.csv
	f=open("ipcount.csv","rU")#read from file ipcount.csv written by genipcount.py
	reader=csv.reader(f,delimiter=',')
	for el in reader:
		if(flag==0):
			flag=1
		
		else:
			ip=el[0]#extract ip address
			ct=el[1]#extract ip count

			intiplist=ip.split(".")#convert ip address from dotted decimal to integer
	

			a=int(intiplist[0])*256**3
			b=int(intiplist[1])*256**2
			c=int(intiplist[2])*256
			d=int(intiplist[3])*1
			intip=int(a+b+c+d)
		

			r=cur.execute("SELECT * FROM ipdb WHERE int_ip1<=? AND int_ip2>?",(intip,intip,)).fetchall()#select the information of all users which are located in the certain location based on their ipranges
			ipmap=map(list,r)
			if(len(ipmap)==0):
			
				break
			else:
			
				f1.write(ip+","+str(ct)+","+ipmap[0][4]+","+ipmap[0][5]+","+ipmap[0][6]+"\n")
	f1.close()

	f.close()
	con.commit()
	con.close()
