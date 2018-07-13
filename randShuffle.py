import random

numbers = list(range(1, 11))
print("Numbers..........:{}".format(numbers))

random.shuffle(numbers)
print("Shufflesd Numbers:{}".format(numbers))