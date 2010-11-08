
def palindrome():
	max = 0
	r = range(999,99,-1)
	for x in r:
		for y in r:
			pal = str(x * y)
			halfway = len(pal) / 2
			notpal = False
			for t in range(0,halfway):
				if(pal[t] != pal[len(pal) - (t + 1)]):
					notpal = True
			if(notpal == False and int(pal) > max):
				print str(x) + " " + str(y)
				print pal + " " + str(max)
				max = int(pal)
	return max
			
print palindrome()		