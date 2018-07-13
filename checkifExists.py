import os
if not os.path.exists("test"):
	os.mkdir("test")
else:
	print("Directory already exists")