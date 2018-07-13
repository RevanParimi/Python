
class Employee:
	employee_count=1
	def __init__(self,firstName,lastName,age,salary):
		employee_count=0
		self.firstName=firstName
		self.lastName=lastName
		self.age=age
		self.salary=salary
		self.fullName=firstName+" "+lastName
		self.email=firstName+"."+lastName+"@cognizant.com"
		self.employee_count+=1

	def printDetails(self):
		print("First Name.....:{0}".format(self.firstName))
		print("Last Name......:{0}".format(self.lastName))
		print("Full Name......:{0}".format(self.fullName))
		print("Age Name.......:{0}".format(self.age))
		print("Salary Name....:{0}".format(self.salary))
		print("Email ID Name..:{0}".format(self.email))
		print("Employee Count.:{0}".format(self.employee_count))
		print("--------------------------------------------------")

e1 = Employee("Virat","Kohli",32,5000)
e1.printDetails()
e2 = Employee("R","Ashwin",33,7000)
e2.printDetails()
#e1.printDetails()

print("e1 dict..............: {0}".format(e1.__dict__))
print("--------------------------------------------------")
print("e2 dict..............: {0}".format(e2.__dict__))
print("--------------------------------------------------")
print("Employee dict........: {0}".format(Employee.__dict__))
e3 = Employee("MS","Dhoni",35,8000)
#e1.printDetails()