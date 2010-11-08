import math

def isPrime(test):
	root = int(math.floor(math.sqrt(test))) +  1
	z = range(2, root,1)
	#print z
	for x in z:
		if(test % x == 0):
			return False
	return True





primes = [2,3,5,7,11,13,17]
x = primes[-1]
while len(primes) < 10001:
	x += 1
	if isPrime(x):
		primes.append(x)
		
print len(primes)
print primes
print primes[-1]
	
