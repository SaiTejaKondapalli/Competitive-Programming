# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth
# Circular prime, which is a prime number that does not contain any 0's and such that all the
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3,
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime,
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).
import math
def isprime(n):
	if n < 2:
		return False
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	for i in range(3, int(math.sqrt(n))+1, 2):
		if n % i == 0:
			return False
	return True
def iscircularprime(n):
	if "0" in str(n):
		return False
	length = len(str(n))
	if length == 1:
		if isprime(n):
			return True
		return False
	i = 0
	rem = 0
	while i < length:
		rem = n % 10
		n = n // 10
		n = rem * (10 ** (length - 1)) + n
		if not isprime(n):
			return False
		i += 1
	return True

def nthcircularprime(n):
	# Your code goes here
	i = 0
	count = 0
	while True:
		if iscircularprime(i):
			count += 1
			if count == n:
				return i
		i += 1
