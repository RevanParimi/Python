import re
s = "Wlcome to Regex...Programming using Python"

lstValues=re.split(r"\s",s)
print("Regex using \s",lstValues)
lstValues=re.split(r"\s+",s)
print(lstValues)
lstValues=re.split(r"(\s)",s)
print(lstValues)
lstValues=re.split("r[a-f]",s)
print(lstValues)
lstValues=re.split("r[a-f][l-n]",s)
print(lstValues)
lstValues=re.split("r([a-f][l-n])",s)
print(lstValues)
lstValues=re.split("r([a-f])",s)
print(lstValues)