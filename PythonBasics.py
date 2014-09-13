import urllib,re
#################################################################
#INSTAL PYTHON (I recommend C:\Python27)
#https://www.python.org/download/releases/2.7.7/
#Add to System Path
#http://www.howtogeek.com/118594/how-to-edit-your-system-path-for-easy-command-line-access/
#Open Command Prompt in same location as this file and Log.txt
#To Run, Use: Python PythonBasics.py
#################################################################

#Printing data to the console
print "Into to Python!!"

#Declaring variables and assigning values
dictionary={'key':'value','Another Key':'Some Other Value'}
dictionary['A Third Key']='Another Value!!'
list=['some stuff','some more stuff']
list.append('another stuff')
string="WOAH! STUFF!"
int=0

#Opening files
#The variable file is being declared as an instance of the Log.txt file in read-only(r) mode
file=open('Log.txt','r')

#The ReadLines() method takes the text from file, and puts each line into a separate element in the variable 'lines'
lines=file.readlines()

#A For loop basically reads as "For each element (declared as 'line') in the list 'lines', do the following stuff:"
#You may notice that python doesn't have braces or parenthesis to define loops or other sections of code. Python uses colons
#and whitespace to tell the compiler where the sections of code are.
for line in lines:
	#You can repeat strings by adding a multiplication symbol and the number of times you want it repeated.
	#This will add a divider between events
	print '-'*70
	print 'Event as written in log:'
	print line
	
	#Splitting data into a list
	#Split() is a string method used to separate data into a list based on the character passed to it.
	#Remember that the character being split on is removed from the resulting list.
	#Ex: 'abcde'.split('c') >>> ['ab','de']
	data=line.split('\t')

	#Now that the variable data has been declared as a list, you can access different elements based on their
	#index. Indxes in python start at zero, so when you want the first item, you use: data[0]
	#NOTE: '\n' tells python to start a new line
	print '\nFirst Element of Data: %s'%(data[0])
	
	#To see how many elements a list has, use len()
	print '\nNumber of Elements in Data: %i'%(len(data))

	#String formatting
	#Here, we use one of Python's formatting tricks to declare the url variable. By putting a %s in the string,
	#and following it with %(ip), the value of ip gets put in place of %s.
	url='http://api.hostip.info/get_html.php?ip=%s&position=true'%(data[4])	

	#Making web requests
	#urllib is one of the many libraries available to make web requests. By accessing the urlopen method, and
	#passing the url we need, we can read the response from the server and manipulate it in the code.
	#Error Handling
	#Python uses Try/Except to tell the compiler what code to run, and what to do when that code goes bad.
	try:
		response = urllib.urlopen(url).read()
		print '\nLocation Information:'
		print response
	except:
		continue

	#Using Regex
	#Regex is a very powerful tool when analyzing data. Here, we use the "search()" function from the re library.
	#Ex: re.search(r'REGEX STATEMENT HERE', 'TEXT TO SEARCH HERE')
	if re.search(r'.php',data[5]):
		print '\nMatch Found: Event Requests .php page!'
	else:
		print '\nNo Regex Match Found'

#Close the file when you're done using it
file.close()
	
	
#Log Data Examples
# 0: Syslog Time/Event Origin/Log Type: Aug 16 00:15:15 Honeypot apache:
# 1: %t: Event Time: [16/Aug/2014:00:15:15 -0400]
# 2: %A: Local IP: 172.168.168.70
# 3: Log Type: apache
# 4: %a: Remote IP: 91.240.163.111
# 5: %r: Request: "GET / HTTP/1.0"
# 6: %s: Status: 200
# 7: %b: Bytes: 177
# 8: %{Referer}: "-"
# 9: %{User-agent}: User Agent: "masscan/1.0 (https://github.com/robertdavidgraham/masscan)"
# 10: %U: URL Path Requested: /index.html

#More Apache Log Format Information Here:
#http://httpd.apache.org/docs/1.3/mod/mod_log_config.html#formats