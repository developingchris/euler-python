sequence = [1,2]
evens = 2
while (sequence[-1] < 4000000):
	next = sequence[-2] + sequence[-1]
	if next % 2 == 0:
		evens += next
	sequence.append(next)

print evens
	
