givenL = [("priya",30,999),("Akshay",35,9999),("Atif",60,99999)]
print(givenL)
print("Sorted values by name....:{}".format(sorted(givenL, key=lambda x:x[0])))
print("\n")
print("Sorted values by age.....:{}".format(sorted(givenL, key=lambda x:x[1])))
print("\n")
print("Sorted values by sal.....:{}".format(sorted(givenL, key=lambda x:x[2])))
print("\n")
print("********************************************************")

class Employee:
	def __init__(self, name, age, salary):
		self.name = name
		self.age = age
		self.salary = salary

	def __repr__(self):
		return "{}-{}-{}".format(self.name, self.age, self.salary)
e1 = Employee("ABC", 25, 700)
e2 = Employee("XYZ", 55, 7000)
e3 = Employee("DEF", 65, 70)

lstEmp = [e1, e2, e3]
print("List of Employees........:{}".format(lstEmp))

def sortKeyEmployeeName(emp):
	return emp.name
def sortKeyEmployeeAge(emp):
	return emp.age
def sortKeyEmployeeSalary(emp):
	return emp.salary
sortedLstEmp = sorted(lstEmp, key=sortKeyEmployeeName)
print("Sorted list of Employees (Name)   {}".format(sortedLstEmp))
sortedLstEmp = sorted(lstEmp, key=sortKeyEmployeeAge)
print("Sorted list of Employees (Age)    {}".format(sortedLstEmp))
sortedLstEmp = sorted(lstEmp, key=sortKeyEmployeeSalary)
print("Sorted list of Employees (Salary) {}".format(sortedLstEmp))

print("Reverse Sorting")
sortedLstEmp = sorted(lstEmp, key=sortKeyEmployeeName, reverse=True)
print("Sorted list of Employees (Name)   {}".format(sortedLstEmp))
sortedLstEmp = sorted(lstEmp, key=sortKeyEmployeeAge, reverse=True)
print("Sorted list of Employees (Age)    {}".format(sortedLstEmp))
sortedLstEmp = sorted(lstEmp, key=sortKeyEmployeeSalary, reverse=True)
print("Sorted list of Employees (Salary) {}".format(sortedLstEmp))

print("IN PlCAE SORTING")
lstEmp.sort(key=sortKeyEmployeeName)
print("Sorted List of Employees (Name)   {}".format(lstEmp))
lstEmp.sort(key=sortKeyEmployeeAge)
print("Sorted List of Employees (Age)    {}".format(lstEmp))
lstEmp.sort(key=sortKeyEmployeeSalary)
print("Sorted List of Employees (Salary) {}".format(lstEmp))

print("----------------------------------------------")
print("IN PLACE LAMBDA SORTING")
lstEmp.sort(key=lambda emp:emp.name)
print("Sorted List of Employees (Name)   {}".format(lstEmp))
lstEmp.sort(key=lambda emp:emp.age)
print("Sorted List of Employees (Age)    {}".format(lstEmp))
lstEmp.sort(key=lambda emp:emp.salary)
print("Sorted List of Employees (Salary) {}".format(lstEmp))
