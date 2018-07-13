arr = {'Revan':'c++','Atif':'python','Himank':'Java','Akshaya':'Unix','Manish':'Scala','Kiran':'AWS'}
arr1 = {'cisco':'c++','Erricson':'python','Standard':'Java','Bosch':'Unix','Flipkart':'Scala','Capgemini':'Sql'}

print arr
print arr1


dictionary = dict(zip(arr, arr1))
print dictionary
for exp in dictionary:
	
	print exp, " - " ,dictionary[exp]

array=set(arr.values())
array1=set(arr1.values())


print "Remaining Freshers ", array.difference(array1)
print array1.difference(array)

