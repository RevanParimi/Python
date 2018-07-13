import re
empDetails = "Hi I have  a credit card with number 3775 123456 78910 and other card is "\
				"3545 45789 12345"

#http://www.getcreditcardnumbers.com
#AMEX card
#Second Digit is either 4 or 7
# <4 digit> <6 digit> <5 digit>

lstValues=re.findall(
	r"3[4|7]\d{2}\s{1}\d{6}\s{1}\d{5}",empDetails)
print(lstValues)
print(empDetails)