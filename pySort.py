li=[9,1,8,4,7,6,2,3,5]
s_li = sorted(li) #Non in place sorting

print("Original List...............:{}".format(li))
print("Sorted new List.............:{}".format(s_li))
print("Original List...............:{}".format(li))
print("Sorting using li.sort method:")
li.sort()
print("Original List...............:{}".format(li))
print("********************************************************")
li1=[9,1,8,4,7,6,2,3,5]
s_li1 = sorted(li1,reverse=True) #Non in place sorting

print("Original List...............:{}".format(li1))
print("Sorted new List.............:{}".format(s_li1))
print("Original List...............:{}".format(li1))
print("Sorting using li.sort method:")
li1.sort(reverse=True)
print("Original List...............:{}".format(li1))
print("********************************************************")
t = (9,1,8,4,7,6,2,3,5)

s_li2 = sorted(t,reverse=True) # Non in place sorting

print("Original tuple..............:{}".format(t))
print("Sorted new List.............:{}".format(s_li2))
print("Sorted new tuple............:{}".format(tuple(s_li2)))
print("Original tuple..............:{}".format(t))

#print("Sorting using li.sort method")
#There is no INPLACE sorting for Tuple STABLE
print("********************************************************")
# Sorting on Dictionaries
d = {"A": 1, "B": 2, "D": 4, "C": 3}
s_D = sorted(d)
s_D_values = sorted(d.values())

print("Original Dictinary..........:{}".format(d))
print("Sorted Dictionary (keys)....:{}".format(s_D)) # default sort is on keys
print("Sorted Dictionary (values)..:{}".format(s_D_values))
print("New Dictionary..............:{}".format(dict(zip(s_D, s_D_values))))

print("********************************************************")

# Sorting based keys

li3 = [-9,1,8,4,-7,6,2,-3,5]
s_li3 = sorted(li3)

print("Original List.........:{}".format(li3))
print("Sorted List...........:{}".format(s_li3))

# Sorting based on absolute values
print("Sorting based on absolute values")
s_li3_abs = sorted(li, key=abs)
print("Sorted List (abs).....:{}".format(s_li3_abs))
print("Sorting Original List using li.sort() method")
li3.sort(key=abs)
print("Oiginal List..........:{}".format(li3))
