# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it.
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.
import math
def primefactors(n):
	factors = []
	while n % 2 == 0:
		factors.append(2)
		n /= 2
	for i in range(3, int(math.sqrt(n)) + 1, 2):
		while n % i == 0:
			factors.append(i)
			n /= i
	if n > 2:
		factors.append(n)
	return factors
def ispowerful(n):
	for i in list(set(primefactors(n))):
		if n % i != 0 or n % (i*i) != 0:
			return False
	return True
def nthpowerfulnumber(n):
	# Your code goes here
	i = 1
	count = 0
	while True:
		if ispowerful(i):
			if count == n:
				return i
			count += 1
		i += 1

