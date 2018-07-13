import re
l1 = ["python","2.7","python 2.7"]

for item in l1:
	re1 = re.findall(r'\W',item)
	if re1:
		print(item + " : {0}".format(re1))
	else:
		print("Not Found")