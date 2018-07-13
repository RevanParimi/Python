class Employee:
	def __init__(self,firstName):
		self.fn = firstName
e1=Employee("Virat")
e2=Employee("Dhoni")

print("e1 dict..........:{0}".format(e1.__dict__))
print("e2 dict..........:{0}".format(e2.__dict__))
print("Employee dict....:{0}".format(Employee.__dict__))
