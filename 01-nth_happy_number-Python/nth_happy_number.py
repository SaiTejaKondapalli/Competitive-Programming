# Write the function nthHappyNumber(n) which takes a non-negative integer
# and returns the nth happy number (where the 0th happy number is 1).
# Here are some test assertions for you:
# assert(nthHappyNumber(0) == 1)
# assert(nthHappyNumber(1) == 7)
# assert(nthHappyNumber(2) == 10)
# assert(nthHappyNumber(3) == 13)
# assert(nthHappyNumber(4) == 19)
# assert(nthHappyNumber(5) == 23)
# assert(nthHappyNumber(6) == 28)
# assert(nthHappyNumber(7) == 31)

def sumofdigits(n):
	summ = 0
	while n > 0:
		dig = n % 10
		summ = dig * dig
		n /= 10
	return summ
def happy(n):
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
def fun_nth_happy_number(n):
	count = 0
	i = 0
	while True:
		if i == 0:
			i += 1
			return 1
		if happy(i):
			count += 1
			if count == n:
				return i
		i += 1