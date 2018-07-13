import sys
print("SYS.ARGV Details..........{}".format(sys.argv))

if "ascii" in sys.argv:
	print("list all the ascii files")
elif "binary" in sys.argv:
	print("list all the binary files")
elif "c" in sys.argv:
	print("list both ascii and binary files")
else:
	print("Invalid option")