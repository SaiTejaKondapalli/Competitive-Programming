# A happy prime is a number that is both happy and prime.
# Write the function nthHappyPrime(n) which takes a non-negative integer
# and returns the nth happy prime number (where the 0th happy prime number is 7).


def sumofdigits(n):
	summ = 0
	while n > 0:
		dig = n % 10
		summ += dig*dig
		n = n // 10
	return summ
def ishappy(n):
	s = set()
	s.add(n)
	while True:
		if n == 1:
			return True
		n = sumofdigits(n)
		if n in s:
			return False
		s.add(n)
	return False
def isprime(n):
	count = 0
	for i in range(1,n+1):
		if n % i == 0:
			count += 1
	if count == 2:
		return True
	return False
def fun_nth_happy_prime(n):
	count = 0
	i = 0
	while True:
		if ishappy(i) and isprime(i):
			count += 1
			if count - 1 == n:
				return i
		i += 1