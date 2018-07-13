import subprocess
#subprocess module intends to replace several older modules and functions like os.system, os.spawn*
#p1 = subprocess.Popen(["ping","www.google.com"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
p1 = subprocess.Popen(["ping","216.58.220.36"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#subprocess.Run() was added in Python 3.5 ( the most prefered way)
print(p1)
print(type(p1))
#Popen.communicate() is used to interact with process. It can take optional input argument that can be sent to the subprocess
#Poepn.communicate() returns tuple (stdout_data,stdout_err)
output = p1.communicate()[0]
print(output)
error = p1.communicate()[1]
print(error)