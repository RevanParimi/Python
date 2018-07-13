import time

def GetListOfNumbers(maxNumber):
	start=0
	lsNos = []
	while start <= maxNumber:
		yield start
		start += 1
start_time = time.time()
print(sum(GetListOfNumbers(10000000)))
end_time = time.time()
print "Total Time : {}".format(end_time-start_time)