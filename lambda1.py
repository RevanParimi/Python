
#def MySquare(num):
#	return num*num
#MySquare(5)
print((lambda num : num*num)(11))
print('*******************************************')
#Function as PARAMETER
def mySquare(num):
	return num*num
def myCube(a):
	return a*a*a
#pint(mySquare(5))
def WrapperFunction(funcAsParam,num):
	print(funcAsParam(num))
WrapperFunction(mySquare,8)
WrapperFunction(myCube,8)
print('*******************************************')
#Ags
def SumUsingArgs(*args):
	print(args)
	print(type(args))
	result = 0
	for item in args:
		result += item
	print(result)
SumUsingArgs(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tNos=(100, 200, 300, 400, 500)
SumUsingArgs(*tNos)
print('*******************************************')
#Args
def printPlayerDetails(name, age, team):
	print("Player details:")
	print("Name   : {0}".format(name))
	print("Age    : {0}".format(age))
	print("Team   : {0}".format(team))
	print("---------------------")

printPlayerDetails("Virat",32,"RCB")
Dhoni=("M S Dhoni", 35,"RPS")
printPlayerDetails(*Dhoni)
print('*******************************************')
