
import sqlite3,csv
def maptoloc():
	flag=0
	con=sqlite3.connect("dbip.db")
	con.text_factory=str
	cur=con.cursor()

	cur.execute("DROP TABLE IF EXISTS iploc")
	cur.execute("DROP TABLE IF EXISTS cache_table")

	f1=open("ipcountandlocation.csv","w")
	f=open("ipcount.csv","rU")
	reader=csv.reader(f,delimiter=',')
	for el in reader:
		if(flag==0):
			flag=1
		
		else:
			ip=el[0]
			ct=el[1]
#ip=raw_input("enter IP ADDRESS: ")
			intiplist=ip.split(".")
	#print intiplist
	#q=intiplist[0]
	#print q

			a=int(intiplist[0])*256**3
			b=int(intiplist[1])*256**2
			c=int(intiplist[2])*256
			d=int(intiplist[3])*1
			intip=int(a+b+c+d)
		
#print intip
#print type(intip)
#for el in cur.execute("SELECT ipaddress1,ipaddress2 from ipdb WHERE country_code LIKE 'IN%"):
	#print el

			r=cur.execute("SELECT * FROM ipdb WHERE int_ip1<=? AND int_ip2>?",(intip,intip,)).fetchall()
			ipmap=map(list,r)
			if(len(ipmap)==0):
			
				break
			else:
			
				f1.write(ip+","+str(ct)+","+ipmap[0][4]+","+ipmap[0][5]+","+ipmap[0][6]+"\n")
	f1.close()

	f.close()
	con.commit()
	con.close()
