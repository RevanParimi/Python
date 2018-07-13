def make_counter(x):
	print 'entering make_counter'
	while True:
		yield x
		print 'incrementing x'
		x += 1
counter=make_counter(3)

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))