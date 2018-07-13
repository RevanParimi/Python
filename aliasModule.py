#Approach : Alias for Functions
from IPL2017.KKR.venue import printVenue as KKRVenue
from IPL2017.RCB.venue import printVenue as RCBVenue

# as is to create alias
KKRVenue()
RCBVenue()

print("--------------------------")

# Approach : Alias for files
from IPL2017.KKR import venue as KVenueFile
from IPL2017.RCB import venue as RVenueFile
from IPL2017 import venue as MVenueFile

KVenueFile.printStadium()
RVenueFile.printStadium()
MVenueFile.printStadium()