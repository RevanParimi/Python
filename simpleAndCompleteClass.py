class Student:
	def __init__(self, name):
		self.name = name
		self.grades = []
	def addGrade(self, grade):
		self.grades.append(grade)
	def getAverage(self):
		return sum(self.grades)/len(self.grades)
	def printDetails(self):
		print("Name....: {0}".format(self.name))
		print("Grades..: {0}".format(self.grades))
		print("Average.: {0}".format(self.getAverage()))
s2 = Student("Virat")
s2.addGrade(10)
s2.addGrade(20)
s2.addGrade(30)
s2.addGrade(40)
s2.addGrade(50)
s2.printDetails()
