fruits={"a":"apple","b":"banana","c":"cherry"}
#Length of dictionary
print(len(fruits))
#Add a key-value pair to dict
fruits["o"]="orange"
print("After adding element: ",fruits)
#Accessing  the elements
print("Accessing the elements: ")
print(fruits["a"])
print(fruits["b"])
#Deleting the elements (key-value pair)
print("Deleting the element")
result=fruits.pop("c")
print(result)
print(fruits)
#Get the keys in the dict
print("Keys: ",fruits.keys())
print("Values: ",fruits.values())
print("Key-Value: ",fruits.items())