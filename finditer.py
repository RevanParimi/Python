import re
#Today's date is june 19 2017
s = "Today's date is June 19 2017 August 07 2018"

pattern = r"([A-Z][a-z]+)\s{1}(\d{1,2})\s{1}(\d{4})"
matches = re.finditer(pattern,s)
for match in matches:
	print("Match at index start: {{}}, End: {{}}. {0}".format(match.start(), match.end()))
	print("Result is : {0}".format(match.group(0)))
	print("Month is  : {0}".format(match.group(1)))
	print("Day is    : {0}".format(match.group(2)))
	print("Year is   : {0}".format(match.group(3)))
	print("------------------------------------------------")