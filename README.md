# log_analyzer
In order to manage any application effectively it is very important to keep a record of activities on that application and timely analyze any problem that is occurring with that application. So the information like status, time of execution, message etc is created whenever a program is executed. This information represents log of that program and it is stored in log files. The information stored in these log files can be further analyzed in order to understand and manage our application. This project aims at developing a similar tool using Python Programming which can parse and analyze apache log files. This tool mainly performs three important functions:
First, It should be able to extract useful information from the log files like ip address, date and time, protocol used etc.
Second, this tool should extract the ip addresses from log files and generate their respective counts.
Third, it should generate locations of the IP Addresses.


The use and function of every file is discussed here:

1.PYTHON FILES:

1.1 logsplitter.py: This is a file which parses the contents of log files.This module uses a function splitcontent() to split the contents of the logfile.The contents are splitted by using string split() function based on apache log formats and useful information like ip address,date and time,method used,protocol,status and size are accessed and written to a csv file named log_contents.csv .


1.2 genipcount.py: Now,after parsing our log file ,we will use the ip addresses extracted from the log file to generate an ipcount corrseponding to each ipaddress.This will help us to analyze the user who is using our application very frequently or less frequently etc based on that we can target a less frequent user by providing some offers etc.
This module finds the ipaddress from the logs in logfiles and then stores them in a list and then generate a count of each ipaddress.It uses regular expression for identifying ip addresses from the logs using re module of python.This module has two functions:

 Apache_log_reader : It finds the ip addresses from the logs and stores them in a list.

 Ipcounter : It generates the ip count and write ip and its count to ipcount.csv file


1.3 dbip_intip.py: Now,our next task is to find the locations of the ip addresses.For that,we need the dbip dataset and in order to use this dataset we must convert our ipaddresses(172.23.4.5) from dotted decimal to decimal form and that's what this file performs:
if IP address is 192.168.1.2 then the formula to get its decimal number is: 

192 * 16777216 + 168 * 65536 + 1 * 256 + 2 = 3232235778


1.4 createdbippy :This module creates a small database in sqlite3 named as dbip.db and hen it pushes the data of iprange.csv file to a table named as ipdb in dbip.db.This will help us finding the location of the ip addresses from the database dbip using a simple sqlite query.

1.5 ipmap2.py :This module reads the log file ,extract ip address from the logs and then find corresponding location of these ip addresses using dbip dataset.

1.6 pushiplocation.py: This module pushes the data of ipcountandlocationfile to dbip into a table named iploc and also creates a help table which consists of countrycodes and their corresponding country names.

1.7 main.py: Main module puts everything together and connects all the modules.


2. INPUT FILE: access.01Jun2017


3.DATASET : DBIP DATASET

4.EXECUTION: 

4.1 Copy all the files in a folder

4.2 Run command : python main.py in your terminal.


5.CONCLUSION: We have successfully developed a loganalyzer using python programming that is capable of parsing the apache log files and finding the location of ipaddresses present in the logs,other than that it also generates the count of ipaddresses.As an input we have given a folder named access_logs containing 32 log files.Our code reads each file and performs three different functions:

 Splitting contents of log file

 Generate IP count

 Find location of each ipaddress

