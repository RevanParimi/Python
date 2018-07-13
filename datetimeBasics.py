import datetime
import time

today = datetime.date.today()
print(type(today))
currenttime = datetime.datetime.now()

now=time.time()
print(now)

# EPOCH 1970

print("Today............{}".format(today))
print("Curent time......{}".format(currenttime))
print("Tuple Format.....{}".format(today.timetuple))
print("Ordinal..........{}".format(today.toordinal))
print("Year.............{}".format(today.year))
print("Month............{}".format(today.month))
print("Day..............{}".format(today.day))