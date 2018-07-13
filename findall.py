import re
address = "Hi l1    89 Main,4th Cross, 123 road,Marathahalli, 5678 Bangalore"
lstValues = re.findall(r"\d+",address)
print("findall using \\d+....: {0}".format(lstValues))

lstValues = re.findall(r"\d{3}",address)
print("findall using \d{{}}....: {0}".format(lstValues))

lstValues = re.findall(r"\d{2}",address)
print("findall using \d{{2}}....: {0}".format(lstValues))

lstValues = re.findall(r"\s\d{2}\s",address)
print("findall using \s\d{{2}}\\s....: {0}".format(lstValues))

lstValues = re.findall(r"\d{1,3}",address)
print("findall using \d{{1,3}}....: {0}".format(lstValues))
