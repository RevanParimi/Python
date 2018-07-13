import pickle
ctTeam = {"groupA" :["England","Bangladesh","Australia","Srilanka"]\
		  ,"groupB":["India","Pakistan","NewZealand","South Africa"]}
fh = open("TeamList","wb")
pickle.dump(ctTeam,fh)
print(fh)
fh.close()