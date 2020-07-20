# Write the function hasnoprimes(L) that takes a 2d list L of integers,
# and returns True if L does not contain any primes, and False otherwise.

def isprime(n):
	count = 0
	for i in range(1,n+1):
		if n % i == 0:
			count += 1
	return count == 2
def fun_hasnoprimes(l):
	for i in l:
		for each in i:
			if isprime(each):
				return False
	return True

