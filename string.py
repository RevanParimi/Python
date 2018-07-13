def defaultArgumentFunction(x=10):
	print("The value of x is:{0} ".format(x))
#	print("Inside defaultArgumentFunction")


defaultArgumentFunction()
defaultArgumentFunction(99)
defaultArgumentFunction("Hello World")
defaultArgumentFunction([4,5,6])
defaultArgumentFunction((4,5,6))
defaultArgumentFunction({4,5,6})
defaultArgumentFunction({})
def namedArgumentFunction(a,b,c):
	print("The values are a: {}, b: {}, c: {}".format(a,b,c))
namedArgumentFunction(100,200,300)
#To copy a line Ctrl + d
namedArgumentFunction(c=5,b=4,a=3)
namedArgumentFunction("X",b="Y",c="Z")
#print("Execution 2")
print('**********************************************')
#lambda Function
#Anonymous Functions
#Functions which have got no names,generally used to write one line functions
f=lambda num : num*num
print(f(10)) 