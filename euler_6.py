import math
r = range(1,101)
sum = 0
squares = 0
for x in r:
	sum += x
	squares += math.pow(x,2)

print math.pow(sum,2)
print str(math.pow(sum,2) - squares)