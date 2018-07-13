import re
s = '''
<html>
<head>
<title>Current IP Address Allocations
</title>
</head>
<body>
IP Address are 172.45.78.109
LoopBackAddress: 127.0.0.1
Computer 1: 10.67.89.101
Computer 2: 11.67.89.102
Computer 3: 12.67.89.102
</body>
</html>
'''

lstValues = re.findall(
	r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",s)
print("IP Addresses..........: {0}".format(lstValues))
lstValues = re.findall(
	r"[1],[0]\.\d{1,3}\.\d{1,3}\.\d{1,3}",s)
print("IP Addresses..........: {0}".format(lstValues))
lstValues = re.findall(
	r"10\.\d{1,3}\.\d{1,3}\.\d{1,3}",s)
print("IP Addresses..........: {0}".format(lstValues))
