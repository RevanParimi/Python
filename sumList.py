import time

def GetListOfNumbers(maxNumber):
	start=0
	lsNos = []
	while start <= maxNumber:
		lsNos.append(start)
		start += 1
	return lsNos
start_time = time.time()
print(sum(GetListOfNumbers(10000000)))
end_time = time.time()
print "Total Time : {}".format(end_time-start_time)