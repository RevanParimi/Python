fh = open("ExceptionHandling.txt","a")
print(fh)
print(type(fh))
fh.write("=============================\n")
fh.write("esting append operations on the file.\n")
fh.write("Done with append operation\n")

fh.close()
