import math

seta = range(1,1001)
setb = range(1,1001)

for a in seta:
	for b in setb:
		if((a + b) < 1000):
			c = math.sqrt( math.pow(a,2) + math.pow(b,2))
			if((a + b + c) == 1000):
				print str(a) + " " + str(b) + " " + str(c)
				print a * b * c
		
