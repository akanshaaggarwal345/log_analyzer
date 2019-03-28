import sqlite3,csv
def pushtodb():
	con=sqlite3.connect("dbip.db")
	con.text_factory=str
	cur=con.cursor()
	list1=[]
	f=open("iprange.csv","rU")
	reader=csv.reader(f,delimiter=',')
	cur.execute("DROP TABLE IF EXISTS ipdb")
	cur.execute("DROP TABLE IF EXISTS cache_table")
	cur.execute("CREATE TABLE ipdb(ipaddress1 text,int_ip1 int,ipaddress2 text,int_ip2 int,country_code text,city text,state text)")
	cur.execute("CREATE TABLE cache_table(ipaddress1 text,int_ip1 int,ipaddress2 text,int_ip2 int,country_code text,city text,state text,count int)")
	for row in reader:
		ipaddress1=row[0]
		int_ip1=row[1]
		ipaddress2=row[2]
		int_ip2=row[3]
		country_code=row[4]
		city=row[5]
		state=row[6]
	
		cur.execute("INSERT INTO ipdb(ipaddress1,int_ip1,ipaddress2,int_ip2,country_code,city,state)VALUES(?,?,?,?,?,?,?)",(ipaddress1,int_ip1,ipaddress2,int_ip2,country_code,city,state))
	


	
			
	con.commit()
	con.close()
	
	


	
	
	  
					 
 
					

                           
                
