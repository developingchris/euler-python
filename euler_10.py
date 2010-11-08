import math

def isPrime(test):
	root = int(math.floor(math.sqrt(test))) +  1
	z = range(2, root,1)
	for x in z:
		if(test % x == 0):
			return False
	return True



primes = [2,3,5,7,11,13,17]
sum = 58
x = primes[-1]
while x < 2000001:
	x += 1
	if isPrime(x):
		primes.append(x)
		sum += x
		
print sum	
print primes
print primes[-1]
print sum	
