import pickle
fh=open("TeamList","rb")
contents = pickle.load(fh)
fh.close()
print(contents)
print(type(contents))