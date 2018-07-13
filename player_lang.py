#Empty Dictionary
players={}
print(type(players))
#Empty Set
languages=set()
print(type(languages))
print('*****************************************')
#range 
r=range(0,10)
print(r)
print(type(r))
#List from the range
print(list(r))
#tuple from range
print(tuple(r))
print('*****************************************')
#range 
k=range(5,51,10)
print(k)
print(type(k))
#list from range
print(list(k))
#Tuple from range
print(tuple(k))
print('*****************************************')
animals={"lion","cat","dog","cow","lion","Dog","fox"}
print(animals)
print(type(animals))
print('*****************************************')
#sets
#Unique Collection of items
#Syntax: {} / set()
a=set("Bangalore")
print(a)
print(type(a))
b=set("Singapore")
print(b)
# a | b
print("A | b :", a | b)
# a - b
print("a - b :",a - b)
# a & b
print("A & b :",a & b)
# b - a
print("b - a :",b - a)
print('******************************************')
#Functions == Methods
def myFunction():
	print("I am in myFunction ")
myFunction()
print('*******************************************')
#Find the maximum among the two
def findMaximum(x, y):
	if x>y:
		return x
	else:
		return y
result=findMaximum(3.9,3.5)
print(result)
print('*******************************************')
#Factorial of a number
def iterfactorial(number):
	result=1
	for item in range(1,number+1):
		result=result*item
	return result
print(iterfactorial(5))
print('********************************************')
#Factorial of number
#recursion
#5! = 5 * 4!
def recurfactorial(number):
	if number==0 or number==1:
		return 1
	else:
		return number*recurfactorial(number-1)
print(recurfactorial(5))
print('*******************************************')
def defaultArgumentFunction(x=10):
	print("The value of x is: ",x)
defaultArgumentFunction()
defaultArgumentFunction(99)
defaultArgumentFunction("Hello World")
#defaultArgumentFunction([4,5,6])
#defaultArgumentFunction((4,5,6))
#defaultArgumentFunction({4,5,6})
#defaultArgumentFunction({})
print('*******************************************')
myFunction()