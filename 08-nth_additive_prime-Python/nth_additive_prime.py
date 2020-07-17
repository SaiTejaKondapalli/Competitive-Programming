# Write the function fun_nth_additive_prime(n) that takes a non-negative int n
# and returns the nth Additive Prime, which is a prime number such that
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2


def isprime(n):
	count = 0
	for i in range(1, n + 1):
		if n % i == 0:
			count += 1
	if count == 2:
		return True
	return False
def getsum(n):
	summ = 0
	while n > 0:
		summ += n % 10
		n = n // 10
	return summ
def fun_nth_additive_prime(n):
	count = 0
	i = 1
	while True:
		if isprime(i) and isprime(getsum(i)):
			if count == n:
				return i
			count += 1
		i += 1