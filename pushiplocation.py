import sqlite3,csv
def pushloc():
	flag=0
	con=sqlite3.connect("dbip.db")
	con.text_factory=str
	cur=con.cursor()
	cur.execute("DROP TABLE IF EXISTS help")
	cur.execute("DROP TABLE IF EXISTS iploc")
	cur.execute("CREATE TABLE iploc(ipaddress text,count int,country_code text,city text,region text)")
	cur.execute("CREATE TABLE help(country_code text,country_name text)")
	f4=open("countrycodes.csv","r")
	reader4=csv.reader(f4,delimiter=',')
	for elem in reader4:
	
		country_code=elem[0]
		country_name=elem[1]
		cur.execute("INSERT INTO help(country_code,country_name) VALUES(?,?)",(country_code,country_name))

	f1=open("ipcountandlocation.csv","r")
	reader=csv.reader(f1,delimiter=',')
	for element in reader:
		ipaddress1=element[0]
		count=element[1]
		country_code=element[2]
		city=element[3]
		region=element[4]
		cur.execute("INSERT INTO iploc(ipaddress,count,country_code,city,region) VALUES(?,?,?,?,?)",(ipaddress1,count,country_code,city,region))
	f1.close()
	f4.close()
	con.commit()
	con.close()

