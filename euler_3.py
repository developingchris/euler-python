import math

def isPrime(test):
	for x in range(2,int(math.floor(math.sqrt(test)))):
		if(test % x == 0):
			return False
	return True

primeFactor = 0
y = 600851475143
current = int(math.floor(math.sqrt(y)))
while primeFactor == 0:
	current = current - 1
	if(y % current == 0 and isPrime(current)):
		 primeFactor = current


print primeFactor

