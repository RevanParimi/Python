from datetime import date
def main():
	bornBefore = date(1997,7,11)
	userdate = promptAndExtractDate()
	if userdate is not None:
		if userdate <= bornBefore:
			print("is atleast 21 years old {}".format(userdate))
		else:
			print("is at younger than 21 years {}".format(date))
def promptAndExtractDate():
	print("Enter a birth date\n")
	month = int(input("month(0 to quit):"))
	if month == 0:
		return None
	else:
		day = int(input("Day: "))
		year = int(input("Year: "))
		return date(year,month,day)

main()