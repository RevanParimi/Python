import os
print os.getcwd()

for dirpath, dirnames, filenames in os.walk(os.getcwd()):
	print("Current path...: {}".format(dirpath))
	print("Directories....: {}".format(dirnames))
	print("Files..........: {}".format(filenames))
	print("--------------------------------------------------------------")