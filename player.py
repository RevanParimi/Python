#Args
def printPlayerDetails(*args):
	print(args)
	print(type(args))
	if args[0] == "V1":
		print("Name.......:{0}".format(args[1]))
		print("Age........:{0}".format(args[2]))
		print("Team.......:{0}".format(args[3]))
	elif args[0] == "V2":
		print("Name.......:{0}".format(args[1]))
		print("Age........:{0}".format(args[2]))
		print("Team.......:{0}".format(args[3]))
		print("Price......:{0}".format(args[4]))
	print("==========================")
printPlayerDetails("V1","Virat",32,"RCB")
printPlayerDetails("V2","Dhoni",35,"RPS","100000")
print('***************  Using Dictionary  ****************')
#kwargs ==> Dictionary
def printStudentDetails(**kwargs):
	print(kwargs)
	print(type(kwargs))
	print("Student details : ")
	print("Name.......:{0}".format(kwargs["name"]))
	print("Age........:{0}".format(kwargs["age"]))
	print("Marks......:{0}".format(kwargs["marks"]))
	print("Stream.....:{0}".format(kwargs["stream"]))
	print("===========================")
printStudentDetails(name="Mary",age=15,marks=25,stream="ECE")
d={"name":"Mike","age":16,"marks":32,"stream":"CSE"}#d is dictionary ** is used while passing through function
printStudentDetails(**d)
print('**************  Using Tuple  *****************')
#kwargs ==> Dictionary
def printStudentDetails1(name,age,marks,stream):
	print("Student details : ")
	print("Name.......:{0}".format(name))
	print("Age........:{0}".format(age))
	print("Marks......:{0}".format(marks))
	print("Stream.....:{0}".format(stream))
	print("===========================")
printStudentDetails1("Mary",15,25,"ECE")
p=("Mike",16,32,"CSE")#d is tuple * is used while passing through function
printStudentDetails1(*p)
p1={"name":"Tom","age":20,"marks":900,"stream":"civil"}
printStudentDetails1(**p1)
#print(*p1)
printStudentDetails1(*p1)#Not the correct way
print('**********************************************')
def foo(x=None):
	if x is None:
		x = []
	x.append(1)
	return x
print(foo())
print(foo())