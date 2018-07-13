x=[]
for i in range(1000,3001):
	num = str(i)
	if (int(num[0])%2==0 and int(num[1])%2==0 and int(num[2])%2==0 and int(num[3])%2==0):
		x.append(num)
print x