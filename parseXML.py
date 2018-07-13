import re

#<car>kwid</car>
#<year>2015</year>
#<rating>Good</rating>

fh=open("Sample.xml")

for line in fh:
	result = re.search(r"<([a-z]+)>(.*)</\1>", line)
	if result:
		print "The '{}' line is valid XML".format(line) 
		print(result.group(1) + "----" + result.group(2))
	else:
		print "The '{}' line is invalid XML {0}".format(line) 
	print("-------------------------------------------")
fh.close()