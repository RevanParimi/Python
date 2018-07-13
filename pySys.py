import sys

print("System Platform.........:{}".format(sys.platform))
print("System Version..........:{}".format(sys.version))
print("System VerInfo..........:{}".format(sys.version_info))
print("Recursion Limit.........:{}".format(sys.getrecursionlimit))
print("Size of Int (Bytes).....:{}".format(sys.getsizeof(10)))
print("Size of List (Bytes)....:{}".format(sys.getsizeof([])))
print("Size of Dict (Bytes)....:{}".format(sys.getsizeof({})))
print("Windows Version.........:{}".format(sys.getwindowsversion()))
print("System Path.............:{}".format(sys.path))
