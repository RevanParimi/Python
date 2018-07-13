from shutil import *
import os

src = os.getcwd() + '\\'+"Files"+ '\\'+"SubFolder\\"
print(src)
dest = "2DeleteTest1"
# rmtree(dest)
copytree(src, dest)