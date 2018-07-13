def myFunction():
	global temp
	temp="Global Python Variable"
	print(temp)
	print("I am in myFunction")
myFunction()
print("Accessing outside the function : {0}".format(temp))