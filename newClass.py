class Employee:
	def __init__(self,firstName,lastName,age,salary):
		self.firstName=firstName
		self.lastName=lastName
		self.age=age
		self.salary=salary
		self.email=firstName+"."+lastName+"@cognizant.com"
		self.fullName=firstName+" "+lastName
	#def fullName(self):
		#return self.firstName+" "+self.lastName
	def printDetails(self):
		print("Name of the Employee is : {0}".format(self.fullName))
		print("Age of the Employee is : {0}".format(self.age))
		print("Salary of the Employee is : {0}".format(self.salary))
		print("Email Id is : {0}".format(self.email))
s1=Employee("Himank","Sharma",23,50000)
s1.printDetails()
print("self1 dict................: {0}".format(s1.__dict__))