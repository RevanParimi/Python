import re
s = "purple alice@google.com abcd helloab@abc.com ------@gmail.com 23@gmail.com"
emails = re.findall(r"[A-Z]*[a-z]+@[\w]+\.[\w]+",s)
for item in emails:
	print(item)