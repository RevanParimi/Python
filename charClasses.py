import re
sampleString='''
Rohit made 122 runs, Virat made 96 runs, and Dhawan made 46 runs and we won the match.
'''
# {"Rohit":122, "Virat":96, "Dhawan":46 }
lstNames = re.findall(r"[A-Z][a-z]+",sampleString)
lstScores = re.findall(r"\d{2,3}",sampleString)

print(lstNames)
print(lstScores)

output = dict(zip(lstNames, lstScores))
print(output)