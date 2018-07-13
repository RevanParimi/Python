#Find out all words whichhave atleast one Capital alphabet and Atleast one number 
import re
s = "A1bc welcome 2Check paT3ern ano3Ter check3aldTe 22Check"

for item in s.split(" "):
	# [A-Z]* \d
	lstWords = re.search(
		r"(.*[A-Z].*\d.*)|(.*\d.*[A-Z].*)",item)
	if lstWords:
		print(lstWords.group(0))
