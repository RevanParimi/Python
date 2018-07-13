try:
	userInput = input("Enter any number : ")
	result=100/int(userInput)
	print("Result is  : {0}".format(result))
except ValueError:
	print("Please enter only numbers")
except ZeroDivisionError:
    print ("This is a DIVIDED BY ZERO error")
except:
	print("Error")
print('*************************************')
