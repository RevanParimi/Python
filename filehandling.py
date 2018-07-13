try:
	fh = open("ExceptionHandling.txt","w")
	fh.write("opening the file\n")
	fh.write("Enter any number: \n")
	userInput = input("Enter any number :")
	fh.write("The user entered number is: "+ str(userInput) + " \n")
	result = 100/int(userInput)
	fh.write("The result is : "+ str(result)+"\n")
	print("Result.......: {0}".format(result))
except ValueError:
	print("Please enter only numbers")
except ZeroDivisionError:
	print("Please enter other than zero")
finally:
	fh.write("Closing the file.\n")
	fh.close()
print('*****************************************************')
runscored=1
def localFunction():
	runscored=2
	print("The value of runscored in localFunction() is {0}".format(runscored))
def GlobalFunc():
	global runscored
	runscored=3
	print("The value of eunscored in GlobalFunc() is {0}".format(runscored))
print("The value of runscored in main : {0}".format(runscored))
localFunction()
print("After calling localFunction(). The value of runscored in main: {0}".format(runscored))
GlobalFunc()
print("After calling GlobalFunc(). The value of runscored in main: {0}".format(runscored))
localFunction()
print("After calling localFunction(). The value of runscored in main: {0}".format(runscored))

