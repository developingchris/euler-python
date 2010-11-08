
smallest = 0
x = 20
twenty = range(20,0,-1)
while smallest == 0:
	x += 20
	divis = True
	for y in twenty:
		if(y < 5):
			print str(x) + " " + str(y)
		if(x % y != 0):
			divis = False
			break
	if(divis == True):
		smallest = x
print x